# Full SEO Audit — American Glass Experts Inc.
**Domain:** americanglassexperts.us
**Audit Date:** 2026-04-30
**Business Type:** Hybrid SAB (Service-Area Business) — Glass Repair & Installation Contractor
**License:** C-17 Glazing Contractor, CSLB #1125850
**Location:** 6933 Reseda Blvd Unit J, Reseda, CA 91335

---

## SEO Health Score: 65 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 68 | 15.0 |
| Content Quality | 23% | 62 | 14.3 |
| On-Page SEO | 20% | 55 | 11.0 |
| Schema / Structured Data | 10% | 74 | 7.4 |
| Performance (CWV) | 10% | 72 | 7.2 |
| AI Search Readiness | 10% | 74 | 7.4 |
| Images | 5% | 58 | 2.9 |
| **TOTAL** | | | **65.2** |

> The site is technically sound and above average for a local contractor. Static HTML on Cloudflare is a real performance/crawlability advantage. Primary gaps: 131 identical meta descriptions, a critical BBB NAP conflict, only 17 Google reviews (likely stale), generic author entity in blog schema, and no YouTube presence.

---

## Top 5 Critical Issues

1. **BBB listing has wrong address + wrong phone** — DA 91 citation actively suppressing local authority
2. **131 city pages share identical meta description template** — GSC duplicate meta flag on every city page
3. **17 Google reviews, most recent in schema dated Sept 2024** — review velocity cliff risk
4. **Blog author schema says "American Glass Experts Team"** but byline says "Frank, Lead Glazier" — E-E-A-T mismatch on all 6 posts
5. **No YouTube presence** — highest single unaddressed AI citation signal gap (0.737 correlation)

## Top 5 Quick Wins

1. Fix copyright footer: `© 2025` → `© 2026` — 1-line edit across all pages
2. Fix blog author schema: change `"name": "American Glass Experts Team"` → `{"@type": "Person", "name": "Frank Salinas", "jobTitle": "Lead Glazier", "url": "/about#frank"}` on all 6 posts
3. Add `"logo"` property to homepage schema (rename `"image"` key) — 2-line edit
4. Add `"foundingDate": "2003"` to homepage LocalBusiness schema — 1-line edit
5. Add Google Maps embed to homepage — 15 mins

---

## 1. Technical SEO

**Score: 68/100**

### Canonical & URL Structure
- Service pages use self-referential canonicals (no trailing slash). ✓
- City pages use extensionless canonical `/hemet` — consistent with Cloudflare Pages `.html` stripping. ✓
- GSC "Page with redirect" entries (temecula.html → /temecula) are **expected behavior**, not errors.
- No canonical/breadcrumb trailing slash conflicts detected.

### robots.txt
- Blocks training crawlers (CCBot, anthropic-ai, cohere-ai). Allows GPTBot, Google-Extended, Googlebot. ✓
- Sitemap declared. ✓
- **Low:** ClaudeBot and PerplexityBot not explicitly listed — covered by wildcard but Cloudflare bot management may challenge independently. Add explicit `Allow: /` entries.

### Sitemap
- 262 URLs, single file. Blog posts and service pages included. ✓
- Priority values set appropriately. ✓

### HTTPS & Security
- HTTP→HTTPS and non-www→www both operational via Cloudflare. ✓
- No custom CSP/X-Frame-Options in HTML — relies on Cloudflare defaults (acceptable for static site).

### Indexability Issues
- **4 pages "Crawled - currently not indexed"** (hemet, wildomar, lake-elsinore, baldwin-park): near-duplicate content root cause. Content diversification deployed 2026-04-30 — monitor GSC over next 2–4 weeks.

| Issue | Severity | Effort |
|---|---|---|
| 4 city pages not indexed (fix deployed) | High | Done |
| No Maps embed on homepage / city pages | High | 1 hr |
| ClaudeBot/PerplexityBot not explicit in robots.txt | Low | 15 min |
| Copyright footer © 2025 (stale) | Low | 5 min |

---

## 2. Content Quality & E-E-A-T

**Score: 62/100**

### Service Pages
- 2,200–3,200 words each. Comprehensive. Unique meta descriptions. Not thin. ✓
- Strong topical depth: process steps, FAQ, pricing context, service area listings.

### City Pages (131 pages)
- Deep content diversification deployed 2026-04-30 (unique hero, neighborhoods, about-city card, FAQ Q7 per city). ✓
- Approx 1,800–2,200 words per page after diversification. ✓
- **Critical:** All 131 share identical meta description template.
- **Medium:** Contact form placeholder phone is `(818) 555-0000` on all 133 pages — should be `(805) 750-6471`.

### Blog (6 posts)
- Visible byline: "By Frank, Lead Glazier · April 2026 · C-17 Licensed · CSLB #1125850" ✓
- Topical clustering (shower, window, storefront, emergency). ✓
- **Critical:** All 6 posts dated April 2026 — no content freshness diversity.
- **Critical:** Author in JSON-LD schema = `"American Glass Experts Team"` — mismatches byline "Frank, Lead Glazier".
- **Medium:** Body paragraphs 80–130 words vs 134–167 AI citation optimal range.
- **Medium:** No internal links from blog posts to city pages, or city pages to blog posts.

### About Page
- License, 20+ years experience, 1000+ jobs, CSLB verification. ✓
- "Frank, Lead Glazier" referenced in blog but not on About page — no `#frank` anchor or bio.
- ~1,100 words — adequate but not deep.

### E-E-A-T

| Signal | Status |
|---|---|
| License number displayed + verifiable | ✓ Strong |
| Named expert with credentials | Partial — "Frank" in blog only |
| Years of experience | ✓ "20+ years" |
| Project count | ✓ "1,000+ jobs" |
| Author schema matches byline | ✗ Mismatch |
| Team bios/photos | ✗ Missing |
| Case studies / portfolio | Partial — gallery, no case study format |

---

## 3. On-Page SEO

**Score: 55/100**

### Title Tags
- All page types: keyword-forward, include location. ✓
- Blog posts: conversational natural-language questions with year. ✓

### Meta Descriptions

| Page Type | Status |
|---|---|
| Homepage | ✓ Present (156 chars) |
| Service pages | ✓ Present, unique per page |
| Blog posts | ✓ Present, unique |
| **City pages (131)** | ✗ All identical template |

### Heading Structure
- Service pages: logical H1→H2→H3 hierarchy. ✓
- City pages: multiple H2s with near-duplicate text ("What We Do in X" + "Glass Services Available in X") — redundant, consider consolidating.
- Blog: H1 is natural-language question — strong for AI query matching. ✓

### Internal Linking
- Hub-and-spoke: service-areas → city pages → adjacent cities → service-areas. ✓
- Service pages ↔ city pages. ✓
- **Medium:** Blog posts do not link to city pages. City pages do not link to blog posts.

| Issue | Severity | Pages Affected |
|---|---|---|
| Identical meta descriptions | Critical | 131 city pages |
| Placeholder phone `(818) 555-0000` in forms | Medium | 133 pages |
| Blog ↔ city page cross-links missing | Medium | 137 pages |
| Redundant H2 headings on city pages | Low | 131 city pages |

---

## 4. Schema / Structured Data

**Score: 74/100**

### Homepage (HomeAndConstructionBusiness)
| Property | Status |
|---|---|
| @type: HomeAndConstructionBusiness | ✓ |
| hasCredential (C-17 CSLB) | ✓ Advanced — rare for contractors |
| aggregateRating (4.8/17) | ✓ |
| sameAs (Yelp + Google) | ✓ |
| geo (GeoCoordinates) | ✓ |
| FAQPage block | ✓ |
| **logo** (currently uses `image` key) | ✗ Rename to `logo` |
| **foundingDate** | ✗ Missing — add `"2003"` |
| **makesOffer / hasOfferCatalog** | ✗ Missing |

### Blog Post Schema
| Property | Status |
|---|---|
| Article @type | ✓ |
| datePublished | ✓ |
| FAQPage on cost guide | ✓ |
| **author: Person (not Org)** | ✗ Critical — all 6 posts wrong |
| dateModified | ✗ Only on 1 of 6 posts |
| ImageObject with caption | ✗ Missing |
| HowTo schema | ✗ Missing on process posts |

### City Pages
| Property | Status |
|---|---|
| Unique @id per page | ✓ |
| parentOrganization link | ✓ |
| City-specific geo | ✓ |
| FAQPage | ✓ |
| BreadcrumbList | ✓ |
| areaServed typed City objects | ✗ Flat string — upgrade |

| Fix | Severity | Effort |
|---|---|---|
| Blog author: Person entity on all 6 posts | Critical | 30 min |
| Add `logo` property to homepage schema | Low | 5 min |
| Add `foundingDate: "2003"` | Low | 5 min |
| Add `makesOffer` catalog to homepage | Medium | 1 hr |
| `HowTo` schema on process blog posts | Medium | 2 hrs |
| Upgrade `areaServed` to typed City objects | Low | 2 hrs |

---

## 5. Performance (CWV)

**Score: 72/100**

*Lab estimates only — CrUX field data not available.*

Static `.html` served via Cloudflare CDN is a **significant advantage** — full content in initial HTTP response, no hydration delay, no JS-blocking render path.

| Metric | Estimate | Basis |
|---|---|---|
| LCP | Good (<2.5s) | Static HTML + CDN + no JS blocking |
| CLS | Good (<0.1) | No late-loading layout elements |
| INP | Good (<200ms) | Minimal JS interactions |

- AVIF logo format. ✓
- FAQ accordion answers present in source HTML (not JS-injected) — crawlable. ✓
- Dark-mode localStorage script above body — negligible render impact.

**Recommendations:** Verify `loading="lazy"` on below-fold images; confirm Brotli compression on Cloudflare; consider hero image `<link rel="preload">`.

---

## 6. AI Search Readiness (GEO)

**Score: 74/100**

### Strengths
- **llms.txt present** with pricing data, FAQ pairs, business identity, page index. Above average for local contractor. ✓
- Static HTML — AI crawlers receive full content without JS. ✓
- FAQPage schema on service, city, and blog pages. ✓
- CSLB credential in structured data — machine-verifiable. ✓
- Specific pricing consistent across llms.txt and blog posts. ✓

### Gaps
| Gap | Priority |
|---|---|
| No YouTube channel (0.737 AI citation correlation) | High |
| Blog author schema mismatch — weakens E-E-A-T for AI | High |
| Blog body paragraphs short for AI citation (80–130 vs 134–167 words) | Medium |
| No Reddit presence | Medium |
| No Wikidata entity | Low |
| Copyright © 2025 contradicts 2026 blog dates | Low |

### Platform Scores
| Platform | Score |
|---|---|
| Google AIO | 72/100 |
| ChatGPT | 76/100 |
| Perplexity | 78/100 |
| Bing Copilot | 70/100 |
| Claude | 74/100 |

---

## 7. Local SEO

**Score: 61/100**

### NAP Consistency

| Source | Address | Phone | Status |
|---|---|---|---|
| Website (all pages) | 6933 Reseda Blvd Unit J, Reseda CA 91335 | (805) 750-6471 | ✓ |
| Homepage JSON-LD | 6933 Reseda Blvd Unit J, Reseda, CA 91335 | +1-805-750-6471 | ✓ |
| **BBB** | **1112 Richardson Ave, Simi Valley CA 93065** | **(818) 426-4649** | ✗ CRITICAL |

### Reviews
- 17 reviews, 4.8★ (schema data)
- Most recent review in schema: September 2024 (7+ months ago)
- 17 reviews is critically low for 4-county market — competitors likely 50–200+
- Review funnel page exists (review.html, noindexed) ✓ — needs active promotion

### GBP
| Signal | Status |
|---|---|
| Profile exists | Detected via sameAs |
| Maps embed — homepage | ✗ Missing |
| Maps embed — city pages | ✗ Missing on all 130+ |
| Primary category | Unknown — verify "Glass repair service" |
| Secondary categories | Unknown — add Mirror shop, Shower door shop |

### Citation Presence
| Directory | DA | Status |
|---|---|---|
| Google Business Profile | 100 | Detected — verify live |
| Yelp | 94 | Present — verify NAP (403 blocked) |
| BBB | 91 | ✗ Wrong NAP |
| Angi, HomeAdvisor, Houzz, Thumbtack | 68–79 | Not detected |
| Bing Places, Apple Maps, Nextdoor | 58–62 | Not detected |

---

## 8. Images

**Score: 58/100**

- Logo: AVIF format. ✓
- OG image on blog post: correct 1200×630 dimensions. ✓
- Alt text present on key images. ✓
- **Gap:** No `ImageObject` schema with `caption`/`description` on blog images.
- **Gap:** Gallery page image alt text not verified.
- **Gap:** No WebP/AVIF confirmed on city page body images.

---

## 9. Backlinks

*No API credentials — no measured data.*

| Source | DA | Status |
|---|---|---|
| Google Business Profile | 100 | sameAs declared |
| Yelp | 94 | sameAs declared |
| BBB | 91 | ✗ Wrong NAP |

Estimated DA range: **10–18** (typical for local contractor at this stage).

Top link building priorities: Fix BBB → Angi → Houzz → Bing Places → Thumbtack → YouTube channel → local chamber.

---

## Data Gaps

| Gap | How to Fill |
|---|---|
| CrUX field CWV data | Configure Google API (GSC + CrUX) |
| Live GBP data (reviews, category, photos) | Manual GBP dashboard review |
| DA, referring domains, anchor text | Moz API or Ahrefs |
| Yelp NAP verification | Manual visit to Yelp listing |
| Live SERP rank tracking | DataForSEO or Semrush |
