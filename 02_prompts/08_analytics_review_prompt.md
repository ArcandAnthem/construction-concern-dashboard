# Analytics Review Prompt

You are performing a monthly analytics review for Construction Concern.

## Purpose

Review the previous month's performance data before generating any new content. This ensures the monthly content plan is informed by what actually worked — not just what was planned.

## Inputs

Add to context before running this prompt:
- `01_config/client_profile.md`
- any platform exports from the prior month (CSV files, screenshots, or copied data from Later.com, Wix, LinkedIn, Facebook, Instagram)
- the prior month's `[YYYY-MM]_social_strategy.md`
- the prior month's `[YYYY-MM]_internal_dashboard.md`

## What to analyze

For each platform with available data, report on:

### Social (Instagram, Facebook, LinkedIn, Threads)
- Total posts published
- Reach or impressions per post (average and top performer)
- Engagement rate (likes, comments, shares, saves)
- Top-performing post (format, topic, hook used)
- Lowest-performing post (format, topic, hook used)
- Follower count change (start vs. end of month)
- Best day and time based on engagement data
- Any content format signals (did carousels outperform single images?)

### Newsletter
- Send date(s)
- Open rate (if available)
- Click rate (if available)
- Subject line(s) used
- Any notable observations

### Blog / Website
- Total sessions or page views (from Wix or Google Analytics)
- Top-performing blog post by views
- Any SEO search terms that drove traffic (if available)
- Bounce rate signal (are people reading or leaving immediately?)

## Output format

Structure the output as:

### Monthly Performance Summary — [Month YYYY]

**Platform Snapshots**
(One paragraph or short bullet list per platform with the key numbers)

**What Worked**
(List the formats, topics, hooks, or timing that outperformed expectations)

**What Didn't Work**
(List the formats, topics, or approaches that underperformed)

**Top Performer of the Month**
(Single best post or content piece — what made it work)

**Audience Signals**
(Demographics, activity windows, growth or loss trends)

**Recommendations for Next Month**
(3–5 specific adjustments to carry forward into the new month's strategy)

## Rules

1. Be specific — cite actual numbers, not vague summaries.
2. If data is missing for a platform, note what's missing and flag it.
3. Do not generate new content in this step — only analyze and recommend.
4. Recommendations must tie directly to observed data, not assumptions.
5. If a content format consistently underperforms, say so clearly.
6. If a format consistently outperforms, recommend doubling down on it.

## How this fits the workflow

Run this prompt BEFORE Step 3 (monthly research summary) each month. The findings from this review should directly inform:
- the monthly research summary focus areas
- the social strategy format and hook decisions
- the newsletter topic prioritization
- the blog topic prioritization
