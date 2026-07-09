#!/usr/bin/env python3
"""
generate_images.py — Construction Concern Monthly Image Generator
Arc & Anthem

Reads image prompts from a _gemini_ready.md file and generates images
using the OpenAI Images API. Saves each image to the output folder with
a branded Construction Concern bar added at the bottom.

Usage:
    python3 generate_images.py

Requirements:
    - OPENAI_API_KEY set as an environment variable (see SETUP.md)
    - pip3 install openai pillow

Output:
    Images saved to: 08_image_prompts/monthly/output/[YYYY-MM]/
"""

import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime

try:
    from openai import OpenAI
except ImportError:
    print("ERROR: openai package not installed. Run: pip3 install openai")
    sys.exit(1)

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("ERROR: Pillow not installed. Run: pip3 install pillow")
    sys.exit(1)

# ── Configuration ─────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).resolve().parents[2]  # construction-concern/
PROMPTS_DIR = BASE_DIR / "08_image_prompts" / "monthly"
OUTPUT_BASE  = PROMPTS_DIR / "output"

# ── Helpers ───────────────────────────────────────────────────────────────────

def get_api_key():
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        print("\nOPENAI_API_KEY environment variable is not set.")
        print("To set it, open Terminal and run:")
        print('  export OPENAI_API_KEY="your-key-here"')
        print("Then run this script again.\n")
        sys.exit(1)
    return key


def find_prompt_file(year_month: str) -> Path:
    """Find the gemini_ready file for a given YYYY-MM string."""
    pattern = f"{year_month}_image_prompts_gemini_ready.md"
    path = PROMPTS_DIR / pattern
    if path.exists():
        return path
    # Try to find any matching file
    matches = list(PROMPTS_DIR.glob(f"{year_month}*gemini_ready*.md"))
    if matches:
        return matches[0]
    raise FileNotFoundError(
        f"No gemini_ready prompt file found for {year_month} in {PROMPTS_DIR}"
    )


def parse_prompts(md_path: Path) -> list[dict]:
    """
    Parse post numbers and image prompts from the gemini_ready markdown file.
    Returns list of dicts: {post_num, topic, prompt, is_real_photo}
    """
    text = md_path.read_text(encoding="utf-8")
    posts = []

    # Split on "### Post #N" headers
    sections = re.split(r"(?=###\s+Post\s+#\d+)", text)

    for section in sections:
        post_match = re.match(r"###\s+Post\s+#(\d+)", section)
        if not post_match:
            continue

        post_num = int(post_match.group(1))

        # Extract topic
        topic_match = re.search(r"\*\*Post Topic:\*\*\s*(.+)", section)
        topic = topic_match.group(1).strip() if topic_match else f"Post {post_num}"

        # Check if this is a real photo post
        is_real_photo = bool(re.search(r"\*\*USE REAL PHOTO", section, re.IGNORECASE))

        # Extract prompt — prefer "AI Prompt" if present, else "Image Prompt"
        ai_prompt_match = re.search(
            r"\*\*AI Prompt.*?:\*\*\s*(.+?)(?=\n\n---|\n###|\Z)", section, re.DOTALL
        )
        image_prompt_match = re.search(
            r"\*\*Image Prompt:\*\*\s*(.+?)(?=\n\n---|\n###|\Z)", section, re.DOTALL
        )

        if ai_prompt_match:
            prompt_text = ai_prompt_match.group(1).strip()
        elif image_prompt_match:
            prompt_text = image_prompt_match.group(1).strip()
        else:
            prompt_text = None

        posts.append({
            "post_num": post_num,
            "topic": topic,
            "prompt": prompt_text,
            "is_real_photo": is_real_photo,
        })

    return sorted(posts, key=lambda x: x["post_num"])


def add_brand_bar(image_path: Path):
    """
    Add a thin Construction Concern branding bar to the bottom of a generated image.
    Bar: warm sand #D4C5A9, ~4.5% of image height, caption-sized dark text.
    """
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size

    bar_height = max(36, int(height * 0.045))
    bar_color = (212, 197, 169, 255)   # #D4C5A9 warm sand
    text_color = (61, 53, 48, 255)     # #3d3530 dark charcoal

    draw = ImageDraw.Draw(img)

    # Draw bar
    bar_y = height - bar_height
    draw.rectangle([(0, bar_y), (width, height)], fill=bar_color)

    # Load font — try system fonts, fall back to default
    font = None
    font_size = max(14, bar_height - 14)
    font_candidates = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for fp in font_candidates:
        if Path(fp).exists():
            try:
                font = ImageFont.truetype(fp, font_size)
                break
            except Exception:
                pass
    if font is None:
        font = ImageFont.load_default()

    text = "Construction Concern"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    text_x = (width - text_w) // 2
    text_y = bar_y + (bar_height - text_h) // 2

    draw.text((text_x, text_y), text, fill=text_color, font=font)

    # Save as RGB PNG
    img.convert("RGB").save(image_path, "PNG")


def generate_image(client: OpenAI, prompt: str, post_num: int, output_dir: Path) -> Path:
    """Call the OpenAI Images API and save the result."""
    print(f"  Generating image via API...")

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024",  # Square 1:1
        quality="medium",  # Options: low, medium, high, auto
        n=1,
    )

    import base64
    filename = output_dir / f"post_{post_num:02d}.png"
    image_data = base64.b64decode(response.data[0].b64_json)
    filename.write_bytes(image_data)

    # Add brand bar via post-processing (more reliable than asking AI to render it)
    add_brand_bar(filename)

    return filename


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("\n── Construction Concern Image Generator ──────────────────────────")

    # Get API key
    api_key = get_api_key()
    client = OpenAI(api_key=api_key)

    # Ask for month
    default_month = datetime.now().strftime("%Y-%m")
    month_input = input(f"\nEnter month to generate (YYYY-MM) [{default_month}]: ").strip()
    year_month = month_input if month_input else default_month

    # Find prompt file
    try:
        prompt_file = find_prompt_file(year_month)
        print(f"Found prompt file: {prompt_file.name}")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    # Parse prompts
    posts = parse_prompts(prompt_file)
    print(f"Found {len(posts)} posts in file.\n")

    # Filter options
    print("Options:")
    print("  A = Generate ALL AI posts (skip real photo posts)")
    print("  S = Select specific post numbers")
    choice = input("Choice [A/S]: ").strip().upper()

    if choice == "S":
        nums_input = input("Enter post numbers separated by commas (e.g. 1,3,7): ")
        selected = [int(x.strip()) for x in nums_input.split(",") if x.strip().isdigit()]
        posts_to_run = [p for p in posts if p["post_num"] in selected]
    else:
        posts_to_run = [p for p in posts if not p["is_real_photo"] and p["prompt"]]

    if not posts_to_run:
        print("No posts selected or no valid prompts found. Exiting.")
        sys.exit(0)

    # Set up output directory
    output_dir = OUTPUT_BASE / year_month
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"\nOutput folder: {output_dir}")

    # Cost estimate
    cost_estimate = len(posts_to_run) * 0.04
    print(f"\nPosts to generate: {len(posts_to_run)}")
    print(f"Estimated cost: ~${cost_estimate:.2f} USD (standard quality, 1024x1024)")
    confirm = input("\nProceed? [y/N]: ").strip().lower()
    if confirm != "y":
        print("Cancelled.")
        sys.exit(0)

    print()

    # Generate
    success = []
    failed = []

    for post in posts_to_run:
        num = post["post_num"]
        topic = post["topic"]

        # Skip real photo posts unless explicitly selected
        if post["is_real_photo"] and not post["prompt"]:
            print(f"Post #{num:02d} [{topic}] — USE REAL PHOTO, skipping.")
            continue

        print(f"Post #{num:02d} [{topic}]")

        try:
            saved_path = generate_image(client, post["prompt"], num, output_dir)
            print(f"  ✅ Saved: {saved_path.name}\n")
            success.append(num)
        except Exception as e:
            print(f"  ❌ Failed: {e}\n")
            failed.append(num)

        # Respect rate limits — pause between requests
        if post != posts_to_run[-1]:
            time.sleep(2)

    # Summary
    print("── Summary ───────────────────────────────────────────────────────")
    print(f"✅ Generated: {len(success)} images → {output_dir}")
    if failed:
        print(f"❌ Failed:    {len(failed)} posts — {failed}")
    print(f"\nOpen folder: open \"{output_dir}\"")
    print()


if __name__ == "__main__":
    main()
