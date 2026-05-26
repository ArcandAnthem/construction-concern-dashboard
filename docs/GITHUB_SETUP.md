# GitHub Pages Setup Guide
## Making the Construction Concern Dashboard Public

This guide sets up a free public dashboard hosted on GitHub Pages.
No coding knowledge required. Takes about 15 minutes the first time.

---

## Your dashboard URL (once set up)

> **`https://arcandanthem.github.io/cc-content-dashboard/`**

This link will be live after you complete the setup steps below.
It does not exist yet — the files are only on your local computer until you push them to GitHub.

---

## One-time setup (do this once)

### Step 1: You already have a GitHub account
Your username is **arcandanthem**. Log in at [github.com](https://github.com).

### Step 2: Create a new repository

1. Once logged in, click the **+** button in the top right → **New repository**
2. Set these options:
   - **Repository name:** `cc-content-dashboard` (or `construction-concern-dashboard`)
   - **Visibility:** Public ✅ (required for free GitHub Pages)
   - **Initialize with README:** Yes ✅
3. Click **Create repository**

### Step 3: Upload the dashboard files

In the new repository, click **Add file** → **Upload files**

Upload these files from your `docs/` folder:
- `index.html`
- `internal.html`
- `weekly_checkin_template.md` (optional — you may prefer to keep this private)

Click **Commit changes** when done.

### Step 4: Enable GitHub Pages

1. In the repository, go to **Settings** (top navigation bar)
2. Scroll down to **Pages** in the left sidebar
3. Under **Source**, select:
   - Branch: `main`
   - Folder: `/ (root)` ← select root since you uploaded files directly
4. Click **Save**

GitHub will show a green banner: *"Your site is live at https://arcandanthem.github.io/cc-content-dashboard/"*

It may take 1–3 minutes to go live the first time.

### Step 5: Test your dashboard

Open the URL shown in the Pages settings.
- You should see the client dashboard (index.html)
- Add `/internal.html` to the URL to see the internal dashboard

Share the main URL with the client. Keep the internal URL for your own use.

---

## Monthly update workflow

Every month when you update the dashboard:

### Option A: Edit directly on GitHub (easiest)

1. Go to your GitHub repository
2. Click on `index.html`
3. Click the **pencil icon** (Edit this file) in the top right
4. Make your changes (update numbers, dates, status pills, weekly table rows)
5. Scroll down → click **Commit changes**
6. The dashboard updates within 60 seconds

### Option B: Edit locally and re-upload

1. Edit `docs/index.html` on your computer
2. Go to your GitHub repository
3. Click `index.html` → pencil icon → delete all text → paste your new version
4. Commit changes

---

## What to update each month

In `index.html`, look for these comments — they mark every field to update:

```
<!-- UPDATE THIS DATE EACH WEEK -->
<!-- UPDATE: change this summary each month -->
<!-- UPDATE: website sessions each month -->
<!-- UPDATE: Instagram follower count -->
<!-- UPDATE: FB avg reach per post -->
<!-- UPDATE: top post views -->
<!-- UPDATE: fill in each row at the end of each week -->
```

Search for `<!-- UPDATE` in the file to jump between them quickly.

---

## Making updates visible quickly

After any commit, GitHub Pages typically updates within **30–60 seconds**.
If you don't see changes, do a hard refresh: `Cmd + Shift + R` (Mac) or `Ctrl + Shift + R` (Windows).

---

## Private vs. public — what to share

| File | Share with client? | Notes |
|------|-------------------|-------|
| `index.html` (main URL) | ✅ Yes | Client-facing dashboard |
| `internal.html` | ❌ No | Internal only — don't publish the URL |
| `weekly_checkin_template.md` | ❌ Optional | Operational tool for Arc & Anthem use |

The internal dashboard IS technically accessible if someone guesses the URL. For true privacy, you would need GitHub Pro (paid) with private repositories and Pages. For now, the internal dashboard contains no sensitive financial data, so the current setup is acceptable.

---

## Optional: Custom URL

If you want the dashboard at a URL like `dashboard.arcanthem.com` or `dashboard.constructionconcern.com`:
1. In GitHub Pages settings, add a custom domain
2. Update your DNS provider with a CNAME record pointing to `arcandanthem.github.io`
This is optional — the default github.io URL works fine for client sharing.

---

## Getting help

If you get stuck on any step, the GitHub documentation is at:
`docs.github.com/en/pages`

Or ask Arc & Anthem — we can set this up on your behalf in a shared session.
