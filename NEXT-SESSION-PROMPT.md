# Next Session Handoff — American Glass Experts

## Site Context

- **URL:** https://www.americanglassexperts.us
- **Repo:** https://github.com/ktorres0109/american-glass-experts (Cloudflare Pages auto-deploys on push to `main`)
- **Stack:** Static HTML (336+ files), no framework. All CSS inline per file. Clean URLs via Cloudflare Worker (strips `.html`).
- **CSS design tokens:** `--blue: #2563eb`, `--charcoal: #1e293b`, `--bg: #ffffff`, `--bg-soft: #f7f8fa`, `--coal: #0f172a`
- **Dark mode warning:** `[data-theme="dark"]` flips `--charcoal` to `#e2eaf4` (near-white). Never use `var(--charcoal)` as a background for text — use hardcoded values like `#475569` or `#1e293b` directly.
- **Business:** Licensed glass contractor (C-17, CSLB #1125850), Southern California. Residential + Commercial. Founded 2003.
- **Working dir:** `/Users/kel/Documents/projects/american-glass-experts/`

## What Was Done (This + Prior Sessions)

1. Full nav updated across all 336+ pages: split into **Residential ▾** / **Commercial ▾** dropdowns.
2. `/commercial` landing page created — hero, services, industries, county-based city links.
3. `service-areas.html` updated with Residential/Commercial audience toggle.
4. `index.html` updated with commercial highlight strip and footer commercial column.
5. `privacy-policy.html` exists and is complete.
6. `terms-of-service.html` created (noindex).
7. Footer across all pages: `Terms | Privacy | Sitemap | Service Areas` in footer-bottom row.
8. **Case studies** created (`case-studies.html` hub + 5 individual pages in `case-studies/`) but **soft taken down** (noindex + removed from nav) until real photos are ready.
9. **Residential nav dropdown** now starts with: `<li><a href="/services" style="font-weight:600;color:var(--blue);">All Residential →</a></li>`
10. **Commercial nav dropdown** has `All Commercial →` link at top.
11. **`commercial.html`** — county badge fix (hardcoded `#475569`), full commercial services list (19 tiles + "...and more"), scrolling gallery strip (images: 71, 7, 15, 8, 20, 35, 56).
12. **`services.html`** — full residential services list (23 tiles + "...and more"), shuffled full gallery (all 74 images, seed=42, 90s/cycle).
13. Gallery strips use R2 CDN: `https://pub-b4878fccfc85401e99bc2b4eff65255a.r2.dev/gallery/{n}.jpg` (74 images, 1–74).

## Current State / Pending Tasks

### 1. Add Testimonials Section Before CTA (HIGH PRIORITY)

**Decision:** Add a testimonials/reviews section **before the "Get Your Free Estimate" CTA strip** on key pages (services.html, commercial.html, index.html at minimum). This is the highest-conversion placement — social proof answers "can I trust them?" right before asking users to act.

**5 real reviews already in index.html schema (use these):**
1. **Erendira N.** — "The glass completely transformed our shower. Their pricing was very competitive and what set them apart was their product knowledge and clear communication."
2. **Kevin F.** — "Perfect experience from beginning to end. The technician was very knowledgeable and gave great advice. Absolutely thrilled with our new shower glass."
3. **Jaquelyn S.** — "Frameless enclosure with starphire glass and brass hardware — love it. The glass is super clear, the brass looks elegant, and installation was done perfectly."
4. **Jesus R.** — "As a contractor I am very particular and American Glass Experts delivered. They measured for our glass partitions, recommended the right glass, showed up on time, and the office turned out spectacular."
5. **Salinas R.** — "Frank and Bryant took the time to show me how the design would look and I decided to move forward. The space now feels bright and spacious. Their work is solid and incredible."

**Design spec:**
- Dark background (`#0C1117` or `--coal`) — this makes it a dark section
- Section title: "What Our Customers Say" (Playfair Display)
- 5 cards in a responsive horizontal scroll or 3+2 grid
- Each card: reviewer name, ★★★★★, quote text, optional service type label
- Platform badge (Yelp / Google — check which platform these are from, or just show stars)
- Fits the light → dark alternating pattern as the section right before the gradient CTA

**Pages to add it to (start here):**
- `services.html` — before CTA strip
- `commercial.html` — before CTA strip
- `index.html` — check if already has reviews section; if so, make sure it matches the dark bg pattern

### 2. Light/Dark Alternating Section Pattern (ONGOING)

User wants: light → dark → light → dark → [dark testimonials] → [gradient CTA] → footer (dark)

Key pages to audit and fix section ordering:
- `services.html`
- `commercial.html`
- `index.html`
- Service-specific pages (shower-glass, window-repair, storefront-glass, etc.)

### 3. Case Studies Re-launch (WHEN READY)

When user has real project photos:
1. Remove `<meta name="robots" content="noindex, follow" />` from `case-studies.html` and all 5 `case-studies/*.html`
2. Add back nav link: `<li><a href="/case-studies">Case Studies</a></li>` to Commercial dropdown in all files
3. Replace placeholder content/images with real photos

### 4. .gitignore Cleanup

Batch scripts and NEXT-SESSION-PROMPT.md were accidentally committed. Add to `.gitignore`:
```
batch_*.py
generate_*.py
fix_*.py
NEXT-SESSION-PROMPT.md
*.py
```
Or at minimum the specific script names. This is minor but clean.

### 5. Other Ideas (Lower Priority)

- **Stats/trust bar** — "Since 2003 · 1,000+ Projects · 4.8★ Yelp · C-17 Licensed · Same-Day Available" — good as a thin strip between hero and first content section
- **FAQ accordion** on services pages — common questions (How long does installation take? Do you offer warranties? Are you licensed and insured?)
- **Process steps section** — already exists on some pages; ensure it's on all main service pages

## Gallery Technical Details

- Commercial page: `#gs-gallery-strip` + `#gs-lightbox`, images 71,7,15,8,20,35,56 (duplicated for loop), 30s/cycle
- Services page: `#svc-gallery-strip` + `#svc-lightbox`, all 74 images shuffled [66,19,37,9,8,59,71,60,44,40,16,65,57,31,53,30,49,52,67,20,21,41,51,3,56,64,54,50,24,58,26,17,34,23,48,25,63,7,43,62,10,47,22,28,11,1,69,38,70,61,27,35,45,42,46,13,72,2,39,33,74,68,6,73,5,55,12,14,18,29,32,36,4,15], 90s/cycle
- Hover pauses animation (`animation-play-state: paused`)
- Seamless loop via `translateX(-50%)` with duplicated image set

## Technical Notes

- Always use **Python batch scripts** for changes touching many files
- Run dry-run count before writing changes
- Batch scripts go in `/Users/kel/Documents/projects/american-glass-experts/` (add to .gitignore)
- After all changes: `git add` specific files, commit, `git push origin main`
- Cloudflare Pages deploys automatically — no manual step needed
- Clean URLs: `.html` stripped by Cloudflare Worker
