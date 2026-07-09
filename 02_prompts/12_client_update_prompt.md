# Client Update Prompt — Monthly HTML Email

You are preparing a monthly client progress email for Construction Concern on behalf of Arc & Anthem.

## Purpose

Translate the monthly analytics review into a polished, client-facing HTML email that:
- Leads with what is working and what is going well
- Is honest but not alarming about areas still building
- Clearly states what is coming next month
- Asks the client to take specific actions that support growth
- Reads as a warm, professional follow-up — not a formal report

This email is sent by Karen M. Blackwell, CEO of Arc & Anthem, directly to the client.

---

## Inputs

Add to context before running this prompt:
- `01_config/client_profile.md`
- The completed analytics review from `08_analytics_review_prompt.md` for the current month
- Any notable wins, milestones, or concerns from the current month's content run
- The client's name (for the greeting)
- Whether this follows a recent call or meeting (adjust opening accordingly)

---

## Tone and Voice

- Warm, direct, and partnership-oriented — written as one professional to another
- Lead with momentum and genuine wins — not disclaimers
- Be honest about what is not working yet — do not hide it, but frame it as "still building" not "failing"
- The client should feel informed, confident, and clear on what to do next
- Avoid agency jargon, technical platform language, and overly formal report structure
- Write as Karen — first-person singular where natural, "we" for Arc & Anthem as a team

---

## Structure (follow this order exactly)

### 1. Greeting
- Address the client by first name
- Reference the most recent call or touchpoint if applicable
- One short paragraph: what this email is, and lead with the positive framing

### 2. What Is Working (always first — minimum 3 items)
Use actual data from the analytics review. Highlight:
- Newsletter open rates (compare to industry average of 20–25% for home services)
- Any content piece or post that outperformed
- Website engagement signals (time on site, returning visitors)
- Content quality and brand consistency
- Preparedness for the coming month (if content is ready, say so)

### 3. Where We Are Still Building (honest, not alarming)
Cover only what is genuinely behind or flat. For each item:
- State the current reality plainly
- Explain why it happens (context, not excuses)
- State what is being done to address it

### 4. What Is Coming Next Month
Bullet list. Specific and concrete — post counts, newsletter dates, blog titles if available.

### 5. Three Things We Need From You
Always include these three asks (adjust wording to fit the month):
1. **Job site photos and videos** — before/after shots, short clips, any phone photos from completed jobs. Request 3–5 photos per job going forward.
2. **Ask clients to follow on social media** — after job completion, direct ask. Include platform handles.
3. **Ask happy clients to leave a Google review** — at the moment of gratitude, direct ask with a text + link.

Frame these as the fastest levers available — because they are.

### 6. At-a-Glance Summary Table
One row per key area. Use three status levels:
- ✅ Strong / Ready
- 🟡 Steady / Building
- ⏳ Action needed from client

### 7. Closing
One short paragraph. Reinforce the partnership, reference the upcoming month as a turning point if true, and invite questions.

### 8. Signature
Always:
```
Karen M. Blackwell
CEO, Arc & Anthem
karen@arcandanthem.com
```

---

## HTML Output Requirements

Generate a complete, self-contained HTML file using inline styles only (no external CSS, no `<style>` blocks — Outlook strips them). The email must be copy-paste ready into Outlook.

### Design specifications:
- Max width: 620px, centered
- Body background: `#f5f2ed`
- Email container background: `#ffffff`
- Header background: `#D4C5A9` (warm sand)
- Section label font: Arial, 11–13px, uppercase, color `#5a4f3f`
- Body font: Georgia or serif, 15px, color `#2c2520`, line-height 1.7
- Dividers: 1px solid `#e0d8cc`
- Callout/card background: `#f9f7f3` with 4px left border `#D4C5A9`
- Footer background: `#f0ebe2`, Arial 11px, color `#8a7f72`
- Table layout (not div/flexbox) for Outlook compatibility
- All colors as hex codes — no rgb() or named colors
- No external images, no web fonts

### Summary table colors:
- ✅ rows: text color `#3a6b35`
- 🟡 rows: text color `#7a6020`
- ⏳ rows: text color `#8a4020`
- Alternating row backgrounds: `#f9f7f3` and `#ffffff`
- Header row background: `#D4C5A9`

---

## Output File

Save the completed HTML file to:
```
09_exports/[YYYY-MM]_client_email_[client-last-name].html
```

Example: `09_exports/2026-05_client_email_richard_herron.html`

Also update or create a plain-text markdown summary version at:
```
09_exports/[YYYY-MM]_client_progress_report.md
```

---

## Rules

1. Always lead with wins — never open with problems.
2. Always cite real numbers from the analytics review — no vague summaries.
3. Newsletter open rates must be compared to the 20–25% home services industry benchmark.
4. The three client asks (photos, follows, reviews) must always appear — every month.
5. Do not include internal agency notes, platform research citations, or strategic rationale in the client email. Those belong in the internal dashboard.
6. The HTML must use table-based layout only — no divs, no flexbox, no CSS grid.
7. Test all hex colors are valid 6-digit codes before outputting.
8. The email must be completable in under 3 minutes of reading.
9. Do not include pricing, contracts, billing, or scope discussions in this email.
10. If a metric is missing or unavailable, acknowledge it briefly and move on — do not leave a blank field.

---

## How This Fits the Workflow

Run this prompt AFTER:
- Step 8: Analytics review is complete (`08_analytics_review_prompt.md`)
- All monthly content has been finalized and scheduled

Run this prompt BEFORE:
- Sending the client any formal communication about the month's results

This prompt produces the only client-facing deliverable in the monthly workflow.

---

## Reference Example

The May 2026 client email to Richard Herron at:
`09_exports/2026-05_client_email_richard_herron.html`

Use this as the visual and structural reference for all future months.
