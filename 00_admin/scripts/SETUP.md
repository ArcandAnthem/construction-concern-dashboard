# Image Generator — Setup & Usage
**File:** `00_admin/scripts/generate_images.py`

---

## One-Time Setup

### Step 1 — Add your API key to your Mac

This stores your key securely in your Mac's shell profile so you never have to paste it into a file.

1. Open **Terminal** (search Terminal in Spotlight)
2. Run this command — replace the key with your actual one from platform.openai.com:

```bash
echo 'export OPENAI_API_KEY="sk-your-actual-key-here"' >> ~/.zprofile
source ~/.zprofile
```

3. Verify it worked:
```bash
echo $OPENAI_API_KEY
```
You should see your key printed. If you see nothing, restart Terminal and try again.

> **Security note:** This stores the key in your Mac's profile file only — not in any project file or GitHub. Never paste your API key into a chat, document, or code file.

---

### Step 2 — Confirm Python and OpenAI are ready

In Terminal, run:
```bash
python3 --version
python3 -c "import openai; print('OpenAI ready:', openai.__version__)"
```

Both should return version numbers without errors. If openai is missing:
```bash
pip3 install openai
```

---

## Running the Script Each Month

### From Terminal:
```bash
cd "/Users/karenblackwell/Documents/ArcAnthem-Content-Ops/construction-concern/00_admin/scripts"
python3 generate_images.py
```

### What happens:
1. Script asks which month to generate (defaults to current month)
2. Finds the `[YYYY-MM]_image_prompts_gemini_ready.md` file automatically
3. Parses all 14 post prompts
4. Shows you the options: generate all AI posts, or select specific ones
5. Shows estimated cost before spending anything
6. Generates images one at a time, saves them as PNG files
7. Output saved to: `08_image_prompts/monthly/output/[YYYY-MM]/`

### File naming:
- `post_01.png` → Post #1
- `post_02.png` → Post #2
- etc.

---

## What Gets Skipped Automatically

Posts marked **USE REAL PHOTO** are skipped — the script recognizes that flag and does not attempt to generate those. For Posts 5, 8, 11, and 14, pull the real photos from `Photos_Before and After/` manually.

---

## Cost Reference

| Quality setting | Cost per image | 14 posts total |
|---|---|---|
| low | ~$0.01 | ~$0.14 |
| medium (default) | ~$0.04 | ~$0.56 |
| high | ~$0.08 | ~$1.12 |

To change quality, open `generate_images.py` and change:
```python
quality="medium",
```
to `"low"`, `"high"`, or `"auto"`.

---

## Regenerating a Single Post

If one image doesn't look right, run the script again and choose **S** (select specific posts), then enter just that post number. It will overwrite the existing file.

---

## Troubleshooting

**"OPENAI_API_KEY environment variable is not set"**
→ Run `source ~/.zprofile` in Terminal, then try again.

**"Billing hard limit reached" or 429 error**
→ Your API account may have hit a spend limit. Log into platform.openai.com → Billing → increase the monthly limit.

**Image looks wrong / doesn't match the prompt**
→ DALL-E 3 sometimes interprets prompts loosely. Regenerate the specific post (option S). You can also open `generate_images.py` and edit the prompt for that post before regenerating.

**"No gemini_ready prompt file found"**
→ Make sure the file exists at `08_image_prompts/monthly/[YYYY-MM]_image_prompts_gemini_ready.md` with the correct month format.

---

## Adding to the Monthly Workflow

This script runs between **Step 14 (Gemini-ready file complete)** and **Step 15 (Client email)** in the monthly checklist.

After generating:
1. Open the output folder: `08_image_prompts/monthly/output/[YYYY-MM]/`
2. Review each image
3. Swap any that need regeneration
4. Use the approved images when scheduling in Later
