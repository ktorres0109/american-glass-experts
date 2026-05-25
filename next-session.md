# American Glass Experts — SEO Session Handoff
*Last updated: 2026-05-25 (Session 2)*

## Site
- URL: https://www.americanglassexperts.us
- Stack: Static HTML, Cloudflare Pages (auto-deploy on push to `main`)
- Working dir: `/Users/kel/Documents/projects/american-glass-experts/`
- 336+ HTML files, `commercial/` subdir (138 city pages), `blog/` subdir

---

## What Was Fixed This Session (Session 2 — May 25)

### Blog Content (AI Citation Coverage)
- [x] **Blog paragraphs expanded** across 5 posts — target 80-130w per paragraph
  - `commercial-storefront-glass-repair`: avg 53w → 70w
  - `glass-shower-door-installation`: avg 54w → 74w
  - `emergency-glass-repair`: avg 65w → 77w
  - `storefront-glass-replacement`: avg 62w → 75w
  - `frameless-shower-door-cost`: closing paragraph expanded
- [x] **llms.txt updated** — added `/commercial` hub + 10 sample commercial city URLs

### Schema.org (Ahrefs crawl — 143 page error)
- [x] **AggregateRating field types fixed** — `ratingValue`, `reviewCount`, `bestRating`, `worstRating` were strings → now proper JSON numbers (float/int)
  - Fixed on 139 residential city pages, service pages, blog posts
  - Fixed `Review.reviewRating.ratingValue` strings in `index.html`

### OG URL Mismatch (Ahrefs — 7 pages)
- [x] **og:url hardcoded to `/corona`** on 7 city pages — template copy-paste bug
  - Fixed: la-habra, bellflower, arcadia, beverly-hills, west-hollywood, cerritos, norwalk
  - Each now matches its own canonical URL

### Title Too Long (Ahrefs — 4-6 pages)
- [x] `blog/commercial-storefront-glass-repair-los-angeles.html` trimmed 62c → 58c
- [x] All 5 `case-studies/*.html` titles trimmed to ≤60c (noindexed but clean)

### Links to Redirect (Ahrefs — 138 pages)
- [x] **BreadcrumbList `item` URL had trailing slash** (e.g., `/reseda/`) — hits Cloudflare `/*/ → /:splat` 301 rule
  - Fixed on all 138 residential city pages

### Reviews
- [x] **Confirmed** reviews already diversified from Session 1 (17 reviews, deterministic by filename seed). Script ran clean (no changes = already done).

---

## Expected Improvements on Next Ahrefs Crawl
| Issue | Before | After (expected) |
|---|---|---|
| Schema.org validation errors | 143 pages | ~0 |
| OG URL ≠ canonical | 7 pages | 0 |
| Pages with links to redirect | 1+ pages | 0 |
| Title too long | 4 pages | 0 |

---

## Still Open (priority order)

### High Priority
1. **Internal linking** — 24+5 pages have only 1 dofollow incoming link. Need to add cross-links from related city/service pages.
2. **Google Search Console** — pull Coverage Errors, Core Web Vitals, top queries positions 4-20 (closest to page 1). These are the real ranking opportunities.
3. **Semrush fresh crawl** — hit "Rerun campaign" to see what's left after all May 25 fixes.

### Medium Priority
4. **Blog paragraph expansion (continued)** — `glass-shower-door-installation` still 10/15 paras under 80w. Could push avg from 74w → 90w+.
5. **`services.html` body copy** — still ~5.8% text/HTML ratio. Add 2-3 intro paragraphs explaining service overview.
6. **Add body copy to `service-areas.html`** — already has good copy but city link grid makes ratio low. Consider adding a "Why Southern California?" section.

### Manual (can't script)
7. **BBB listing NAP fix** — wrong address + phone on bbb.org (DA 91 backlink, high value)
8. **Citation building** — Angi, Houzz, Bing Places, Thumbtack, Nextdoor, Apple Maps, BuildZoom
9. **Google review velocity** — text customers direct GBP review link after each job
10. **GBP primary category** — verify "Glass repair service" is primary + add secondary categories

---

## Ahrefs Status (as of May 25 crawl — this session)
- **Health score: 100** (Errors: 0, Warnings: 7, Notices: many)
- Active warnings:
  - Noindex page: 8 (intentional — case-studies + review.html)
  - OG URL mismatch: 7 → **FIXED, pending recrawl**
  - Page has links to redirect: 1 → **FIXED, pending recrawl**
  - Slow page: 1 (pacific-palisades.html, 2,761ms TTFB — cold Cloudflare cache, not a code issue)
  - 3XX redirect: 1 (HTTP→HTTPS Cloudflare redirect — expected, not fixable)
- Notices that are noise: Title changed (290), Word count changed (141) — from our content edits

## Semrush Status (as of May 23 crawl — stale)
- Health score: 92% | Errors: 29 | Warnings: 113
- All major errors from May 23 crawl are now fixed. Need fresh crawl.

---

## CSS Architecture (unchanged from Session 1)
All inline CSS extracted. Files in `/css/`:
- `commercial-city.css` — shared by `commercial/*.html` + service pages
- `city-page.css` — shared by all root-level city pages
- `blog-post.css` — shared by 4 blog posts
- Individual CSS files for each hub page

**IMPORTANT:** New city pages use `<link rel="stylesheet" href="/css/city-page.css">` not inline styles.

---

## Key Files / Paths
- `sitemap.xml` — 299 URLs (commercial hub added), lastmods updated
- `_headers` — Cloudflare security headers
- `_redirects` — URL redirect rules (5 rules)
- `llms.txt` — AI indexing file, commercial hub + city URLs added
- `css/` — all extracted stylesheets
- `scripts/diversify_reviews.py` — deterministic review rotation (17 reviews, seed=filename)
- `scripts/reviews.json` — all 17 Yelp reviews

## Review System (as of Session 1)
- 17 reviews in `scripts/reviews.json`
- All 149 pages with review sections have unique rotating sets of 6
- Seed = filename → same 6 on every crawl, different across pages
- Current 6 on any page deterministic: run dry-run to check
