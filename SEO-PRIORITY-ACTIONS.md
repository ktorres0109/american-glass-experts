# SEO Priority Actions — americanglassexperts.us
*Generated: 2026-05-23 | Data source: Google APIs (GSC, GA4, URL Inspection)*

---

## Site Status Snapshot

| Metric | Value |
|---|---|
| Homepage | Indexed, last crawled May 22 2026 |
| Sitemap | 297 submitted / 0 indexed (new site, normal — monitor) |
| Rich Results | FAQ + Review snippets passing on homepage |
| Organic sessions (28d) | 88 sessions / 76 users / 170 pageviews |
| Avg daily sessions | 3.4/day (trending up) |
| Schema (commercial pages) | Fixed May 23 — incomplete LocalBusiness removed from 138 pages |

---

## City Page Structure

- **139 residential city pages** — `/city-name` (e.g. `/northridge`)
- **138 commercial city pages** — `/commercial-glass-city` (e.g. `/commercial-glass-northridge`)
- Already separated by URL — no restructuring needed

---

## Priority 1 — Fix API Key (PageSpeed + CrUX)

**Problem:** PSI + CrUX APIs were not enabled for the GCP API key.

**Fix:** In Google Cloud Console (project: morning-bot):
1. APIs & Services → Library → enable **PageSpeed Insights API**
2. APIs & Services → Library → enable **Chrome UX Report API**
3. Credentials → click the key → confirm restrictions include both APIs

Without this: no Core Web Vitals field data, no Lighthouse scores via `/seo google pagespeed`.

---

## Priority 2 — Emergency Glass Page Content

**Why:** `/emergency-glass` ranks position ~20 for:
- "24 hour glass repair los angeles" — 30 impressions, 0 clicks
- "24 hour window repair los angeles" — 22 impressions, 0 clicks
- "24/7 emergency glass service" — impressions, 0 clicks

Position 20 = page 2 = no clicks. Needs to crack top 10.

**Fix:**
- Add dedicated H2 sections: "24-Hour Glass Repair in Los Angeles", "Same-Day Emergency Board-Up"
- Add FAQ entries targeting "24 hour" and "emergency" variants
- Add service schema with `availableChannel` → `servicePhone` for 24/7
- Internal links from top city pages (LA, Burbank, Northridge) to `/emergency-glass`

---

## Priority 3 — Sitemap Indexed 0/297

**Why:** 297 URLs submitted, 0 credited as "indexed via sitemap" in GSC.
Not an error — Google crawls on its own schedule. But worth monitoring.

**Fix (when ready):**
- Use `/seo google index-batch` to ping Indexing API for top 50 pages
- Monitor weekly: GSC → Sitemaps → check indexed count
- Re-check in 2-4 weeks

---

## Priority 4 — Simi Valley Local Ranking

**Why:** `/simi-valley` at position 17 for "simi valley glass" (10 impressions). Should rank top 5 for a local branded term.

**Fix:**
- Verify GBP has Simi Valley service area listed
- Add "Simi Valley" explicitly in H1 and first paragraph
- Get a citation on Yelp/Nextdoor specifically mentioning Simi Valley

---

## Priority 5 — Unique Meta Descriptions (131 city pages)

**Issue:** All 131 city pages use identical meta descriptions — flagged in GSC.
**Fix:** Batch Python script to generate unique descriptions per city. Pattern:
`"Glass repair and installation in {City}, CA. Shower enclosures, window repair, storefront glass. Licensed C-17 contractor. Call (805) 750-6471."`

---

## Priority 6 — BBB Listing NAP

**Issue:** BBB listing has wrong address + phone (DA 91 — high authority citation sending wrong signals).
**Fix:** Claim/correct listing at bbb.org. Address: 6933 Reseda Blvd Unit J, Reseda CA 91335. Phone: (805) 750-6471.

---

## Priority 7 — Contact Form Placeholder

**Issue:** 133 pages show `(818) 555-0000` placeholder instead of real phone.
**Fix:** Batch replace across all pages.

---

## Pending Setup

- [ ] Fix API key (PSI + CrUX APIs not enabled in GCP project)
- [ ] Add GA4 data to Claude config (done — `properties/534586830`)
- [ ] Apply for Google Ads Basic Access (exact search volumes vs bucketed)
- [ ] Wire up Keyword Planner after Ads API approved

---

## Google APIs Status

| API | Status |
|---|---|
| Search Console | Working |
| URL Inspection | Working |
| Indexing API | Working |
| GA4 Data API | Working |
| PageSpeed Insights | API key invalid — needs fix |
| CrUX | API key invalid — needs fix |
| Google Ads / Keyword Planner | Configured (test token — bucketed volumes) |

Config: `~/.config/claude-seo/google-api.json`
