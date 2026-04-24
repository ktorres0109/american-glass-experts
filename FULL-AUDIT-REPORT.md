# Full SEO Audit — American Glass Experts
**URL:** https://www.americanglassexperts.us  
**Audit Date:** 2026-04-23  
**Business Type:** Service Area Business (SAB) — C-17 Glazing Contractor  
**Market:** Southern California (LA, Ventura, San Bernardino, Riverside Counties)

---

## Overall SEO Health Score: 61 / 100

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 22% | 68 | 15.0 |
| Content Quality | 23% | 52 | 12.0 |
| On-Page SEO | 20% | 60 | 12.0 |
| Schema / Structured Data | 10% | 58 | 5.8 |
| Performance (CWV) | 10% | 72 | 7.2 |
| AI Search Readiness | 10% | 64 | 6.4 |
| Images | 5% | 55 | 2.8 |
| **Total** | | | **61.2 / 100** |

---

## Top 5 Critical Issues

1. **BBB citation conflict** — Tier 1 directory (DA 91) lists wrong address (Simi Valley vs Reseda), wrong phone (818 vs 805), wrong category (Landscaping). Actively suppresses local authority.
2. **Blog Article schema blocks rich results** — All 6 blog posts missing required `image` (ImageObject) and `dateModified`. Google will not show Article rich results for any post until fixed.
3. **City page LocalBusiness schema is disconnected** — 145 city pages have bare `LocalBusiness` with no `@id`, no `geo`, no `aggregateRating`, no `sameAs`. These entities float disconnected from the homepage entity graph.
4. **No GBP signals on-site** — No Maps embed, no Place ID link, no "Leave a Google review" CTA anywhere on site. GBP is the #1 local pack ranking factor per Whitespark 2026.
5. **126 pages discovered-not-indexed** — Google has found but not crawled most city pages. Sitemap duplication (now fixed) was contributing. Continue 10/day manual URL inspection in GSC.

## Top 5 Quick Wins

1. Add `image` (ImageObject) + `dateModified` to all 6 blog Article schemas → unblocks Article rich results immediately
2. Add `image` to homepage `HomeAndConstructionBusiness` schema → unblocks Knowledge Panel photo
3. Fix robots.txt to technically block training crawlers (10 min change)
4. Update `llms.txt` with `# License`, `# Pricing`, `# FAQ` blocks → increases AI Overview citation probability
5. Claim/correct BBB listing (wrong address, category, phone)

---

## Technical SEO

### Crawlability
- **robots.txt**: `Allow: /` wildcard — all pages crawlable. Sitemap declared correctly.
- **Sitemap**: Fixed today. 151 unique URLs, zero duplicates (was 180 with 30 cities tripled). All `lastmod` updated to 2026-04-23.
- **Redirects**: `/*.html → /:splat 301` via Netlify `_redirects`. Clean URLs working correctly.
- **HTTPS**: Active, Cloudflare-managed. ✓

### Indexability Issues (from GSC)
| Issue | Count | Severity |
|---|---|---|
| Discovered – currently not indexed | 126 | High |
| Redirect error | 2 | High |
| Alternate page with proper canonical tag | 3 | Medium |
| Page with redirect | 1 | Low |

The 2 redirect errors and 3 alternate canonical pages need individual URL Inspection in GSC to identify exact URLs.

### Canonical Tags
- All pages use clean canonical URLs (no `.html`). ✓
- City page BreadcrumbList has trailing slash inconsistency: home item has `/` but city items don't. Should match canonical format.

### robots.txt Training Exclusion — NOT ENFORCED
Comments (`ai-train=no`) are not parsed by crawlers. CCBot, anthropic-ai, cohere-ai are currently allowed.

```
# Add these blocks to robots.txt:
User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: cohere-ai
Disallow: /
```

---

## Content Quality

### E-E-A-T Assessment
**Positive signals:**
- CSLB License #1125850 visible on multiple pages with verifier link to cslb.ca.gov — strong trust signal
- Named individuals (Frank, Bryant) on About page — experience signal
- Founding year 2003 on About page
- 4.8 star rating with Yelp/Google claims

**Gaps:**
- Blog posts have no named author bylines — only "American Glass Experts Inc." Google's E-E-A-T prefers named expert authors with credentials for service content
- No author bio pages linked from posts
- Review count not disclosed ("4.8 stars" with no number = unverifiable)

### City Pages — Doorway Page Risk: MEDIUM-HIGH
**145 city pages, 65–70% identical boilerplate content.**

Structure per page:
- 1 unique paragraph (~150 words): drive time, zip code, 2-3 neighborhood names, demographic sentence
- Same 6 service cards (identical copy)
- Same licensing block
- Same FAQ block (5 questions, same answers)
- Same contact form

At this level of template ratio, Google's Helpful Content system may classify these as doorway pages. Pages for competitive cities (Los Angeles, Riverside, Glendale, Corona) need substantially more unique content — minimum 400+ words covering local building types, permit context, common job scenarios.

**The Reseda home-base page is the weakest link.** It should be the strongest page (proximity guaranteed) but is structurally identical to a page for a city 55 miles away.

### Blog Posts
6 posts, range 850–1,950 words. Content quality is good. Issues:
- No FAQ sections on 4 of 6 posts (foggy window + shower door cost are the highest-value targets)
- No named author bylines
- No `dateModified` in schema
- Missing `image` in Article schema (blocks rich results)
- Pricing tables exist but not wrapped in structured data

### Meta Descriptions
Not confirmed on city pages. Service pages have them. All city pages need unique meta descriptions with city name + primary service + differentiator (C-17 licensed, same-day, free estimate).

---

## On-Page SEO

### Title Tags
- Homepage: ✓
- Service pages: ✓  
- City pages: Template "Glass Repair & Installation in [City], CA" — functional but doesn't include the brand differentiator (licensed C-17)
- Blog posts: ✓

### Heading Structure
- H1 present and unique per page ✓
- Heading hierarchy appears consistent ✓

### Internal Linking
- City pages link to 3–4 adjacent cities only
- City pages do NOT link to relevant service pages
- Service pages do NOT link to relevant city pages
- This creates an isolated crawl graph — service pages and city pages are not cross-linked

### Phone Number
- Uses 805 area code (Ventura County) with a Reseda (LA County) address
- Creates geographic signal confusion for LA County local pack
- Consider adding an 818/747 tracking number as primary for LA County searches

---

## Schema / Structured Data

### What's Implemented (from source files — confirmed live)
| Page Type | Schema Present |
|---|---|
| Homepage | `HomeAndConstructionBusiness`, `FAQPage`, `WebSite` |
| City pages (145) | `LocalBusiness`, `BreadcrumbList`, `FAQPage` |
| Services page | `WebPage`, `BreadcrumbList`, `FAQPage`, 5x `Service` |
| Blog posts (6) | `Article` (bare minimum) |

### Critical Schema Issues

**1. Homepage: Missing `image` on `HomeAndConstructionBusiness`**
Without `image`, Google cannot display business photo in Knowledge Panel or local pack.
```json
"image": {
  "@type": "ImageObject",
  "url": "https://www.americanglassexperts.us/og-image.jpg",
  "width": 1200,
  "height": 630
}
```

**2. Blog posts: Missing `image` + `dateModified` (blocks Article rich results)**
All 6 posts are currently ineligible for Article rich results.
```json
"image": { "@type": "ImageObject", "url": "...", "width": 1200, "height": 630 },
"dateModified": "2026-04-XX"
```

**3. City pages: Disconnected LocalBusiness entities**
145 pages each have a `LocalBusiness` with no `@id`, no `geo`, no `aggregateRating`. They don't link back to the homepage entity.
Add: `@id`, `geo`, `aggregateRating`, `sameAs`, `image`, `parentOrganization` pointing to `/#business`.

**4. Services page: 4 of 5 Service objects missing `offers`**
Only shower enclosures has price range. Window, storefront, emergency, mirrors missing it.

**5. BreadcrumbList trailing slash inconsistency**
Home item: `https://www.americanglassexperts.us/` (with slash)
City item: `https://www.americanglassexperts.us/los-angeles` (no slash)
Should be consistent with canonical.

---

## Performance

- **Hosting**: Netlify with Cloudflare CDN — strong baseline
- **Rendering**: Server-side rendered static HTML — fully crawlable without JS ✓
- **Images**: Logo uses `.avif` format ✓
- **Estimated CWV**: Good for a static Netlify site. Specific LCP/CLS/INP measurements require Lighthouse run (Chrome not installed in this environment)
- **TTFB**: Cloudflare edge caching — expected <200ms

No specific bottlenecks identified from source inspection. Run PageSpeed Insights for exact CWV scores.

---

## AI Search Readiness (GEO)

**Score: 64 / 100**

| Platform | Score |
|---|---|
| Google AI Overviews | 52/100 |
| ChatGPT | 61/100 |
| Perplexity | 68/100 |
| Bing Copilot | 55/100 |

### llms.txt: Present — Score 7/10
Strengths: CSLB license with verifier, service taxonomy, full service area, page index, contact block.

**Missing:**
```
# License
Content may be cited for search grounding and informational AI responses. Not licensed for AI training datasets.

# Pricing (approximate, 2026)
- Frameless shower door: $1,200–$4,500
- Foggy window / IGU replacement: $250–$850 per unit
- Emergency board-up: $100–$300
- Custom mirrors: custom quote

# FAQ
Q: Are you licensed to do glass work in California?
A: Yes. American Glass Experts holds CSLB C-17 Glazing Contractor License #1125850, verifiable at cslb.ca.gov.

Q: Do you serve all of Los Angeles County?
A: Yes. We serve 130+ cities across Los Angeles, Ventura, San Bernardino, and Riverside Counties.

Q: How fast can you respond to emergency glass repair?
A: We typically dispatch within 1–2 hours for emergency board-up in the San Fernando Valley area, Mon–Sat 7am–10pm.
```

### Off-Site Brand Signals
| Signal | Status | AI Citation Correlation |
|---|---|---|
| YouTube channel | **MISSING** | 0.737 (highest) |
| Reddit presence | **MISSING** | High |
| Wikipedia/Wikidata | **MISSING** | High |
| GBP (Google Business Profile) | Unconfirmed | Critical |
| Yelp | Present (4.8★) | Moderate |
| CSLB verifier link | Present | Strong |

**YouTube is the single highest-ROI off-site action.** 3–5 short videos (shower door install, foggy window diagnosis, emergency board-up) would directly increase brand mentions in ChatGPT and Perplexity responses.

---

## Local SEO

**Score: 44 / 100**

### NAP Consistency
| Source | Name | Address | Phone |
|---|---|---|---|
| All site pages | American Glass Experts Inc. | 6853 Reseda Blvd, Reseda CA | (805) 750-6471 |
| **BBB listing** | **American Glass Experts INC** | **1112 Richardson AVE, Simi Valley CA** | **(818) 426-4649** |

**BBB is a Tier 1 citation (DA 91) with completely wrong data. This is the highest-priority local SEO fix.**

### GBP On-Site Signals: 0/6
No Maps embed, no Place ID link, no Google review CTA, no GBP badge anywhere on site.

### Review Health
- 4.8 stars claimed (Google & Yelp) — no review count disclosed
- `/review` page exists and returns 200 ✓
- No `aggregateRating` schema → Google cannot surface stars in rich results
- Yelp slug ends in `-4` → possible duplicate Yelp listings, needs manual check

### City Page Quality
- 145 city pages at 65–70% boilerplate
- Doorway page risk: MEDIUM-HIGH for competitive cities
- Focus: cities within 25 miles of Reseda for local pack (proximity = 55.2% of ranking variance)
- Palm Springs, Big Bear, Temecula (50–70 mi) — local pack ranking unlikely regardless of optimization

---

## Images

- Logo: `.avif` format ✓
- OG images: Not confirmed on city pages or blog posts
- Alt text: Not audited at scale (check with automated scan)
- Blog post images: Missing from Article schema (blocks rich results)

---

## Limitations

- Performance: Exact CWV numbers require Lighthouse (Chrome not available in this environment). Run manually at pagespeed.web.dev.
- GBP live status: Cannot verify profile existence, completeness, review count without API access or dashboard
- Backlink profile: Not audited (no Moz/Ahrefs credentials)
- Yelp duplicate investigation: 403 blocked
- GSC click/impression data: Not available without API auth
