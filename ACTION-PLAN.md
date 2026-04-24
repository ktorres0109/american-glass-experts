# SEO Action Plan — American Glass Experts
**Generated:** 2026-04-23  
**Overall Score:** 61/100  
**Goal:** 80/100 in 90 days

---

## CRITICAL — Fix Immediately (This Week)

### 1. Fix BBB Citation Conflict
**Impact:** Local SEO | **Effort:** 30 min
- BBB shows: 1112 Richardson Ave, Simi Valley, (818) 426-4649, category "Landscape Contractors"
- Go to bbb.org → claim/find listing → correct address to 6853 Reseda Blvd, Reseda CA 91335
- Correct phone to (805) 750-6471
- Correct category to "Glass & Mirror Shop" or "Glazing Contractor"
- If not claimable, submit a business dispute

### 2. Add `image` to Homepage LocalBusiness Schema
**Impact:** Schema rich results | **Effort:** 15 min
In `index.html`, inside the `HomeAndConstructionBusiness` JSON-LD block, add:
```json
"image": {
  "@type": "ImageObject",
  "url": "https://www.americanglassexperts.us/logo.avif",
  "width": 512,
  "height": 512
}
```

### 3. Fix Blog Article Schema (unblocks rich results for all 6 posts)
**Impact:** Article rich results | **Effort:** 1–2 hours
For each blog post HTML file, update the `Article` JSON-LD block:
```json
"image": {
  "@type": "ImageObject",
  "url": "https://www.americanglassexperts.us/blog/[post-slug]/og.jpg",
  "width": 1200,
  "height": 630
},
"dateModified": "2026-04-23",
"mainEntityOfPage": {
  "@type": "WebPage",
  "@id": "https://www.americanglassexperts.us/blog/[post-slug]"
},
"author": {
  "@type": "Organization",
  "@id": "https://www.americanglassexperts.us/#business",
  "name": "American Glass Experts Inc."
},
"publisher": {
  "@type": "Organization",
  "@id": "https://www.americanglassexperts.us/#business",
  "name": "American Glass Experts Inc.",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.americanglassexperts.us/logo-icon-dark.png"
  }
}
```
Affects: foggy-window-repair-los-angeles, frameless-shower-door-cost-los-angeles, storefront-glass-replacement-los-angeles, emergency-glass-repair-los-angeles, glass-shower-door-installation-los-angeles, commercial-storefront-glass-repair-los-angeles

### 4. Fix robots.txt — Enforce Training Exclusion
**Impact:** IP compliance + AI hygiene | **Effort:** 5 min
Add to `robots.txt`:
```
User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: cohere-ai
Disallow: /
```

### 5. Continue GSC URL Inspection — 10/day
**Impact:** Indexing | **Effort:** 10 min/day
Keep doing what you're doing. Prioritize in this order:
1. Service pages (shower-enclosures, window-repair, storefront-glass, custom-mirrors, emergency-glass)
2. High-volume city pages (los-angeles, glendale, burbank, pasadena, long-beach, torrance)
3. Blog posts (all 6)
4. Remaining city pages alphabetically

---

## HIGH — Fix Within 1 Week

### 6. Update llms.txt with License, Pricing, FAQ blocks
**Impact:** AI Overview citations | **Effort:** 20 min
Add to `llms.txt`:
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
A: Yes. We serve 130+ cities across Los Angeles, Ventura, San Bernardino, and Riverside Counties from our base in Reseda, CA.

Q: How fast can you respond to emergency glass repair?
A: We typically dispatch within 1–2 hours for emergency board-up in the San Fernando Valley, Mon–Sat 7am–10pm.
```

### 7. Confirm GBP Exists + Add On-Site Signals
**Impact:** Local pack #1 factor | **Effort:** 1–3 hours
- Verify GBP at business.google.com — confirm it exists and is verified
- Add Maps embed to `/contact` page (use iframe embed from Google Maps)
- Add a "Leave us a Google Review" link in footer using the GBP Place ID URL
- Add GBP profile URL to `llms.txt`
- Primary GBP category: "Glass & Mirror Shop" or "Window Installation Service"

### 8. Update City Page LocalBusiness Schema
**Impact:** Local entity graph | **Effort:** 1–2 hours (scripted change)
Currently 145 city pages have bare `LocalBusiness` with no `@id`, `geo`, `aggregateRating`, or `sameAs`.

Run a script to update all city page templates. Add to each city's `LocalBusiness` JSON-LD:
```json
"@id": "https://www.americanglassexperts.us/[city-slug]#business",
"geo": {
  "@type": "GeoCoordinates",
  "latitude": 34.2003,
  "longitude": -118.5359
},
"aggregateRating": {
  "@type": "AggregateRating",
  "ratingValue": "4.8",
  "reviewCount": "17",
  "bestRating": "5"
},
"sameAs": [
  "https://www.yelp.com/biz/american-glass-experts-san-fernando-valley-4",
  "https://share.google/bjUDf31y962SkEPvv"
],
"image": {
  "@type": "ImageObject",
  "url": "https://www.americanglassexperts.us/logo.avif"
},
"parentOrganization": {
  "@type": "HomeAndConstructionBusiness",
  "@id": "https://www.americanglassexperts.us/#business"
}
```

### 9. Add FAQ Sections to Top 2 Blog Posts
**Impact:** AI Overviews direct answers | **Effort:** 1–2 hours
Target posts (highest-volume queries):
- `frameless-shower-door-cost-los-angeles` → add FAQ: "How much does a frameless shower door cost?", "What factors affect shower door price?", "Do you offer financing?"
- `foggy-window-repair-los-angeles` → add FAQ: "Can a foggy window be fixed without full replacement?", "How much does IGU replacement cost in LA?", "How long does it take?"

Add FAQPage JSON-LD to each post. The FAQ content you already have on service pages can be adapted.

### 10. Fix BreadcrumbList Trailing Slash Consistency
**Impact:** Schema validation | **Effort:** 30 min (scripted)
City page breadcrumbs have inconsistent trailing slashes. The `item` URL in the city ListItem should end in `/` to match canonical format.
Change: `"item": "https://www.americanglassexperts.us/los-angeles"`  
To: `"item": "https://www.americanglassexperts.us/los-angeles/"`

---

## MEDIUM — Fix Within 1 Month

### 11. Expand Reseda Page as Flagship Location
**Impact:** Local SEO + proximity rankings | **Effort:** 2–3 hours
Reseda is the business address — should be the highest-authority city page but is identical to every other. Add:
- 600+ words of unique Reseda-specific content
- Maps embed tied to 6853 Reseda Blvd
- Photo gallery of local Reseda/Valley jobs
- Testimonials block with reviews from Reseda/nearby customers
- Full `HomeAndConstructionBusiness` schema with precise geo coords

### 12. Build Out 8 High-Value City Pages
**Impact:** Competitive city rankings | **Effort:** 4–8 hours**
These markets have the highest search volume. Each needs 400+ words of unique content:
- Los Angeles, Glendale, Burbank, Pasadena (LA County)
- Thousand Oaks, Simi Valley, Ventura (Ventura County)  
- Riverside, Corona, Rancho Cucamonga (IE)

Content to add: local housing stock, common job types, specific neighborhood references (3–5), local permit context, 1 specific project scenario or case study.

### 13. Add Author Bylines to All Blog Posts
**Impact:** E-E-A-T | **Effort:** 30 min
Add to each blog post near the top:
`Written by Frank, Lead Glazier — C-17 Licensed, 15+ years in Southern California`

Also update Article schema `author` to reference a named person:
```json
"author": {
  "@type": "Person",
  "name": "Frank [Last Name]",
  "jobTitle": "Lead Glazier",
  "worksFor": { "@id": "https://www.americanglassexperts.us/#business" }
}
```

### 14. Add Meta Descriptions to All City Pages
**Impact:** CTR | **Effort:** 2–3 hours (scripted)
Template: `Licensed C-17 glass repair in [City], CA. Shower enclosures, window repair, emergency board-up. Free estimates. Call (805) 750-6471.`

### 15. Cross-Link City Pages ↔ Service Pages
**Impact:** Internal link graph + crawl depth | **Effort:** 2–3 hours
- Each city page should link to: /shower-enclosures, /window-repair, /emergency-glass
- Each service page should link to top 5–8 nearest cities
- Add breadcrumb: Home → Service Areas → [County] → [City]

### 16. Add `offers` to 4 Service Objects (Services page schema)
**Impact:** Schema completeness | **Effort:** 30 min
Window repair, storefront glass, emergency glass, custom mirrors are missing `offers` in their Service JSON-LD.

### 17. Verify Yelp for Duplicate Listings
**Impact:** Local citation hygiene | **Effort:** 30 min
Yelp slug ends in `-4` which indicates possible auto-created duplicates. Log into Yelp business account, search for "American Glass Experts" to find and merge/suppress any duplicates. Ensure primary listing shows Reseda address.

### 18. Investigate 2 Redirect Errors + 3 Alternate Canonical Pages in GSC
**Impact:** Indexing | **Effort:** 30 min
Go to GSC → Pages → click "Redirect error" row → find exact URLs → use URL Inspection to diagnose.
Same for "Alternate page with proper canonical tag" row.

---

## LOW — Backlog

### 19. Create YouTube Channel with 3–5 Videos
**Impact:** AI citation (0.737 correlation) | **Effort:** 2–3 days filming
Highest-ROI off-site action for ChatGPT/Perplexity visibility. Video ideas:
- "How we install a frameless shower door in LA" (timelapse/process)
- "How to tell if your window seal is broken (and when to repair vs replace)"
- "What happens during emergency glass board-up"
- "Foggy window IGU replacement — before and after"

### 20. Reddit Presence
**Impact:** AI brand signals | **Effort:** Ongoing
Answer genuine questions in r/LosAngeles, r/HomeImprovement, r/sanfernandovalley about glass repair, window seals, shower doors. No promotional spam — authentic expert answers only.

### 21. EmergencyService Schema on /emergency-glass
**Impact:** Emergency query rich results | **Effort:** 30 min
Add `"@type": ["HomeAndConstructionBusiness", "EmergencyService"]` and 24/7 `openingHoursSpecification` to the emergency glass page schema.

### 22. `image` + `offers` on All 5 Service Objects
**Impact:** Schema richness | **Effort:** 1 hour
Add service photos to each Service JSON-LD block.

### 23. OG Images for City Pages and Blog Posts
**Impact:** Social sharing CTR | **Effort:** Template-based
Ensure all pages have `og:image` meta tags pointing to valid 1200×630 images.

### 24. noindex Low-Value Distant City Pages
**Impact:** Crawl budget | **Effort:** 1–2 hours
Cities 50+ miles from Reseda (Palm Springs, Big Bear, Temecula, Adelanto, Banning) have near-zero local pack potential due to proximity bias. Consider noindexing the weakest ones to focus crawl budget on pages with ranking potential.

---

## 90-Day Roadmap

| Week | Actions |
|---|---|
| 1 | Fix BBB, add `image` to homepage schema, fix blog Article schema, fix robots.txt, continue GSC 10/day |
| 2 | Update llms.txt, confirm GBP + add Maps embed, update city page LocalBusiness schema (scripted), fix breadcrumb slashes |
| 3 | Add FAQ to top 2 blog posts, add author bylines, meta descriptions for all city pages |
| 4 | Cross-link city ↔ service pages, expand Reseda page |
| 5–8 | Build out 8 high-value city pages (400+ words each), fix GSC redirect errors |
| 9–12 | YouTube channel first 3 videos, Reddit presence, EmergencyService schema, remaining schema cleanup |

---

## Score Projection

| Category | Current | Target (90 days) |
|---|---|---|
| Technical SEO | 68 | 80 |
| Content Quality | 52 | 68 |
| On-Page SEO | 60 | 74 |
| Schema | 58 | 85 |
| Performance | 72 | 75 |
| AI Search Readiness | 64 | 80 |
| Images | 55 | 70 |
| **Overall** | **61** | **78** |
