# Next Session Handoff — American Glass Experts

## Site Context

- **URL:** https://www.americanglassexperts.us
- **Repo:** https://github.com/ktorres0109/american-glass-experts (Cloudflare Pages auto-deploys on push to `main`)
- **Stack:** Static HTML (336 files), no framework. All CSS inline per file. Clean URLs via Cloudflare Worker (strips `.html`).
- **CSS design tokens:** `--blue: #2563eb`, `--charcoal: #1e293b`, `--head: Playfair Display`, `--body: DM Sans`
- **Business:** Licensed glass contractor (C-17, CSLB #1125850), Southern California. Residential + Commercial.
- **Working dir:** `/Users/kel/Documents/projects/american-glass-experts/`

## What Was Done (Previous Sessions)

1. Full nav updated across all 336 pages: split into **Residential ▾** / **Commercial ▾** dropdowns.
2. New `/commercial` landing page (`commercial.html`) created — hero, services, industries, county-based city links.
3. `service-areas.html` updated with Residential/Commercial audience toggle.
4. `index.html` updated with commercial highlight strip and footer commercial column.
5. Footer across all pages now has: Residential col, Commercial col, Company col.
6. Footer-bottom row: `© 2026 American Glass Experts Inc. · C-17 Licensed · CSLB #1125850` + Sitemap + Service Areas links.
7. All 138 commercial city pages (`/commercial-glass-[city]`) were in the repo before this session; they now have the updated nav/footer.
8. `privacy-policy.html` already exists in the repo (content unknown — read it before editing).
9. **No `terms-of-service.html` exists yet.**

## Tasks for This Session

### 1. Terms of Service + Privacy Policy Pages

**Goal:** Create `terms-of-service.html` and ensure `privacy-policy.html` is complete and accurate. Then add both links to the footer of every page.

**Details:**
- Business name: **American Glass Experts Inc.**
- License: C-17 Glazing Contractor, CSLB #1125850
- Service area: Southern California (Los Angeles, Ventura, San Bernardino, Riverside counties + Coachella Valley)
- Services: Residential glass (shower enclosures, window repair, mirrors, emergency glass), Commercial glass (storefronts, partitions, entry systems)
- Contact email: use whatever is in the existing pages (check `about.html` or `index.html`)
- Terms should cover: scope of services, quote/estimate process, payment terms, warranty/workmanship, limitation of liability, governing law (California)
- Privacy Policy should cover: what info is collected (name, phone, email via quote form), how it's used, no sale of data, California privacy rights (CCPA), contact info

**Footer change needed (all 336 files):**
Current footer-bottom row:
```html
<div style="display:flex;gap:20px;"><a href="sitemap.xml">Sitemap</a><a href="/service-areas">Service Areas</a></div>
```
Change to:
```html
<div style="display:flex;gap:20px;"><a href="/terms-of-service">Terms</a><a href="/privacy-policy">Privacy</a><a href="sitemap.xml">Sitemap</a><a href="/service-areas">Service Areas</a></div>
```

Use Python batch script to make this replacement across all 336 files reliably (not sed — previous sessions showed Python handles the variants better). Check how many files match before and after.

**Style for new legal pages:** Match existing site aesthetic. Use `storefront-glass.html` or `about.html` as CSS/nav template. Simple single-column layout, readable line-length (~70ch), section headings in Playfair Display, body in DM Sans. Nav should have neither Residential nor Commercial as active. No modal/quote widget needed on these pages.

---

### 2. Case Studies Section (New Feature)

**Reference:** Competitor site LA Glass Company (laglass.com) has a "Case Studies" dropdown under "Project Gallery" in nav. Examples observed:
- Storefront Glass Repair for specific client types (restaurants, offices, retail)
- Interior Business Glass Services
- Emergency Board-Ups

**Goal:** Create a `/case-studies` hub page + 3–5 individual case study pages that showcase real project types American Glass Experts handles.

**Proposed case studies (fabricate realistic but truthful-sounding examples — no fake client names, just project descriptions):**
1. `case-studies/restaurant-storefront-glass-los-angeles.html` — Replace shattered storefront for a San Fernando Valley restaurant, same-day emergency response
2. `case-studies/office-glass-partitions-burbank.html` — Open-plan office in Burbank converted with frameless glass partitions
3. `case-studies/custom-shower-enclosure-calabasas.html` — Frameless custom shower for residential remodel in Calabasas
4. `case-studies/retail-storefront-upgrade-glendale.html` — Retail storefront glass upgrade in Glendale, improved curb appeal + security
5. `case-studies/emergency-board-up-los-angeles.html` — Emergency glass board-up after break-in, overnight response

**Case study page structure (per page):**
- Hero: Project title + location + 1-line summary
- Meta strip: Service type | Location | Timeline | Outcome
- Problem / Solution / Result sections (3-paragraph narrative)
- Trust signals: C-17 Licensed badge, "Same-Day Available" if applicable
- Related services links
- CTA strip: "Have a Similar Project? Get a Free Quote"

**Hub page `/case-studies`:**
- Grid of case study cards (title, service type badge, 1-sentence summary, "Read More" link)
- Intro: "Real projects. Real results. Serving Southern California since [year from about.html]."
- Link from nav: Add "Case Studies" to the Commercial ▾ dropdown (makes sense — commercial buyers want proof of work)
  - Also link from the main nav "Projects" or as a sub-item if there's already a gallery link

**Nav addition needed:** In the Commercial ▾ dropdown (currently has: Commercial Overview, Storefront Glass, Commercial Areas), add:
```html
<li><a href="/case-studies">Case Studies</a></li>
```
This needs to be added to all 336 files via batch script.

---

## Technical Notes

- Always use **Python batch scripts** for changes that touch many files — sed/awk missed variants in previous sessions
- Always run a dry-run count (how many files matched) before writing changes
- **Do not commit** `generate_all_new_pages.py`, `fix_template_errors.py`, `generated_meta_descriptions.json`, or any `* 2.html` files — they're in `.gitignore` now
- After all changes: `git add` specific files/dirs, commit, `git push origin main`
- Cloudflare Pages deploys automatically on push — no manual deploy needed
- Clean URLs: `terms-of-service.html` → `/terms-of-service`, `privacy-policy.html` → `/privacy-policy`, `case-studies/index.html` OR `case-studies.html` → `/case-studies`

## File Reading Priority

Before starting, read these files to understand current state:
1. `index.html` — for nav/footer exact HTML patterns (find footer-bottom div and all nav dropdown HTML)
2. `privacy-policy.html` — check what content already exists
3. `about.html` — find contact email, founding year, any other business details to use in legal pages
4. `commercial.html` — use as CSS/structure reference for new pages (it was just created and is the most up-to-date template)

## Commit Message Style

```
Add Terms of Service, Privacy Policy, case studies; footer legal links across all pages

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```
