# SEO Action Plan — American Glass Experts Inc.
**Generated:** 2026-04-30
**Overall Score:** 65/100
**Target:** 80/100 in 90 days

---

## CRITICAL — Fix Immediately (This Week)

### 1. Fix BBB Citation NAP Conflict
**Impact:** High | **Effort:** 30 min | **Category:** Local SEO

BBB lists wrong address (Simi Valley) and wrong phone ((818) 426-4649). This is a DA 91 citation actively harming local authority.

**Action:** Go to bbb.org → find "American Glass Experts" → claim listing → update to:
- Name: American Glass Experts Inc.
- Address: 6853 Reseda Blvd, Reseda, CA 91335
- Phone: (805) 750-6471
- Category: Glass & Glazing Contractors

### 2. Fix Blog Author Schema — All 6 Posts
**Impact:** High | **Effort:** 30 min | **Category:** Schema + E-E-A-T

All 6 blog posts have `"author": {"@type": "Person", "name": "American Glass Experts Team"}`. This mismatches the visible byline and hurts AI citation E-E-A-T signals.

**Action:** In all 6 blog HTML files, change author block to:
```json
"author": {
  "@type": "Person",
  "name": "Frank Salinas",
  "jobTitle": "Lead Glazier",
  "url": "https://www.americanglassexperts.us/about#frank"
}
```
Then add an `id="frank"` anchor section on the About page with a 2–3 sentence bio and CSLB credential mention.

### 3. Boost Google Review Velocity
**Impact:** High | **Effort:** Ongoing | **Category:** Local SEO

17 reviews is critically low for a 4-county market. Most recent in schema is Sept 2024 — a 7-month drought. Sterling Sky 18-day rule means rankings penalize stale velocity.

**Action:**
- After every completed job, text the customer a direct link to the Google review page (use review.html shortlink)
- Target: 2–3 new Google reviews per month minimum
- Respond to all existing reviews on GBP (if not done)
- Prioritize Google over Yelp — Google reviews carry far more GBP ranking weight

### 4. Verify GBP Primary Category
**Impact:** High | **Effort:** 15 min | **Category:** Local SEO

Primary GBP category is the #1 local ranking factor (Whitespark 2026).

**Action:** Log into GBP → verify primary category is "Glass repair service" (not a generic contractor category) → add secondary categories:
- Mirror shop
- Shower door shop
- Glass & mirror shop

---

## HIGH — Fix Within 1 Week

### 5. Fix Identical Meta Descriptions on 131 City Pages
**Impact:** High | **Effort:** 2–3 hrs (scripted) | **Category:** On-Page SEO

All 131 city pages use: `"Professional glass repair and installation in [CITY], CA — shower enclosures, windows, storefronts, mirrors. Licensed C-17 contractor. Free estimates. Call (805) 750-6471."`

GSC flags this as 131 duplicate meta descriptions.

**Action:** Write a script to generate city-specific meta descriptions. Suggested variants by region:
- SFV cities: `"Glass repair & installation in [CITY] — we're based nearby in Reseda. Shower enclosures, windows, storefronts, mirrors. C-17 Licensed. Free estimates."`
- IE/Desert cities: `"Licensed glass contractor serving [CITY], [COUNTY]. [X]-minute response. Shower doors, windows, storefronts. Free estimates. Call (805) 750-6471."`
- Coastal/LA: `"Custom glass in [CITY] — frameless showers, dual-pane windows, storefronts. C-17 glazing contractor. Free estimate. Serving [CITY] and [COUNTY]."`

### 6. Add Google Maps Embed to Homepage
**Impact:** High | **Effort:** 15 min | **Category:** Local SEO

No Maps embed on homepage. Missing trust signal and proximity cue.

**Action:** Embed the business's GBP listing map in the contact section of index.html. Also add to the top 10 highest-traffic city pages (Los Angeles, Burbank, Glendale, North Hollywood, Pasadena).

### 7. Fix Copyright Footer Across All Pages
**Impact:** Low | **Effort:** 5 min (global find-replace) | **Category:** Technical

Footer says `© 2025` but blog posts are dated April 2026 — contradiction visible to AI crawlers.

**Action:** Global find-replace `© 2025 American Glass Experts` → `© 2026 American Glass Experts` across all HTML files.

---

## HIGH — Fix Within 2 Weeks

### 8. Build Missing Tier 1–2 Citations
**Impact:** High | **Effort:** 3–4 hrs total | **Category:** Local SEO / Backlinks

None of these directories appear in current citations. All use exact NAP: "American Glass Experts Inc." / "6853 Reseda Blvd, Reseda, CA 91335" / "(805) 750-6471"

| Directory | Action |
|---|---|
| Angi (HomeAdvisor) | Create contractor profile |
| Houzz | Create profile + add gallery photos |
| Thumbtack | Create profile |
| Bing Places | Claim business listing |
| Apple Maps Connect | Claim listing |
| Nextdoor Business | Claim business page |
| BuildZoom | Verify auto-indexed CSLB entry is correct |

### 9. Add `logo`, `foundingDate`, `makesOffer` to Homepage Schema
**Impact:** Medium | **Effort:** 30 min | **Category:** Schema

Quick schema improvements to homepage `HomeAndConstructionBusiness` block:

```json
"logo": {
  "@type": "ImageObject",
  "url": "https://www.americanglassexperts.us/logo.avif",
  "width": 200,
  "height": 60
},
"foundingDate": "2003",
"hasOfferCatalog": {
  "@type": "OfferCatalog",
  "name": "Glass Repair & Installation Services",
  "itemListElement": [
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Shower Enclosures", "url": "https://www.americanglassexperts.us/shower-enclosures"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Window Repair", "url": "https://www.americanglassexperts.us/window-repair"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Storefront Glass", "url": "https://www.americanglassexperts.us/storefront-glass"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Custom Mirrors", "url": "https://www.americanglassexperts.us/custom-mirrors"}},
    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Emergency Glass", "url": "https://www.americanglassexperts.us/emergency-glass"}}
  ]
}
```

### 10. Fix Placeholder Phone in Contact Forms
**Impact:** Medium | **Effort:** 15 min | **Category:** On-Page

133 pages have `placeholder="(818) 555-0000"` in contact forms. Should be the business number.

**Action:** Global find-replace `(818) 555-0000` → `(805) 750-6471` across all HTML files.

### 11. Add `#frank` Section to About Page
**Impact:** Medium | **Effort:** 1 hr | **Category:** E-E-A-T

Blog posts reference "Frank, Lead Glazier" but About page has no named team members or `id="frank"` anchor. AI systems can't build a credentialed person entity without a linkable page.

**Action:** Add to about.html:
```html
<section id="frank">
  <h2>Frank Salinas — Lead Glazier</h2>
  <p>[2-3 sentence bio: years of experience, specialties, C-17 license context]</p>
  <p>C-17 Licensed under CSLB #1125850. Verifiable at <a href="https://www.cslb.ca.gov">cslb.ca.gov</a>.</p>
</section>
```

---

## MEDIUM — Fix Within 1 Month

### 12. Add Blog ↔ City Page Cross-Links
**Impact:** Medium | **Effort:** 2 hrs | **Category:** On-Page / Internal Linking

Blog posts don't link to city pages. City pages don't link to relevant blog posts.

**Action:**
- Add "See our Los Angeles cost guide →" contextual links from relevant city pages to the shower door cost blog post
- Add 2–3 city page links (highest traffic cities) within blog post body content

### 13. Expand Blog Body Paragraphs to 134–167 Words
**Impact:** Medium | **Effort:** 2–3 hrs across 6 posts | **Category:** AI Search

Body paragraphs run 80–130 words — below AI citation optimal range. Adding one concrete detail per paragraph (specific example, measurement spec, local code reference) hits the target range.

### 14. Add `HowTo` Schema to Process Blog Posts
**Impact:** Medium | **Effort:** 2 hrs | **Category:** Schema

Posts like the installation guide are natural fits for `HowTo` markup that AI systems use for step-by-step answer cards.

### 15. Add `dateModified` to All Blog Posts
**Impact:** Low | **Effort:** 30 min | **Category:** Schema / Content Freshness

Only 1 of 6 posts has `dateModified`. Add to all and update it whenever content is revised.

### 16. Upgrade `areaServed` on City Pages
**Impact:** Low | **Effort:** Scripted | **Category:** Schema

Change flat string `"areaServed": "Burbank"` → typed City object:
```json
"areaServed": {"@type": "City", "name": "Burbank", "containedInPlace": {"@type": "AdministrativeArea", "name": "Los Angeles County"}}
```

---

## LOW — Backlog

### 17. Start YouTube Channel
**Impact:** Very High long-term | **Effort:** High | **Category:** AI Search / Backlinks

0.737 AI citation correlation. 2 anchor videos with immediate ROI:
- "How Much Does a Frameless Shower Door Cost in Los Angeles? (2026)"
- "Foggy Window Repair vs Replacement — Los Angeles Homeowners Guide"

Both should: include business name, CSLB #, phone in description. Blog posts should embed the corresponding videos.

### 18. Add Explicit ClaudeBot / PerplexityBot to robots.txt
**Action:** Add before wildcard rule:
```
User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /
```

### 19. Add ImageObject Schema to Blog Post Images
Add `caption`, `description`, and `keywords` to the `ImageObject` within Article schema on all blog posts.

### 20. Verify Yelp Listing NAP
Manually visit `yelp.com/biz/american-glass-experts-san-fernando-valley-4` — confirm address and phone match exactly. The `-4` slug suffix may indicate duplicate listings; if so, consolidate.

### 21. Monitor GSC for "Crawled - currently not indexed" Recovery
City page content diversification was deployed 2026-04-30. Check GSC in 2–4 weeks to confirm hemet, wildomar, lake-elsinore, and baldwin-park have moved to "Indexed" status.

---

## 90-Day Roadmap

| Week | Actions |
|---|---|
| Week 1 | Fix BBB · Fix blog author schema · Fix copyright footer · Verify GBP category · Start review velocity campaign |
| Week 2 | Unique meta descriptions on all city pages · Add Maps embed to homepage + top 5 cities · Fix contact form placeholder phone |
| Week 3–4 | Build Angi, Houzz, Bing Places, Thumbtack, Nextdoor citations · Add `#frank` section to About · Schema quick-wins (logo, foundingDate, makesOffer) |
| Month 2 | Add blog ↔ city cross-links · Expand blog paragraphs · HowTo schema · dateModified on all posts |
| Month 3 | YouTube channel first 2 videos · Apple Maps · Wikidata entity · Monitor GSC indexing recovery |

**Expected score at 90 days if all High/Critical items resolved:** ~79–82/100
