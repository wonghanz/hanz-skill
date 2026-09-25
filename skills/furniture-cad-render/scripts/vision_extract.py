#!/usr/bin/env python3
"""
vision_extract.py — Reads a set of furniture CAD images (front view, side view,
dimension-annotated page, and any component/part drawings from the CAD PDF) and
extracts a single structured description of the piece: overall dimensions,
component list, joints, and any material/color notes visible on the drawings.

Requires: DASHSCOPE_API_KEY environment variable.
Requires: pip install dashscope
"""

import os
import sys
import json
import argparse
from dashscope import MultiModalConversation

MODEL = "qwen3-vl-plus"  # vision-language model for structural understanding

EXTRACTION_PROMPT = """You are reading a furniture CAD drawing set. The images may include a front
view, side view, a dimension-annotated page, and individual component/part
(零件) drawings extracted from a CAD PDF.

Study all images together and return ONLY a JSON object (no prose, no markdown
fences) with this exact shape:

{
  "piece_type": "e.g. dining chair / bookshelf / coffee table",
  "overall_dimensions_mm": {"width": <number or null>, "depth": <number or null>, "height": <number or null>},
  "components": [
    {"name": "e.g. leg, seat, drawer front", "count": <int>, "dimensions_mm": "as noted, or null", "notes": "joint/attachment info if visible"}
  ],
  "material_or_color_notes": "anything visible on the drawing about material/finish, or null if none",
  "missing_or_unclear": ["list anything you could not determine confidently, e.g. 'no dimension page provided', 'side view dimensions not legible'"]
}

Be precise about numbers — do not guess a dimension that is not actually
legible; put it in "missing_or_unclear" instead. This extraction is the only
source of truth the next generation step will use, so do not silently invent
structure that isn't in the drawings."""


def extract_structure(image_paths, api_key=None):
    """Call Qwen-VL on the full CAD image set and return the parsed structure dict."""
    api_key = api_key or os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("Set DASHSCOPE_API_KEY (Capafy execution environment should inject this).")

    content = [{"text": EXTRACTION_PROMPT}]
    for p in image_paths:
        content.append({"image": p})

    messages = [{"role": "user", "content": content}]

    response = MultiModalConversation.call(
        api_key=api_key,
        model=MODEL,
        messages=messages,
    )

    if response.status_code != 200:
        raise RuntimeError(f"Qwen-VL call failed: {response.code} - {response.message}")

    raw_text = response.output.choices[0].message.content
    # content can come back as a list of content blocks; normalize to text
    if isinstance(raw_text, list):
        raw_text = "".join(block.get("text", "") for block in raw_text if isinstance(block, dict))

    raw_text = raw_text.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        raw_text = raw_text.split("\n", 1)[1] if "\n" in raw_text else raw_text

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Vision model did not return valid JSON: {e}\nRaw output: {raw_text}")


def main():
    parser = argparse.ArgumentParser(description="Extract furniture structure from CAD images")
    parser.add_argument("images", nargs="+", help="Paths or URLs to CAD view/component images")
    parser.add_argument("--out", help="Write JSON result to this path instead of stdout")
    args = parser.parse_args()

    structure = extract_structure(args.images)
    output = json.dumps(structure, indent=2, ensure_ascii=False)

    if args.out:
        with open(args.out, "w") as f:
            f.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main()
