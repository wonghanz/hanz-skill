#!/usr/bin/env python3
"""
consistency_check.py — Compares a generated render against the original CAD
structure and classifies any mismatch as hard-fail (must retry) or soft
(acceptable, ship as-is).

Hard-fail criteria (per design spec):
  - overall dimensions/proportions off by more than ~10%
  - wrong component count (missing/extra leg, drawer, shelf, etc.)
  - wrong overall silhouette

Soft, does not trigger retry:
  - texture/shading/lighting/background variance
  - minor non-structural styling differences

Requires: DASHSCOPE_API_KEY environment variable.
Requires: pip install dashscope
"""

import os
import json
import argparse
from dashscope import MultiModalConversation

MODEL = "qwen3-vl-plus"

CHECK_PROMPT_TEMPLATE = """You are a QA reviewer comparing a generated furniture render against the
original CAD structure it was supposed to match.

Original structure (ground truth, extracted from the CAD drawings):
{structure_json}

Look at the attached generated render image and judge whether it matches
this structure. Return ONLY a JSON object (no prose, no markdown fences):

{{
  "pass": <true|false>,
  "hard_fail_issues": [
    {{"issue": "short description", "detail": "what's wrong and roughly by how much, e.g. 'height looks ~20% shorter than the stated 900mm'"}}
  ],
  "soft_issues": [
    {{"issue": "short description"}}
  ]
}}

Mark "pass": false ONLY if there is at least one hard_fail_issue, using these
criteria:
  - overall dimensions/proportions appear off by more than roughly 10%
  - a component is missing or an extra one was added compared to the structure's component list
  - the overall silhouette/shape doesn't match the described piece

Texture, lighting, background, and minor stylistic rendering choices are
soft issues only — do not fail the render for those."""


def check_consistency(structure, generated_image_url, api_key=None):
    api_key = api_key or os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("Set DASHSCOPE_API_KEY (Capafy execution environment should inject this).")

    prompt = CHECK_PROMPT_TEMPLATE.format(structure_json=json.dumps(structure, ensure_ascii=False))
    content = [{"text": prompt}, {"image": generated_image_url}]
    messages = [{"role": "user", "content": content}]

    response = MultiModalConversation.call(
        api_key=api_key,
        model=MODEL,
        messages=messages,
    )

    if response.status_code != 200:
        raise RuntimeError(f"Qwen-VL call failed: {response.code} - {response.message}")

    raw_text = response.output.choices[0].message.content
    if isinstance(raw_text, list):
        raw_text = "".join(block.get("text", "") for block in raw_text if isinstance(block, dict))
    raw_text = raw_text.strip()
    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        raw_text = raw_text.split("\n", 1)[1] if "\n" in raw_text else raw_text

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"Consistency checker did not return valid JSON: {e}\nRaw output: {raw_text}")


def main():
    parser = argparse.ArgumentParser(description="Check a generated render against the CAD structure")
    parser.add_argument("--structure", required=True, help="Path to structure JSON from vision_extract.py")
    parser.add_argument("--image", required=True, help="URL or path of the generated render to check")
    args = parser.parse_args()

    with open(args.structure) as f:
        structure = json.load(f)

    result = check_consistency(structure, args.image)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
