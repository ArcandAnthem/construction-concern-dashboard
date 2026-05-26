# Monthly Run Checklist — Construction Concern

Use this checklist at the start of each new month so the workflow stays fast, repeatable, and low-friction.

---

## Preferred method: Run the monthly agent

For a fully autonomous run, use the master agent prompt instead of stepping through this checklist manually:

**File:** `00_admin/monthly_agent_prompt.md`

**How to start:**
1. Open a new Copilot chat
2. Paste the full contents of `monthly_agent_prompt.md`
3. Tell the agent the month and year (e.g., "Run June 2026")
4. Attach or paste any analytics exports from Later.com and Wix

The agent will execute all 15 phases and produce every file without step-by-step direction.

**Human input still required (at any point in the run):**
- Analytics CSV exports from Later.com + Wix (provide at the start)
- Real project photos from the client (share when available)
- Newsletter send approval before publishing
- Blog approval before posting to Wix
- Any service or promotion changes since last month

---

## Manual checklist (use if running step-by-step)

## 0) Analytics review (run this first — before anything else)

Before duplicating files or generating new content, review last month's actual performance data.

Add to context:
- `01_config/client_profile.md`
- `02_prompts/08_analytics_review_prompt.md`
- any CSV exports from Later.com, Wix, LinkedIn, Facebook, or Instagram for the prior month
- the prior month's `[YYYY-MM]_internal_dashboard.md`

Run the analytics review prompt and save the output as notes to carry into this month's research and strategy steps.

### Checklist
- [ ] Export platform data from Later.com (Instagram + Facebook post performance)
- [ ] Export traffic data from Wix (last 30 days)
- [ ] Screenshot or export any LinkedIn and Threads performance available
- [ ] Save Instagram follower count before and after the prior month
- [ ] Run the analytics review prompt
- [ ] Note the top-performing content format and topic
- [ ] Note the lowest-performing content format and topic
- [ ] Carry forward 3–5 recommendations into Step 3 (research summary)

---

## 1) Create the new month from last month

Duplicate the prior month’s files and rename them for the new month.

Example:
- `2026-05_research_summary.md` → `2026-06_research_summary.md`
- `2026-05_internal_dashboard.md` → `2026-06_internal_dashboard.md`
- `2026-05_client_dashboard.md` → `2026-06_client_dashboard.md`
- `2026-05_social_strategy.md` → `2026-06_social_strategy.md`
- `2026-05_social_calendar.csv` → `2026-06_social_calendar.csv`
- `2026-05_social_final_posting.md` → `2026-06_social_final_posting.md`
- `2026-05_newsletter_draft.md` → `2026-06_newsletter_draft.md`
- `2026-05_newsletter_final.md` → `2026-06_newsletter_final.md`
- `2026-05_blog_draft.md` → `2026-06_blog_draft.md`
- `2026-05_blog_final.md` → `2026-06_blog_final.md`
- `2026-05_image_prompts.md` → `2026-06_image_prompts.md`
- `2026-05_image_prompts_gemini_ready.md` → `2026-06_image_prompts_gemini_ready.md`

After duplicating, update the month and year inside each file title.

---

## 2) Pre-flight check

Before generating anything new, confirm these are still current:

- `01_config/client_profile.md`
- `02_prompts/01_monthly_research_prompt.md`
- `02_prompts/03_social_prompt.md`
- `02_prompts/04_newsletter_prompt.md`
- `02_prompts/05_blog_prompt.md`
- `02_prompts/06_revision_prompt.md`
- `02_prompts/07_image_prompt_prompt.md`

If any of these changed last month, update them first before running the new month.

---

## 3) Update the monthly research summary first

Open:
- `03_research/monthly_logs/[YYYY-MM]_research_summary.md`

Add to Copilot context:
- `01_config/client_profile.md`
- `02_prompts/01_monthly_research_prompt.md`
- the new monthly research file

Run a monthly research refresh using the current month.

### Checklist
- [ ] Remove last month’s old content
- [ ] Generate the new month’s research summary
- [ ] Make sure the file includes:
  - Executive Summary
  - What the Monthly Research Shows
  - What Was Reviewed
  - Competitor and Market Signals
  - Seasonal and Local Context
  - Strategic Implications
  - Recommended Focus Areas
  - Channel Implications
  - Source Notes
  - References
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 4) Build the internal dashboard

Open:
- `04_dashboards/internal/[YYYY-MM]_internal_dashboard.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the new monthly research summary
- `04_dashboards/internal/research_dashboard_template.md`
- the new internal dashboard file

### Checklist
- [ ] Generate the internal dashboard from the research summary
- [ ] Remove placeholder/setup text if still present
- [ ] Confirm the dashboard includes:
  - Executive Summary
  - What the Monthly Research Shows
  - What Was Reviewed
  - Competitor and Market Signals
  - Seasonal and Local Context
  - Strategic Recommendations for the Month
  - Channel Implications
  - What Content the Client Will See
  - Source Notes
  - References
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 5) Build the client dashboard

Open:
- `04_dashboards/client/[YYYY-MM]_client_dashboard.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the new monthly research summary
- the new internal dashboard
- `04_dashboards/client/client_dashboard_template.md`
- the new client dashboard file

### Checklist
- [ ] Generate the client dashboard
- [ ] Keep it polished, concise, and client-friendly
- [ ] Make sure it includes:
  - Overview
  - What the Monthly Research Shows
  - What Was Reviewed
  - Our Strategy for the Month
  - What Content You Will See
  - Recommended Next Actions
- [ ] Remove any technical clutter or internal-only language
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 6) Build the social strategy

Open:
- `05_social/strategy/[YYYY-MM]_social_strategy.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the new monthly research summary
- the new internal dashboard
- the new client dashboard
- `02_prompts/03_social_prompt.md`
- the new social strategy file

### Checklist
- [ ] Generate the full monthly social strategy
- [ ] Confirm it starts with:
  - Posting strategy for the month
  - Research guiding the posting strategy
- [ ] Confirm it includes all planned posts using this structure:

#### Post structure
- Recommended Day to Post
- Recommended Time of Day to Post
- Post Platform
- Platform Strategy
- Content Pillar
- Caption with hashtags
- Image prompt

- [ ] Confirm the approved platforms only:
  - LinkedIn
  - Facebook
  - Instagram
  - Threads
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 7) Build the final social posting file

Add to Copilot context:
- `01_config/client_profile.md`
- the new monthly research summary
- the new social strategy
- the new final posting file

### Checklist
- [ ] Generate the clean final posting file
- [ ] Confirm each post uses only this structure:

#### Final posting structure
- Post #
- Platform
- Caption with hashtags

- [ ] No separate CTA field
- [ ] No separate hashtags field
- [ ] No strategy notes
- [ ] Final captions are easy to copy and paste
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 8) Build the audience growth and engagement plan

Open:
- `02_prompts/11_audience_growth_prompt.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the analytics review findings from Step 0
- the new monthly social strategy

### Checklist
- [ ] Run the audience growth prompt
- [ ] Confirm the monthly engagement plan includes:
  - Weekly comment engagement targets (Instagram + Facebook)
  - Follow targets for the month
  - Facebook group participation guidance
  - 2 interactive Story concepts
  - Updated hashtag set (local / service / audience)
  - Response protocol reminder
- [ ] Save the engagement plan (can be added as an appendix to the social strategy file)
- [ ] Schedule 15 minutes per day in the client's calendar for engagement activities

---

## 9) Build the newsletter draft

Open:
- `06_newsletter/drafts/[YYYY-MM]_newsletter_draft.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the new monthly research summary
- the new internal dashboard
- the new client dashboard
- `02_prompts/04_newsletter_prompt.md`
- the new newsletter draft file

### Checklist
- [ ] Generate 2 newsletters
- [ ] Make sure the tone is warm, credible, grounded, and homeowner-first
- [ ] Remove unsupported claims or overly specific numbers unless verified
- [ ] Keep subject lines short and scan-friendly
- [ ] Keep CTAs aligned with:
  - Start with a conversation
  - Request a free estimate
  - `constructionconcern.com/free-estimate`
- [ ] Save the draft file

---

## 10) Build the final newsletter file

Open:
- `06_newsletter/final/[YYYY-MM]_newsletter_final.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the newsletter draft
- the new newsletter final file

### Checklist
- [ ] Create the cleaned final version
- [ ] Remove production notes
- [ ] Confirm all links and CTA language are consistent
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 11) Build the blog draft

Open:
- `07_blog/drafts/[YYYY-MM]_blog_draft.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the new monthly research summary
- the new internal dashboard
- the new client dashboard
- `02_prompts/05_blog_prompt.md`
- the new blog draft file

### Checklist
- [ ] Generate 4 blog posts
- [ ] Make sure topics support:
  - FAQs
  - process clarity
  - service education
  - local/seasonal homeowner relevance
  - material or upgrade comparisons
- [ ] Remove unsupported hard claims
- [ ] Keep CTA language clean and consistent
- [ ] Save the draft file

---

## 12) Build the final blog file

Open:
- `07_blog/final/[YYYY-MM]_blog_final.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the blog draft
- the new blog final file

### Checklist
- [ ] Clean the final version
- [ ] Tighten SEO titles if needed
- [ ] Use one primary SEO keyword per post
- [ ] Remove raw markdown links in body copy if needed
- [ ] Keep final CTA language simple and clean
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 13) Build the image prompt file

Open:
- `08_image_prompts/monthly/[YYYY-MM]_image_prompts.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the new monthly research summary
- the new client dashboard
- the final social posting file
- `02_prompts/07_image_prompt_prompt.md`
- the new image prompt file

### Checklist
- [ ] Generate one image prompt per approved social post
- [ ] Match each prompt to the platform and post concept
- [ ] Keep the visual direction:
  - warm
  - trustworthy
  - local
  - clean
  - authentic
  - homeowner-focused
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 14) Build the Gemini-ready image prompt file

Open:
- `08_image_prompts/monthly/[YYYY-MM]_image_prompts_gemini_ready.md`

Add to Copilot context:
- `01_config/client_profile.md`
- the full image prompt file
- the Gemini-ready file

### Checklist
- [ ] Create one final Gemini prompt per post
- [ ] Use only:
  - Post #
  - Platform
  - Final Gemini Prompt
- [ ] Remove design notes not needed by Gemini
- [ ] Do not include text overlays inside the Gemini prompt
- [ ] Add cleanup language where useful:
  - photorealistic
  - natural lighting
  - no watermark
  - no extra text
  - no exaggerated stock-photo poses
- [ ] Save the file
- [ ] Mark status as `Completed`

---

## 15) Final monthly QA check

Before you send or use anything, confirm:

### Research and dashboards
- [ ] Monthly research summary is completed
- [ ] Internal dashboard is completed
- [ ] Client dashboard is completed

### Social
- [ ] Social strategy is completed
- [ ] Final social posting file is clean and copy-ready

### Newsletter
- [ ] Draft is completed
- [ ] Final version is cleaned and approved

### Blog
- [ ] Draft is completed
- [ ] Final version is cleaned and approved

### Images
- [ ] Full image prompt file is completed
- [ ] Gemini-ready image prompt file is completed

### General quality check
- [ ] No leftover placeholder text
- [ ] No unsupported hard claims
- [ ] CTA language is consistent
- [ ] Local relevance is visible
- [ ] Tone is warm, credible, grounded, and not salesy

---

## 16) Optional month-end wrap-up

At the end of the month, update notes for next month:
- What worked well
- What needed too much cleanup
- Which prompts should be improved
- Which content formats felt strongest
- Which files should become the new reference model

Add those notes to:
- `10_archive`
or
- `00_admin/monthly_lessons_learned.md`

---

## Monthly execution order (short version)

0. Analytics review (prior month data)
1. Duplicate last month’s files
2. Research summary
3. Internal dashboard
4. Client dashboard
5. Social strategy
6. Final social posting file
7. Audience growth and engagement plan
8. Newsletter draft
9. Newsletter final
10. Blog draft
11. Blog final
12. Image prompt file
13. Gemini-ready image prompt file
14. QA review

---

## Default reminder

Do not rebuild the whole system each month.

Only update:
- the month’s files
- the month’s research
- any prompts or profile files that truly need revision

Everything else is already built.