# American Glass Experts — Claude Context

## Site
- **URL:** https://www.americanglassexperts.us
- **Repo:** https://github.com/ktorres0109/american-glass-experts (Cloudflare Pages, auto-deploys on push to `main`)
- **Stack:** Static HTML (336+ files), no framework. All CSS inline per file.
- **Clean URLs:** Cloudflare Worker strips `.html`
- **Working dir:** `/Users/kel/Documents/projects/american-glass-experts/`

## Business
- Licensed glass contractor — C-17, CSLB #1125850
- Southern California, residential + commercial. Founded 2003.
- Address: 6853 Reseda Blvd, Reseda, CA 91335 | Phone: (805) 750-6471

## CSS Design Tokens
```
--blue: #2563eb
--charcoal: #1e293b
--bg: #ffffff
--bg-soft: #f7f8fa
--coal: #0f172a
```
**Dark mode warning:** `[data-theme="dark"]` flips `--charcoal` to `#e2eaf4` (near-white). Never use `var(--charcoal)` as background for text — use hardcoded `#475569` or `#1e293b` directly.

Dark/light toggle via `data-theme` on `<html>`, stored in `localStorage('age-theme')`.

## Structure
- Root `.html`: `index.html`, `services.html`, `about.html`, `commercial.html`, `contact.html`, `review.html`, `blog.html`, `gallery.html`, city pages (138 total), service pages
- `commercial-glass-{city}.html` — 130+ commercial location pages
- Subdirs: `blog/`, `case-studies/`

## Design Conventions
- `.reveal` + IntersectionObserver for scroll animations; stagger with `.d1/.d2/.d3`
- `.section-label` — eyebrow text (blue uppercase with line)
- `.btn-call` — phone CTA | `.btn.btn-primary` — primary action
- CTA: city pages use `.contact-strip` (`<!-- CONTACT STRIP -->`) | service pages use `.cta-band`
- Reviews: `.reviews-section` > `.reviews-grid` (3-col, 2×3 = 6 cards) > `.review-card` — CSS in `<style>` blocks per page

## Section Backgrounds (all 336+ pages)
- `.reviews-section`: light `var(--bg-soft)`, dark `#0C1117`
- Services "What We Do": always `#131A24` (force `data-theme="dark"`)
- Stats band: always `#0C1117`
- About "Built on Glass": always `#0C1117`

## Current Reviews (same 6 on all pages)
1. Alexis M. — Shower Enclosure — 5★
2. Jesus S. — Shower Enclosure — 5★
3. Joshua B. — Shower Glass — 5★
4. Mercy R. — Window Replacement — 5★
5. Dylan N. — Glass Services — 5★
6. Lisandro O. — Glass Panel — 5★

## Gallery
- Commercial page: `#gs-gallery-strip` + `#gs-lightbox`, images 71,7,15,8,20,35,56
- Services page: `#svc-gallery-strip` + `#svc-lightbox`, all 74 images shuffled, 90s/cycle
- R2 CDN: `https://pub-b4878fccfc85401e99bc2b4eff65255a.r2.dev/gallery/{n}.jpg`

## Case Studies
On hold — noindex on `case-studies.html` + 5 sub-pages, removed from nav. Re-enable when real photos ready: remove noindex, add nav link back to Commercial dropdown.

## History of Changes
1. Full nav updated across all 336+ pages: Residential ▾ / Commercial ▾ dropdowns
2. `/commercial` landing page created
3. `service-areas.html` updated with Residential/Commercial toggle
4. `index.html` updated with commercial highlight strip + footer commercial column
5. `privacy-policy.html`, `terms-of-service.html` exist
6. Footer: `Terms | Privacy | Sitemap | Service Areas` in footer-bottom row across all pages
7. Case studies soft taken down (noindex, removed from nav)
8. Reviews section (6 cards, 2×3 grid) added to all 148+ pages before CTA
9. Dark mode double-toggle bug fixed on 189 pages (rogue `<script>` after `</body>`)
10. `services.html` contact-strip upgraded to collapsible inline form
11. Map sections removed from all pages except `contact.html`
12. Reviews updated to 6 cards — Alexis M./Jesus S./Joshua B./Mercy R./Dylan N./Lisandro O. (real Yelp reviews)

## Pending Tasks (from ACTION-PLAN.md)
- Fix BBB listing NAP (wrong address + phone — DA 91 hurting local authority)
- Unique meta descriptions on all 131 city pages (all identical = GSC flag)
- Fix blog author schema: `"American Glass Experts Team"` → `Person: Frank Salinas, Lead Glazier`
- Add `#frank` bio section to `about.html`
- Fix contact form placeholder: `(818) 555-0000` → `(805) 750-6471` (133 pages)
- Fix copyright footer: `© 2025` → `© 2026`
- Add `logo`, `foundingDate: "2003"`, `hasOfferCatalog` to homepage schema
- Add Google Maps embed to homepage + top 5 city pages
- Build citations: Angi, Houzz, Bing Places, Thumbtack, Nextdoor, Apple Maps
- Optional: diversify reviews per page type (17 Yelp reviews available)
- Optional: move stats/trust bar above CTA on homepage

## Technical Rules
- Use Python batch scripts for changes touching many files — dry-run count first
- After changes: `git add -A && git commit -m "..." && git push origin main`
- Cloudflare auto-deploys on push
