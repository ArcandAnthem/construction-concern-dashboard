# Wix Blog Template — Construction Concern
**Reusable Monthly Template | Arc & Anthem**

## Recommended Publish Schedule

| Blog Post | Day | Time | Notes |
|---|---|---|---|
| Post #1 | **Tuesday** | **9:00am PST** | Publish first — referenced in Newsletter #1 |
| Post #2 | **Tuesday** | **9:00am PST** | Same week as Newsletter #2, 2 weeks later |
| Post #3 | **Wednesday** | **9:00am PST** | Mid-month for SEO consistency |
| Post #4 | **Wednesday** | **9:00am PST** | End of month |

**Why Tuesday/Wednesday at 9am:** Google indexes new content faster on weekday mornings. Tuesday captures the peak of home improvement research intent (post-weekend planning). Publishing before 10am means your post can rank before peak search hours.

---

## Before You Start — Image Prompts

Generate **two images per blog post** before uploading to Wix:
1. **Featured cover image** — shown in blog list, homepage, and social share previews
2. **In-body image** — placed within the article to break up text and reinforce the topic

Use ChatGPT (GPT-4o image generation) or the API script to generate both before opening Wix.

---

### Featured Cover Image
**Wix field:** "Add media" in the blog editor — set as the post's Cover Image
**Required dimensions: 1200px wide × 628px tall (16:9 ratio)**

> ⚠️ This is the most important image. It shows in the blog post list on your website, in Google search results, in social share previews (Facebook, LinkedIn), and on any blog widget. Always generate this at 1200×628.

#### Cover Image Prompt Template
```
Create a photorealistic [scene description] for a home improvement blog post cover image.
Output size: 1200 pixels wide by 628 pixels tall, 16:9 landscape ratio.
[Scene details — what type of home, exterior or interior, what feature is shown.]
No people. No text, logos, watermarks, or overlays of any kind.
Shot on DSLR camera at a real-world location. No CGI or 3D rendering.
No warm color cast, no golden-hour filter, no artificial color grading.
Neutral, true-to-life daylight exposure.
Style: professional real-estate photography.
```

#### Scene options by topic:
| Topic | Scene description |
|---|---|
| Windows | Exterior of SoCal home with traditional double-hung windows, bright afternoon, stucco and tile roof |
| HVAC | Side yard of SoCal home with condenser unit on concrete pad, tidy landscaping, clear sky |
| Siding / Fire season | Exterior of well-maintained SoCal home with enclosed soffits, stucco, tile roof, clear blue sky |
| Bundled projects | Freshly renovated SoCal home — new siding and windows, curb appeal, afternoon light |
| Contractor tips | Interior: homeowner at kitchen table reviewing paperwork, tile counters, everyday finishes |
| Solar | Rooftop solar install on SoCal home, clear sky, suburban neighborhood |

---

### In-Body Image
**Wix field:** Insert image block within the blog post content — place after the second or third section
**Required dimensions: 800px wide × 500px tall (8:5 ratio)**

> The in-body image reinforces the article's main point with a close-up detail. It breaks up long text and improves time-on-page. Use a detail shot (close-up) rather than a wide exterior shot — the cover image already handles the establishing view.

#### In-Body Image Prompt Template
```
Create a photorealistic close-up detail photograph for a home improvement blog article.
Output size: 800 pixels wide by 500 pixels tall, 8:5 landscape ratio.
[Close-up scene description — what specific detail, material, or element is shown.]
No people. No text, logos, watermarks, or overlays of any kind.
Shot on DSLR camera. No CGI or 3D rendering.
No warm color cast, neutral natural light, true-to-life exposure.
Style: editorial, real-estate quality detail shot.
```

#### Detail shot options by topic:
| Topic | Detail to show |
|---|---|
| Windows | Close-up of window frame meeting wall — seal, weatherstripping, or glass edge |
| HVAC | HVAC air filter being held up, or vent grille on interior wall |
| Siding / Fire season | Close-up of enclosed soffit underside or fiber cement siding texture |
| Bundled projects | Joint where window frame meets new siding — clean caulk line, flashing visible |
| Contractor tips | Close-up of printed contract or estimate on a table with a pen |
| Solar | Close-up of solar panel edge on a roof, clear sky in background |

---

## Wix Blog Editor — Step-by-Step

### Before publishing:
1. Generate cover image (1200×628) and in-body image (800×500) using prompts above
2. Write or paste the final blog text from the `07_blog/final/` file
3. Open Wix Blog editor and create a new post

### In the editor:

**Step 1 — Set post metadata**
- **Post title:** Paste from the final file's "Post Title" field
- **SEO title:** Paste from "SEO Title" field (Settings → SEO)
- **Meta description:** Paste from "Meta Description" field
- **URL slug:** Paste from "URL Slug" field — do not auto-generate
- **Category:** Select the relevant service category (Windows, Siding, HVAC, etc.)

**Step 2 — Upload cover image**
- In the post editor, click the cover image placeholder at the top
- Upload `blog_[N]_cover.png` (1200×628)
- Add alt text from the "Cover Image Alt Text" field in the final file

**Step 3 — Paste body content**
- Paste the full blog text from the final file
- Keep the heading levels (H2 for main sections, H3 for sub-sections)
- Font: Wix default blog font — do not override

**Step 4 — Insert in-body image**
- Place cursor after the second or third section
- Insert > Image
- Upload `blog_[N]_body.png` (800×500)
- Add a brief caption if relevant (optional — not required on every post)

**Step 5 — Set internal link**
- At the bottom CTA, make "constructionconcern.com/free-estimate" a live hyperlink

**Step 6 — Preview and publish**
- Preview on mobile — confirm the cover image crops cleanly on phones
- Confirm meta description shows in SEO preview
- Publish at the scheduled time (see schedule table at top of this file)

---

## Image Alt Text Rules for SEO

Always write alt text that:
- Describes what is literally in the image
- Naturally includes the post's target SEO keyword where it fits
- Is 10–15 words max
- Does not say "image of" or "photo of" — just describe the scene

**Examples:**
- ✅ `Energy efficient windows installed on a stucco home in Santa Clarita, California`
- ✅ `Residential HVAC unit on concrete pad, Southern California side yard`
- ❌ `Image showing a house with windows`
- ❌ `Window photo`

---

## Monthly Fill-In Reference

Each month, fill in the following before generating images:

```
Month: ___________
Blog Post #: ___
Post Title: ___________
Target keyword: ___________
Cover image topic/scene: ___________
Body image detail/scene: ___________
Cover image filename: blog_[N]_cover.png
Body image filename: blog_[N]_body.png
Publish date: ___________  at 9:00am PST
```
