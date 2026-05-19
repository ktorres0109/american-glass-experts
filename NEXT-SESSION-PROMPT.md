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
11. **Map sections removed from all pages** (except `contact.html`) — covered `<!-- MAP -->`, `<!-- MAP EMBED -->`, `<!-- OUR LOCATION MAP -->` variants across 150 pages.
12. **Reviews updated to 6 cards (2×3 grid)** across all 149 pages — replaced Erendira N./Kevin F./Jaquelyn S./Jesus R./Salinas R. with Alexis M./Jesus S./Joshua B./Mercy R./Dylan N./Lisandro O. All 5★ real Yelp reviews. Removed `review-wide` class.
13. Always push to GitHub after changes.

## Tasks for Next Session

### 1. ~~REMOVE Map sections~~ ✅ DONE
### 2. ~~Reviews 5→6 cards~~ ✅ DONE

### 3. Diversify reviews per page type (OPTIONAL FOLLOW-UP)
- Currently: same 6 reviews on every page
- Goal: city pages show local-feeling reviews, service pages show service-specific ones
- Yelp source: https://www.yelp.com/biz/american-glass-experts-san-fernando-valley-4
- 17 total reviews available (see NEXT-SESSION-PROMPT for full list when ready)

### 4. Homepage: move stats/trust bar above CTA
- On `index.html`, identify stats/trust strip and move it to appear directly above the contact-strip CTA
- Confirm exact element with user

## Current Reviews (in all pages right now)
1. Alexis M. — Shower Enclosure — 5★
2. Jesus S. — Shower Enclosure — 5★
3. Joshua B. — Shower Glass — 5★
4. Mercy R. — Window Replacement — 5★
5. Dylan N. — Glass Services — 5★
6. Lisandro O. — Glass Panel — 5★

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
