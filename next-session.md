# American Glass Experts — SEO Session Handoff
*Last updated: 2026-05-25*

## Site
- URL: https://www.americanglassexperts.us
- Stack: Static HTML, Cloudflare Pages (auto-deploy on push to `main`)
- Working dir: `/Users/kel/Documents/projects/american-glass-experts/`
- 336+ HTML files, `commercial/` subdir (138 city pages), `blog/` subdir

---

## What Was Fixed This Session

### Ahrefs Issues
- [x] **Broken images** — `flag-us.svg` → `/flag-us.svg` on all 138 commercial pages (relative path bug)
- [x] **Orphan page** — `window-installation-alhambra.html` now linked from `window-repair.html` + `services.html` footer
- [x] **Meta descriptions too long** — trimmed to ≤155 rendered chars on 5 pages: `services`, `reseda`, `gallery`, `custom-mirrors`, `storefront-glass`

### Semrush / Structured Data
- [x] **LocalBusiness missing address** — added `PostalAddress` (6853 Reseda Blvd, Reseda CA 91335) to 6 service pages: `custom-mirrors`, `shower-enclosures`, `storefront-glass`, `window-repair`, `gallery`, `emergency-glass`
- [x] **Duplicate H1/title** — fixed `blog/commercial-storefront-glass-repair-los-angeles.html` title → "LA Commercial Storefront Glass Repair | American Glass Experts" (62 chars)
- [x] **Title too long** — `temple-city.html` trimmed to 62 chars

### Technical / Performance
- [x] **HSTS + security headers** — created `_headers` file for Cloudflare Pages (`Strict-Transport-Security`, `X-Frame-Options`, `X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy`)
- [x] **Sitemap** — added missing `/commercial` hub page (was in file system, not sitemap); updated lastmod for 6 modified pages
- [x] **CSS externalized** — massive win for text/HTML ratio and page weight:
  - `css/commercial-city.css` — 138 commercial city pages + 8 service pages (38KB saved each)
  - `css/city-page.css` — 138 residential city pages (37KB saved each)
  - `css/blog-post.css` — 4 blog posts (39KB saved each)
  - `css/index.css`, `services.css`, `gallery.css`, `contact.css`, `commercial.css`, `service-areas.css`, `about.css`, `blog.css`, `blog-shower-door.css`, `blog-commercial-storefront.css` — hub pages
  - **Result:** text/HTML ratio improved from ~8% → 15-19% on city/service pages

---

## Still Under 10% Text/HTML Ratio (needs body copy added)

| Page | Ratio | Issue |
|---|---|---|
| `gallery.html` | 0.031 | JS-heavy gallery — hard without refactor |
| `services.html` | 0.058 | Nav/feature-heavy — add intro paragraphs |
| `contact.html` | 0.063 | Form page — naturally low, low priority |
| `service-areas.html` | 0.064 | Link-list heavy — add regional intro copy |
| `commercial-glass.html` | 0.081 | Add more body paragraphs |
| `review.html` | 0.035 | **noindexed** — ignore |

---

## Remaining SEO Tasks (priority order)

### High Priority
1. **Diversify reviews per page** — same 6 reviews on all 300+ pages. 17 Yelp reviews available. Duplicate content signal. Need to rotate which 6 show per page using a Python script.
2. **Trigger fresh Semrush crawl** — all fixes deployed, need updated report to see real remaining errors (current data is stale May 23 crawl). Hit "Rerun campaign" and screenshot new Errors + Warnings tabs.
3. **Add body copy to thin pages** — `services.html`, `service-areas.html`, `commercial-glass.html` need more visible text to push ratio above 10%

### Medium Priority
4. **HowTo schema** on `blog/glass-shower-door-installation-los-angeles.html` — quick structured data win
5. **Blog paragraph expansion** — body paragraphs should be 80–130 words for AI citation coverage. Check all 6 blog posts.
6. **Expand `llms.txt`** — add commercial hub page + new blog posts to Pages/Blog Posts sections (currently missing `/commercial`, `/commercial/{city}` pages)
7. **Google Search Console** — need screenshots of: Coverage Errors, Core Web Vitals, top queries by impressions (positions 4-20 are closest to page 1)

### Manual (can't script)
8. **BBB listing NAP fix** — wrong address + phone on bbb.org (DA 91 backlink, high value) → fix at bbb.org
9. **Citation building** — Angi, Houzz, Bing Places, Thumbtack, Nextdoor, Apple Maps, BuildZoom
10. **Google review velocity** — text customers direct GBP review link after each job
11. **GBP primary category** — verify "Glass repair service" is primary + add secondary categories

---

## CSS Architecture (new — this session)

All inline CSS extracted. Files in `/css/`:
- `commercial-city.css` — shared by `commercial/*.html` + service pages (shower-enclosures, window-repair, sliding-window-repair, custom-mirrors, emergency-glass, storefront-glass, commercial-glass, window-installation-alhambra)
- `city-page.css` — shared by all root-level city pages (reseda, burbank, glendale, etc.)
- `blog-post.css` — shared by 4 blog posts (emergency, foggy-window, frameless-shower-door, storefront-glass-replacement)
- Individual CSS files for each hub page

**IMPORTANT:** If adding new city pages, use `<link rel="stylesheet" href="/css/city-page.css">` instead of inline `<style>` blocks.

---

## Key Files / Paths
- `sitemap.xml` — 298 URLs, lastmods updated
- `_headers` — Cloudflare security headers (new this session)
- `_redirects` — URL redirect rules
- `llms.txt` — AI indexing file (complete, not causing real issues)
- `css/` — all extracted stylesheets (new this session)

## Semrush Audit Status (as of May 23 crawl — stale)
- **Health score:** 92% | Errors: 29 | Warnings: 113 | Crawled: 100/100
- Most errors/warnings from this crawl are NOW FIXED. Need fresh crawl to get accurate count.

## Ahrefs Status
- Broken images: fixed
- Orphan pages: fixed (was 2, now 0)
- Meta descriptions: fixed (was 6, now 0)
