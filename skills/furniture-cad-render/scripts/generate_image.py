#!/usr/bin/env python3
"""
generate_image.py — Turns an extracted furniture structure (from vision_extract.py)
into a photorealistic preview render via Qwen-Image.

Requires: DASHSCOPE_API_KEY environment variable.
Requires: pip install dashscope
"""

import os
import json
import argparse
from dashscope import MultiModalConversation

MODEL = "qwen-image-2.0-pro"
EDIT_MODEL = "qwen-image-edit-plus"  # used for reference-conditioned angles, see generate_render_from_reference
SIZE = "2048*2048"  # presentation-quality resolution, per design spec


def build_prompt(structure, material_notes, angle):
    """Turn the structured CAD extraction into a text-to-image prompt.

    Only uses what was actually extracted — the whole point of the earlier
    vision_extract step is that this function never has to guess structure.
    """
    piece = structure.get("piece_type", "furniture piece")
    dims = structure.get("overall_dimensions_mm", {})
    dims_str = ", ".join(f"{k}={v}mm" for k, v in dims.items() if v)
    components = structure.get("components", [])
    comp_str = "; ".join(
        f"{c.get('count', 1)}x {c.get('name')}" + (f" ({c['dimensions_mm']})" if c.get("dimensions_mm") else "")
        for c in components
    )
    material = material_notes or structure.get("material_or_color_notes") or "natural wood tone, standard upholstery-safe finish for this furniture type (unspecified by designer — treat as a placeholder, not a client decision)"

    prompt = (
        f"Photorealistic product photography of a {piece}. "
        f"Overall dimensions: {dims_str}. "
        f"Structure/components: {comp_str}. "
        f"Material/finish: {material}. "
        f"Camera angle: {angle}. "
        f"Studio lighting, neutral background, catalog/showroom quality, sharp focus, "
        f"accurate proportions matching the stated dimensions — do not add decorative "
        f"features, extra components, or structural changes not listed above."
    )
    return prompt


def generate_render(structure, material_notes, angle, api_key=None):
    """Generate one render for the given angle from text alone. Use this ONLY for the
    first ("hero") angle of a version — every subsequent angle should be generated
    with generate_render_from_reference() instead, so they can't independently drift
    on details (leg style, hardware, exact material tone) that the structure JSON
    doesn't fully pin down. Returns the image URL from Qwen-Image.
    """
    api_key = api_key or os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("Set DASHSCOPE_API_KEY (Capafy execution environment should inject this).")

    prompt = build_prompt(structure, material_notes, angle)
    messages = [{"role": "user", "content": [{"text": prompt}]}]

    response = MultiModalConversation.call(
        api_key=api_key,
        model=MODEL,
        messages=messages,
        n=1,
        size=SIZE,
        watermark=False,
        prompt_extend=True,
    )

    if response.status_code != 200:
        raise RuntimeError(f"Qwen-Image call failed: {response.code} - {response.message}")

    image_url = response.output.choices[0].message.content[0]["image"]
    return {"angle": angle, "image_url": image_url, "prompt_used": prompt}


def generate_render_from_reference(reference_image_url, structure, material_notes, angle, api_key=None):
    """Generate a new angle of the SAME piece by conditioning on an already-generated
    reference image (typically the hero angle from generate_render), instead of
    generating from text alone.

    Why this exists: two independent text-to-image calls for "front view" and "side
    view" of the same furniture are two separate guesses — the model can render
    different leg styles, hardware, or material tone each time, since the structure
    JSON specifies dimensions and components but not every visual detail. Feeding the
    actual pixels of an already-generated, already-verified angle back in as a
    reference via Qwen-Image-Edit keeps every subsequent angle visually consistent
    with it, because the model has something concrete to match instead of
    re-imagining the piece from scratch.
    """
    api_key = api_key or os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("Set DASHSCOPE_API_KEY (Capafy execution environment should inject this).")

    piece = structure.get("piece_type", "furniture piece")
    prompt = (
        f"This image shows a {piece}. Generate this exact same piece — identical "
        f"material, color, hardware, and proportions, no design changes — but shown "
        f"from a different camera angle: {angle}. Studio lighting, neutral "
        f"background, catalog/showroom quality. Only the camera angle should change."
    )
    content = [{"image": reference_image_url}, {"text": prompt}]
    messages = [{"role": "user", "content": content}]

    response = MultiModalConversation.call(
        api_key=api_key,
        model=EDIT_MODEL,
        messages=messages,
        n=1,
        watermark=False,
    )

    if response.status_code != 200:
        raise RuntimeError(f"Qwen-Image-Edit call failed: {response.code} - {response.message}")

    image_url = response.output.choices[0].message.content[0]["image"]
    return {"angle": angle, "image_url": image_url, "prompt_used": prompt, "reference_used": reference_image_url}


def main():
    parser = argparse.ArgumentParser(description="Generate a photorealistic furniture render")
    parser.add_argument("--structure", required=True, help="Path to structure JSON from vision_extract.py")
    parser.add_argument("--material", default=None, help="Optional material/color notes from the designer")
    parser.add_argument("--angles", nargs="+", default=["3/4 front view", "side view"])
    args = parser.parse_args()

    with open(args.structure) as f:
        structure = json.load(f)

    results = [generate_render(structure, args.material, angle) for angle in args.angles]
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
