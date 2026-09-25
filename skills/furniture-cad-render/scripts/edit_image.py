#!/usr/bin/env python3
"""
edit_image.py — Fixes a specific mismatch on an already-generated render using
Qwen-Image-Edit, instead of regenerating the whole image from scratch. This
preserves everything that already matched and only touches what's wrong —
a full regenerate risks fixing one thing while breaking another that was
already correct.

Requires: DASHSCOPE_API_KEY environment variable.
Requires: pip install dashscope
"""

import os
import json
import argparse
from dashscope import MultiModalConversation

MODEL = "qwen-image-edit-plus"


def build_edit_instruction(hard_fail_issues):
    """Turn the consistency checker's hard_fail_issues into one edit instruction."""
    parts = [f"{issue['issue']}: {issue.get('detail', '')}" for issue in hard_fail_issues]
    return (
        "Fix ONLY the following issues in this furniture render, without changing "
        "anything else about the piece (keep the same style, material, lighting, "
        "and camera angle): " + "; ".join(parts)
    )


def edit_render(image_url, hard_fail_issues, api_key=None):
    api_key = api_key or os.environ.get("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError("Set DASHSCOPE_API_KEY (Capafy execution environment should inject this).")

    instruction = build_edit_instruction(hard_fail_issues)
    content = [{"image": image_url}, {"text": instruction}]
    messages = [{"role": "user", "content": content}]

    response = MultiModalConversation.call(
        api_key=api_key,
        model=MODEL,
        messages=messages,
        n=1,
        watermark=False,
    )

    if response.status_code != 200:
        raise RuntimeError(f"Qwen-Image-Edit call failed: {response.code} - {response.message}")

    new_image_url = response.output.choices[0].message.content[0]["image"]
    return {"image_url": new_image_url, "instruction_used": instruction}


def main():
    parser = argparse.ArgumentParser(description="Fix a specific mismatch on a generated render")
    parser.add_argument("--image", required=True, help="URL of the render to fix")
    parser.add_argument("--issues", required=True, help="Path to JSON file with hard_fail_issues list")
    args = parser.parse_args()

    with open(args.issues) as f:
        issues = json.load(f)

    result = edit_render(args.image, issues)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
