# American Glass Experts — Claude Context

## Site
- **URL:** https://www.americanglassexperts.us
- **Repo:** https://github.com/ktorres0109/american-glass-experts (Cloudflare Pages, auto-deploys on push to `main`)
- **Stack:** Static HTML (336+ files), no framework. All CSS inline per file.
- **Clean URLs:** Cloudflare Worker strips `.html`
- **Working dir:** `/Users/kel/Documents/projects/american-glass-experts/`

## Business
- Licensed glass contractor — C-17, CSLB #1125850
- Southern California, residential + commercial.
- Address: 6853 Reseda Blvd, Reseda, CA 91335 | Phone: (805) 750-6471

## CSS Design Tokens
```
--blue: #4a90d9
--blue-dk: #3a7bc8
--blue-lt: #6aaee8
--charcoal: #1e293b
--bg: #ffffff
--bg-soft: #f7f8fa
--coal: #0f172a
```
**Dark mode warning:** `[data-theme="dark"]` flips `--charcoal` to `#e2eaf4` (near-white). Never use `var(--charcoal)` as background for text — hardcode `#475569` or `#1e293b` directly.

Dark/light toggle via `data-theme` on `<html>`, stored in `localStorage('age-theme')`.

## Structure
- Root `.html`: `index.html`, `services.html`, `about.html`, `commercial.html`, `contact.html`, `review.html`, `blog.html`, `gallery.html`, city pages (138 total), service pages
- `commercial/{city}.html` — 138 commercial location pages (URLs: `/commercial/{city}`)
- `_redirects`: `/commercial-glass-* /commercial/:splat 301` handles old URLs
- Subdirs: `blog/`, `case-studies/`, `commercial/`

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

## Pending Tasks (manual — cannot be scripted)
- Fix BBB listing NAP (wrong address + phone — DA 91 hurting local authority) → bbb.org
- Build citations: Angi, Houzz, Bing Places, Thumbtack, Nextdoor, Apple Maps, BuildZoom
- Boost Google review velocity (text customers direct review link after each job)
- Verify GBP primary category is "Glass repair service" + add secondary categories

## Optional SEO Improvements (scriptable)
- Diversify reviews per page — 17 Yelp reviews available, currently same 6 on all 300+ pages
- Expand blog paragraphs — body paragraphs under optimal AI citation range (~80-130 words, target 134-167)
- HowTo schema on the installation guide blog post

## API Keys and Credentials
All private secrets live in `secrets/credentials.json`.
This folder is gitignored — **never push it to GitHub**.

Rules:
- Private API keys → always read from `secrets/credentials.json`
- Never hardcode private keys into HTML, JS, or CSS
- Never create credential files outside `secrets/`
- When adding a new key: store in `secrets/credentials.json`, document below

### Keys intentionally hardcoded (public by design — do not move)
- **Web3Forms key** (`53665885-fb86-4fce-8d07-d90806ff1317`) — client-side form key, must be in HTML to work
- **Google Analytics ID** (`G-0N1LQ71T8T`) — public tracking ID
- **IndexNow key** (`faa237c5f0e41eee3f2be30cfcc96af2`) — public verification key for Bing/Yandex
- **JSON-LD schema data** — public SEO markup
- **Cloudflare Wrangler account ID** — non-sensitive account metadata in `.wrangler/`

### Current credentials in secrets/credentials.json
*(none — no private secrets found in repo as of 2026-05-27)*

## Technical Rules
- Use Python batch scripts for changes touching many files — dry-run count first
- After changes: `git add -A && git commit -m "..." && git push origin main`
- Cloudflare auto-deploys on push
- **Never include `secrets/` in any git command.** Verify `.gitignore` before pushing.
