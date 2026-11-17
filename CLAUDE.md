# American Glass Experts — Claude Context

## Site
- **URL:** https://www.americanglassexperts.us
- **Repo:** https://github.com/ktorres0109/american-glass-experts
- **Hosting:** Cloudflare Worker `american-glass-experts` with static assets (`wrangler.jsonc`, `.assetsignore`). Auto-deploys on push to `main` via Workers Builds (fixed 2026-11-16: a root `requirements.txt` made the build pip-install Playwright and fail; it now lives in `tests/`. Never put `requirements.txt` or `package.json` in the repo root). `american-glass-web` is an unused workers.dev copy. Manual fallback: `wrangler deploy`. After pushing, check the build with `gh api repos/ktorres0109/american-glass-experts/commits/<sha>/check-runs` and `curl` a changed page.
- **Stack:** Static HTML (313 pages), no framework. CSS is in `/css/*.css` (one sheet per page type), plus some inline styles.
- **Clean URLs:** `_redirects` strips `.html`; response headers come from `_headers` (the Worker script does not run for asset hits)
- **Working dir:** `/Users/kel/Documents/projects/american-glass-experts/`

## Business
- Licensed glass contractor — C-17, CSLB #1125850 (issued 2024-08-30, active through 2028-08-31, verified on CSLB 2026-11-16; CSLB address of record is still Simi Valley)
- Emergency board-up is 24 hours (owner confirmed); shop hours Mon–Sat 7am–10pm
- Owner confirmed true: 1,000+ jobs, 20+ years combined experience, bonded and insured, curtain wall / high-rise work
- Southern California, residential + commercial.
- Address: 6933 Reseda Blvd Unit J, Reseda, CA 91335 | Phone: (805) 750-6471

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
On hold, removed from nav. Owner confirmed 2026-11-16 the case studies are real and should be shown, especially from commercial pages. No noindex tags remain; all 6 are in `sitemap.xml`. They still have no photos.

## History of Changes
1. Full nav updated across all 336+ pages: Residential ▾ / Commercial ▾ dropdowns
2. `/commercial` landing page created
3. `service-areas.html` updated with Residential/Commercial toggle
4. `index.html` updated with commercial highlight strip + footer commercial column
5. `privacy-policy.html`, `terms-of-service.html` exist
6. Footer: `Terms | Privacy | Sitemap | Service Areas` in footer-bottom row across all pages
7. Case studies soft taken down (noindex, removed from nav); re-enabled 2026-11-16
8. Reviews section (6 cards, 2×3 grid) added to all 148+ pages before CTA
9. Dark mode double-toggle bug fixed on 189 pages (rogue `<script>` after `</body>`)
10. `services.html` contact-strip upgraded to collapsible inline form
11. Map sections removed from all pages except `contact.html`
12. Reviews updated to 6 cards — Alexis M./Jesus S./Joshua B./Mercy R./Dylan N./Lisandro O. (real Yelp reviews)
13. 2026-11-16: phone field added to estimate modal (295 pages); `/glass-partitions` rebuilt; `/operable-glass-walls` and `/commercial/glass-door-repair` created; partitions, operable walls, and door links added to all 276 city pages; Company Facts table and AboutPage schema on `/about`; business details inlined in `Service.provider` on 138 commercial city pages; `robots.txt` names OAI-SearchBot, ChatGPT-User, Claude-SearchBot, Claude-User, Perplexity-User; `llms.txt` refreshed; `click_to_call` GA4 event sitewide; GA added to `/commercial`; mobile overflow fixed on `/commercial`; invalid schema type `GlassOrMirrorShop` removed; auto-deploy repaired

## State and Playbook (written 2026-11-16, read this first)

**Business goal:** more commercial leads. The owner's brother lives on this business. Priority order: office glass partitions and glass walls, operable glass walls, commercial glass doors, storefronts, commercial windows, then residential.

### Facts confirmed by the owner (safe to state on the site)
- Serves all 138 listed cities. Keep every city page; never noindex or delete one.
- Installs fixed glass partitions and operable glass walls (sliding, stacking, folding) and swing glass doors.
- Emergency board-up is 24 hours a day. Shop hours are Mon–Sat 7am–10pm.
- True claims: 1,000+ jobs, 20+ years combined experience, bonded and insured, curtain wall / high-rise work.
- Case studies are real. Show them. They have no photos yet.
- Do not invent prices, timelines, client names, certifications, or project details. Reuse wording already on the site.

### Measured on 2026-11-16 (Google Search Console)
- 90 days: 52,406 impressions, 84 clicks (CTR 0.16%). Most clicks are brand searches.
- Index check of 312 URLs: 120 indexed, 188 "Crawled - currently not indexed" (106 commercial city pages, about 80 residential). June 2026 was 251 indexed. No technical block. Cause: city pages are 46–56% identical and the domain has little authority. More template text will not fix it; real per-city job photos and consistent listings will.
- Query gaps that had no page: partitions, operable glass walls, commercial glass door repair. All three now have pages.
- Still weak: "commercial window repair" (945 impressions, position 17), "commercial glass repair near me" (790, position 47), "custom mirror installation" (631, position 79), "shower door repair near me" (622, position 50).

### Key pages (commercial money pages)
- `/glass-partitions`, `/operable-glass-walls`, `/commercial/glass-door-repair`, `/glass-railings`, `/storefront-glass`, `/commercial/window-repair`, `/commercial/emergency-glass`, `/commercial` (hub), `/case-studies`.
- New service pages are made by cloning `glass-partitions.html`: replace the block from `<section class="page-hero">` to `<!-- REVIEWS -->`, update title, description, JSON-LD (`Service`, `FAQPage`, `WebPage` name), and the `'partitions'` entry in the `SERVICES` object, which feeds the quote modal. Pages under `commercial/` need absolute asset paths (`/flag-us.svg`).
- Then: add to `sitemap.xml` and `llms.txt`, link from `commercial.html` and related pages, and ping IndexNow.
- Root URLs starting with `/commercial-glass-` are redirected by `_redirects`; do not create pages with that prefix.

### Added late 2026-11-16
- `/glass-railings` page. "Commercial" added to the top and mobile menus sitewide. Top menu collapses to the hamburger at 1180px (rule appended to every `css/*.css` and to pages with inline nav CSS); with six links the header overflows below that, so keep this rule if links are added.
- Footer "Services" column sitewide links `/commercial`, `/operable-glass-walls`, `/commercial/glass-door-repair`.
- Real job photos already exist in the R2 gallery and are now used in `#project-photos` grids. Verified by eye: partitions/office glass 8, 14, 20, 35, 40, 43, 49, 56, 57, 58; glass doors 28, 41, 50; stair railings 59, 60, 64; storefronts 6, 68, 71; board-up 74; retail interiors 1, 2, 3, 5, 38. Look at an image before using it; captions must describe only what is visible.
- Homepage offer catalog schema lists operable walls, door repair, railings. Money pages use a real photo as `og:image`.

### Shared header and footer (2026-11-16)
- Every page except `review.html` has the same `<nav>`, `#nav-mobile` menu, and `<footer>`, copied from `index.html` with absolute asset paths. Only differences: `class="active"` on the current nav link; city pages keep their own `footer-desc`, "Nearby" footer column, and copyright line; other pages get a "Company" column. To change header or footer, edit `index.html` then re-apply to all pages with a batch script (regex on `<nav>…</nav>`, `#nav-mobile`, `<footer>…</footer>`).
- All 6 blog posts use `css/blog-post.css`. Homepage H1 is "Glass Partitions & Storefronts" (owner asked for a commercial-first homepage).

### How to work on this site
- Batch edits: Python script with exact-string asserts and a count before writing. Validate every JSON-LD block with `json.loads` after edits.
- Visual check before calling UI done: headless Playwright with Brave, 1280 and 390 wide, check `document.documentElement.scrollWidth` equals the viewport and no `pageerror`. Use `.claude/skills/seo/.venv/bin/python`; Bash sandbox must be off.
- Google data: `/opt/homebrew/bin/python3.14 .claude/skills/seo/scripts/gsc_query.py` and `gsc_inspect.py`. If auth returns 401, the user must re-run `google_auth.py --auth --creds ~/.config/claude-seo/client_secret.json` (OAuth app is in Testing mode, token dies every 7 days). PageSpeed API key is invalid. Keyword Planner needs the adwords scope and the `google-ads` package.
- After deploy: IndexNow POST to `https://api.indexnow.org/indexnow` with key `faa237c5f0e41eee3f2be30cfcc96af2` (see `ping-indexnow.sh`). Bing feeds ChatGPT search.
- Lead forms post to Web3Forms. The estimate modal (`#modal-form`) requires a phone number since 2026-11-16; keep it required.
- GA4 event `click_to_call` fires on every `tel:` link tap.

### Open work, best first
1. More real job photos, especially operable (sliding/folding) walls and case studies; the owner is collecting them. Gallery photos already cover partitions, doors, and railings.
2. Per-city real job content (photo plus two lines) on the city pages that bring work, to get them re-indexed.
3. Strengthen `/commercial/window-repair` for "commercial window repair" (position 17).
4. `service-areas.html` links 121 of 138 commercial city pages; 17 are missing (their residential cards use different markup).
5. Re-run the GSC index check in a few weeks and compare with the 120 baseline.

## Pending Tasks (manual — owner only)
- Same address everywhere: CSLB record (still 1112 Richardson Ave, Simi Valley, phone (818) 426-4649), Yelp, BBB, Google Business Profile, MapQuest should all show 6933 Reseda Blvd Unit J and (805) 750-6471. Mixed addresses are why customers doubted ChatGPT's listing.
- Google Business Profile: add services "Glass partitions", "Office glass walls", "Operable glass walls", "Commercial glass door repair"; post job photos.
- Request indexing about 10 URLs a day from `~/Desktop/AGE-pages-to-index.txt`.
- Citations: Angi, Houzz, Bing Places, Thumbtack, Nextdoor, Apple Maps, BuildZoom. Sign up for Bing Webmaster Tools.
- Ask each customer for a Google review after the job.

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
- Cloudflare auto-deploys on push (see Hosting above); verify the build passed
- Visual checks: headless Playwright with Brave (`/Applications/Brave Browser.app`), or Zen. Never Chrome.
- **Never include `secrets/` in any git command.** Verify `.gitignore` before pushing.
