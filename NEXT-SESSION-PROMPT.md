# Next Session Handoff — American Glass Experts

## Site Context

- **URL:** https://www.americanglassexperts.us
- **Repo:** https://github.com/ktorres0109/american-glass-experts (Cloudflare Pages auto-deploys on push to `main`)
- **Stack:** Static HTML (336+ files), no framework. All CSS inline per file. Clean URLs via Cloudflare Worker (strips `.html`).
- **CSS design tokens:** `--blue: #2563eb`, `--charcoal: #1e293b`, `--bg: #ffffff`, `--bg-soft: #f7f8fa`, `--coal: #0f172a`
- **Dark mode warning:** `[data-theme="dark"]` flips `--charcoal` to `#e2eaf4` (near-white). Never use `var(--charcoal)` as a background for text — use hardcoded values like `#475569` or `#1e293b` directly.
- **Business:** Licensed glass contractor (C-17, CSLB #1125850), Southern California. Residential + Commercial. Founded 2003.
- **Working dir:** `/Users/kel/Documents/projects/american-glass-experts/`

## What Was Done (Prior Sessions)

1. Full nav updated across all 336+ pages: split into **Residential ▾** / **Commercial ▾** dropdowns.
2. `/commercial` landing page created — hero, services, industries, county-based city links.
3. `service-areas.html` updated with Residential/Commercial audience toggle.
4. `index.html` updated with commercial highlight strip and footer commercial column.
5. `privacy-policy.html`, `terms-of-service.html` exist.
6. Footer: `Terms | Privacy | Sitemap | Service Areas` in footer-bottom row across all pages.
7. Case studies created but soft taken down (noindex, removed from nav) until real photos ready.
8. Reviews section (5 cards, `.reviews-section` > `.reviews-grid`) added to all 148+ pages before CTA. CSS already embedded in all pages.
9. **Dark mode toggle fixed on 189 pages** — rogue `<script>` block after `</body></html>` was binding a second click listener causing double-toggle (net no change). Removed from all.
10. `services.html` contact-strip upgraded to collapsible inline form.
11. Always push to GitHub after changes.

## Tasks for Next Session

### 1. REMOVE "Our Location" / Map section from ALL pages
- Look for `<!-- MAP -->` comment or section containing `"Visit Our Showroom"` / Google Maps `<iframe>`
- Remove from every page that has it — check services.html, index.html, city pages, service pages
- Keep footer address text — only remove the embedded map section

### 2. Change reviews grid: 5 cards → 6 cards (2×3 grid)
- Current layout: 3 cards row 1 + 1 card + 1 `.review-wide` (span 2 cols) = asymmetric
- New layout: 6 equal cards, `grid-template-columns: repeat(3,1fr)`, 2 rows × 3 cols
- Remove `review-wide` class from all review sections — all cards equal width
- Apply across ALL pages

### 3. Add more diverse reviews per page (USER WILL PASTE REVIEWS AT SESSION START)
- User will paste raw Yelp reviews from: https://www.yelp.com/biz/american-glass-experts-san-fernando-valley-4
- Goal: different pages show different subsets — not the same 5 curated ones everywhere
- Include negative/mixed reviews too, not just best ones
- Strategy: rotate by page type (city pages get local-feeling reviews, service pages get service-specific ones)

### 4. Homepage: move stats/trust bar above CTA
- On `index.html`, identify stats/trust strip and move it to appear directly above the contact-strip CTA
- Confirm exact element with user

## Current Reviews (in all pages right now)
1. Erendira N. — Shower Enclosure — 5★
2. Kevin F. — Shower Enclosure — 5★
3. Jaquelyn S. — Frameless Shower — 5★
4. Jesus R. — Glass Partitions — 5★
5. Salinas R. — Glass Partitions — 5★

## Technical Notes
- Always use **Python batch scripts** for changes touching many files
- Run dry-run count before writing
- After all changes: `git add -A`, commit, `git push origin main`
- Cloudflare Pages deploys automatically
- Clean URLs: `.html` stripped by Cloudflare Worker
- `.review-wide { grid-column: span 2; }` — remove this from reviews when switching to 6-card layout
- Reviews CSS is inside `<style>` blocks per page, not an external file

## Gallery Technical Details
- Commercial page: `#gs-gallery-strip` + `#gs-lightbox`, images 71,7,15,8,20,35,56
- Services page: `#svc-gallery-strip` + `#svc-lightbox`, all 74 images shuffled, 90s/cycle
- R2 CDN: `https://pub-b4878fccfc85401e99bc2b4eff65255a.r2.dev/gallery/{n}.jpg`

## Case Studies (On Hold)
When real photos ready: remove noindex from `case-studies.html` + 5 sub-pages, add back nav link to Commercial dropdown.
