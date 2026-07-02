# Commercial SEO Audit & Action Plan — americanglassexperts.us
*Generated: 2026-07-02 | Data: GSC (service account, through Jun 29), URL Inspection (305 URLs), PageSpeed Insights, local-SEO agent audit*

Goal: grow COMMERCIAL clients (storefronts, offices, property managers, board-up).

---

## Site Status Snapshot (vs May 23 baseline)

| Metric | May 23 | Jun 29 | Trend |
|---|---|---|---|
| Pages with impressions (28d) | ~small | 330 | ↑↑ |
| Impressions (28d) | — | 20,642 | ↑↑ |
| Clicks (28d) | — | 117 | ↑ |
| Indexed (of 305 sitemap URLs) | 0 credited | 251 (82%) | ↑↑ |
| Organic sessions/day | 3.4 | growing | ↑ |
| PSI mobile (home / commercial hub) | — | 79 / 87 | OK |
| PSI desktop | — | 96 / 99 | Good |

Site is being indexed and gaining impressions fast. CTR is the weak point (~0.5%) — lots of page-2 rankings.

---

## THE core commercial problem (data)

**37 of the 54 non-indexed URLs are commercial pages** — including the four nav-linked
commercial service pages (`/commercial/window-repair`, `/commercial/sliding-window-repair`,
`/commercial/custom-mirrors`, `/commercial/emergency-glass`) and ~33 `/commercial/{city}`
pages (northridge, studio-city, tarzana, ventura, oxnard, west-hollywood, torrance…).
Mostly "Discovered – currently not indexed" = Google knows them but doesn't consider them
worth crawling. Root causes: nav-only internal links + ~85% template similarity across the
138 commercial city pages (word-level diff, measured).

Commercial queries already show demand (28d): 296 commercial-intent queries, 1,873
impressions, only 6 clicks. Striking distance (pos 4–20):

| Query | Imp | Pos |
|---|---|---|
| glass shop near me | 64 | 8.4 |
| commercial door glass corona ca | 35 | 10.7 |
| commercial window glass corona ca | 35 | 14.7 |
| commercial glass repair | 23 | 13.6 |
| local glass shop | 22 | 11.5 |
| commercial glass door replacement near me | 20 | 4.3 |
| storefront glass repair santa clarita | 20 | 10.8 |
| commercial glass contractors ventura | 19 | 16.3 |
| commercial glass repair los angeles | 18 | 18.7 |
| aluminum storefront repair san fernando valley | 17 | 9.9 (1 click) |

Also: "storefront glass" shows position 1.0 (55 imp, 0 clicks) — likely image/local-pack
placement; and "commercial glass contractor los angeles" at 24.6.

---

## FIXED THIS SESSION (2026-07-02, in this commit)

1. **`/commercial-glass` orphan duplicate killed** — page deleted, 301 → `/commercial` added
   to `_redirects`, removed from sitemap, its two strong B2B sections (What C-17 Licensing
   Means / Code Compliance & Safety Glass) merged into `commercial.html`, and all 138
   `href="/commercial-glass"` links in `commercial/*.html` repointed to `/commercial`.
2. **138 residential→commercial cross-links added** — every residential city page now has a
   contextual "commercial glass services in {City}" link above the contact strip. This is the
   direct fix for "Discovered – not indexed": contextual links from already-indexed pages.
   (Commercial→residential links already existed.)
3. **Case studies re-indexed** — removed `noindex` from `case-studies.html` + all 5 case
   studies (4 are commercial: office partitions Burbank, restaurant storefront SFV, retail
   Glendale, board-up Koreatown). Added all 6 URLs to sitemap. Added a 4-card "How We Handle
   Commercial Jobs" case-study section to `commercial.html`.
   *Note: these were noindexed intentionally in May — revert if that was for a reason beyond thin content; word counts are ~480–510 each.*
4. **commercial.html schema upgraded** — Service now references canonical `#business` @id,
   structured `areaServed` (4 counties), `hasOfferCatalog` with 5 commercial services.
5. **Commercial reviews surfaced** — swapped 3 residential review cards on `commercial.html`
   for the commercial ones from reviews.json (Jesus R. office partitions, Salinas R.
   partitions, Elise Z. tenant work). `diversify_reviews.py` now excludes commercial.html.
6. **GBP added to sameAs** on homepage schema (`maps.google.com/?cid=12823616644875683456`).
7. **Homepage title retargeted** — "Glass Shop & Glass Repair Los Angeles | American Glass
   Experts" (targets the "glass shop near me / local glass shop" cluster at pos 8–12).
8. **Contact form commercial lane** — picking "Commercial" now shows COI / CSLB / account
   program note.

After push: resubmit sitemap in GSC, then request indexing manually for `/commercial`,
the 4 commercial service pages, and the top ~10 commercial city pages (URL Inspection →
Request Indexing). Run `ping-indexnow.sh` for Bing.

---

## STILL OPEN — priority order

### Critical (off-site, can't script)
1. **BBB listing is WRONG and live** (re-confirmed 2026-07-02): shows 1112 Richardson Ave,
   Simi Valley + phone (818) 426-4649. Both wrong. No correct BBB listing exists. Dispute or
   claim at bbb.org — highest-authority citation actively contradicting NAP.
2. **GBP for commercial**: keep primary category as-is (residential calls work); add
   secondary categories (Glass & mirror shop, Window installation service, Commercial glass
   if available). Add GBP Products/Services entries mirroring commercial.html service names
   (Storefront Glass Replacement, Emergency Board-Up, Office Partition Glass…). Weekly GBP
   posts featuring commercial job photos. Ask EVERY commercial client for a review.
3. **Google LSA (Local Services Ads / Google Guaranteed)** — check category availability for
   glaziers in LA/Ventura/SB/Riverside. CSLB #1125850 + insurance already satisfies the
   vetting bottleneck. If available: fastest paid path to commercial leads.

### High
4. **Commercial city page uniqueness** — 85% template similarity across 138 pages = doorway
   risk (and the likely reason 33 city pages sit un-indexed). De-template the top 15 metros
   first (LA, Long Beach, Glendale, Burbank, Pasadena, Torrance, Ventura, Oxnard,
   Riverside, San Bernardino…): name real business districts, property types, recent-work
   references, city permit notes. Target <70% similarity.
5. **Citations**: claim Bing Places (feeds ChatGPT/Copilot), Apple Business Connect, then
   Angi/Houzz/Thumbtack/Nextdoor/BuildZoom. Nextdoor + Houzz most commercial-relevant.
6. **Commercial FAQ block on commercial.html** — COI limits, net-30 terms, W-9, licensing
   verification, turnaround, after-hours work. Add "Net-30 available / W-9 on file" language
   (currently absent everywhere; procurement people search for it).

### Medium
7. Corona cluster (70 imp, pos 10–15): beef `/commercial/corona` content + internal links.
8. Blog: only 2/6 posts commercial. Add: "glass partition cost LA", "property manager's
   board-up guide", "ADA storefront glass compliance CA".
9. Fix OAuth for seo skill Google APIs (`python3 ~/.claude/skills/seo/scripts/google_auth.py --auth`)
   — token refresh is dead; this session pulled GSC via gsc-index-monitor's service account instead.
10. Homepage mobile LCP 4.4s (lab) — preload hero image.

### Ignore
- Central Valley queries (Stockton/Wasco/Delano/Taft) — outside service area.
- CrUX field data absent — traffic still too low, revisit at ~50+ clicks/day.
