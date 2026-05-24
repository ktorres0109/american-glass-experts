# American Glass Experts — Session Handoff Prompt
*Last updated: 2026-05-23 — SEO session (Google APIs setup + schema fix)*

---

## SEO Next Session — Start Here

Read `SEO-PRIORITY-ACTIONS.md` for full priority queue. Quick summary:

1. **Fix BBB NAP** (wrong address/phone, DA 91) — manual task on bbb.org

### Google APIs (all configured)
Config: `~/.config/claude-seo/google-api.json`
OAuth token: `~/.config/claude-seo/oauth-token.json`
Client secret: `/Users/kel/client_secret_555656842247-nnqkoqk79m5jdqf2qed14eeg4i2t0o2f.apps.googleusercontent.com.json`

```bash
# Verify credentials
cd /Users/kel/.claude/skills/seo && .venv/bin/python scripts/google_auth.py --check

# Full Google SEO run
# /seo google https://www.americanglassexperts.us

# GSC data
cd /Users/kel/.claude/skills/seo && .venv/bin/python scripts/gsc_query.py --property "sc-domain:americanglassexperts.us" --json

# GA4 organic traffic
cd /Users/kel/.claude/skills/seo && .venv/bin/python scripts/ga4_report.py --property "properties/534586830" --json
```

### What was done 2026-05-23
- Schema: removed incomplete LocalBusiness inline from provider in all 138 commercial-glass-*.html → pushed
- Google APIs: fully configured Tier 2 (GSC, Indexing, GA4, Ads)
- First data pull: 88 organic sessions in 28d, sitemap 297 submitted/0 indexed, homepage indexed + rich results passing

---

# American Glass Experts — Original Design Handoff Prompt

## Project
- **URL:** https://www.americanglassexperts.us
- **Repo:** https://github.com/ktorres0109/american-glass-experts (Cloudflare Pages, auto-deploys on push to `main`)
- **Stack:** 307 static HTML files, no framework. All CSS inline per file.
- **Clean URLs:** Cloudflare Worker strips `.html`
- **Working dir:** `/Users/kel/Documents/projects/american-glass-experts/`
- **File layout:** Root `.html` + `commercial-glass-{city}.html` (130+) + `{city}.html` (138) + `blog/*.html` + `case-studies/*.html`
- **Business:** Licensed glass contractor — C-17, CSLB #1125850. Southern California. Founded 2003.
- **Phone:** (805) 750-6471 | **Address:** 6853 Reseda Blvd, Reseda, CA 91335

---

## EXACT Design Tokens (use these values, never guess)

```css
/* Light mode (:root) */
--blue:      #4a90d9;
--blue-dk:   #3a7bc8;
--blue-lt:   #6aaee8;
--blue-dim:  rgba(74,144,217,0.08);
--blue-glow: rgba(74,144,217,0.22);
--coal:      #0f172a;
--charcoal:  #1e293b;

/* Dark mode ([data-theme="dark"]) */
--blue:      #4a90d9;   /* same in both modes now */
--blue-dk:   #3a7bc8;
--blue-lt:   #6aaee8;
--coal:      #f0f4f8;   /* flips in dark — do NOT use for backgrounds */
--charcoal:  #e2eaf4;   /* flips in dark — do NOT use for dark backgrounds */
```

**Dark mode warning:** `--charcoal` flips to near-white in dark mode. Never use `var(--charcoal)` as a section background. Hardcode values instead.

---

## All Changes Made This Session (DO NOT redo)

### ✅ 1. Footer background — solid `#0c1117` both modes (294 pages)
```css
.footer { background: #0c1117; color: rgba(255,255,255,0.55); padding: 72px 0 36px; }
[data-theme="dark"] .footer { background: #0c1117; }
```

### ✅ 2. Contact strip gradient above footer — all 306 pages
Section: `<section class="contact-strip">` directly before `<footer`.
**EXACT CSS that must be in every page:**
```css
.contact-strip {
  background: linear-gradient(180deg, #1a2535 0%, #0d1117 100%);
  padding: 96px 0; text-align: center;
  position: relative; overflow: hidden;
}
[data-theme="dark"] .contact-strip {
  background: linear-gradient(180deg, #1a2535 0%, #0d1117 100%);
}
.contact-strip::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse at 50% 0%, rgba(74,144,217,0.22) 0%, transparent 65%);
  pointer-events: none;
}
.contact-strip h2 { color: #fff; margin-bottom: 12px; }
[data-theme="dark"] .contact-strip h2 { color: var(--white); }
.contact-strip-sub { font-size: 1rem; color: rgba(255,255,255,0.55); margin-bottom: 44px; }
[data-theme="dark"] .contact-strip-sub { color: var(--text-mid); }
.contact-actions { position: relative; z-index: 1; display: flex; flex-direction: column; align-items: center; gap: 18px; }
.contact-actions-main { display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; }
```

### ✅ 3. Blue accent — `#4a90d9` everywhere (297 pages)
Old `#2563eb` / `#1d4ed8` / `#3b82f6` fully replaced. Buttons use `var(--blue)`.

### ✅ 4. Nav logo
- `height: 48px` (was 40px), `gap: 6px` (was 10px)
- `logo-icon-dark.webp` = dark icon on transparent bg (light mode)
- `logo-icon.webp` = white icon on transparent bg (dark mode)
- Favicon: `logo-icon-dark.png` = transparent bg

### ✅ 5. Removed `cta-band` sections (153 pages)
Old `<section class="cta-band">` was a duplicate CTA. All removed. No page should have `cta-band` anymore.

### ✅ 6. Homepage footer/contact-strip fixed
Both were light-colored. Now dark and matching all other pages.

---

## Known Remaining Issues — Fix These

### 🔴 `review.html` — missing contact-strip HTML
Only page (out of 307) that still has no `class="contact-strip"`. Add section before `<footer`.

### 🔴 Verify ALL 307 pages with Python — use `glob` not shell loops

**ALWAYS scan with:**
```python
import glob
all_files = list(set(
    glob.glob("/Users/kel/Documents/projects/american-glass-experts/*.html") +
    glob.glob("/Users/kel/Documents/projects/american-glass-experts/**/*.html", recursive=True)
))
```

**Run these 7 checks and fix anything found:**

1. **Missing contact-strip HTML** — `class="contact-strip"` not in file
2. **Old blue color** — `#2563eb` or `#1d4ed8` still present
3. **Wrong footer bg** — `.footer {` contains `var(--coal)` or `#060a10`
4. **cta-band remnants** — `class="cta-band"` still present anywhere
5. **Duplicate contact strips** — `class="contact-strip"` appears more than once
6. **Wrong contact-strip bg** — `.contact-strip {` has `var(--charcoal)` instead of gradient
7. **Wrong dark override** — `[data-theme="dark"] .contact-strip {` has `var(--bg-soft)` instead of gradient

---

## Workflow Rules
- Use Python batch scripts for multi-file changes — print count before writing
- After changes: `git add -A && git commit -m "..." && git push origin main`
- Always use absolute paths
- Cloudflare auto-deploys on push to `main`

---

## Other Site Context

### Nav structure
Residential ▾ / Commercial ▾ dropdowns. Theme toggle + "Call Now" + "Get a Free Quote" buttons.

### Reviews (same 6 on all pages)
Alexis M. / Jesus S. / Joshua B. / Mercy R. / Dylan N. / Lisandro O. — all 5★ real Yelp reviews.

### Case studies (on hold)
noindex on `case-studies.html` + 5 sub-pages. Removed from nav. Re-enable when real photos ready.

### Gallery
- Commercial: `#gs-gallery-strip` + `#gs-lightbox`, images 71,7,15,8,20,35,56
- Services: `#svc-gallery-strip` + `#svc-lightbox`, all 74 images shuffled
- CDN: `https://pub-b4878fccfc85401e99bc2b4eff65255a.r2.dev/gallery/{n}.jpg`
