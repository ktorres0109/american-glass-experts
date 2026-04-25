#!/usr/bin/env python3
"""
Add cross-links:
1. Service pages → "Cities We Serve" section (body inline links to city pages)
2. City pages → "Our Glass Services" section (body inline links to service pages)
"""
import os
import re

# ── Service page data ──────────────────────────────────────────────
SERVICE_PAGES = {
    "shower-enclosures": {
        "name": "Shower Enclosures",
        "desc": "Frameless, semi-frameless, and sliding shower glass",
    },
    "window-repair": {
        "name": "Window Repair",
        "desc": "Broken seals, foggy double-pane, cracked or shattered glass",
    },
    "storefront-glass": {
        "name": "Storefront Glass",
        "desc": "Tempered panels, aluminum framing, and commercial glass doors",
    },
    "custom-mirrors": {
        "name": "Custom Mirrors",
        "desc": "Bathroom, closet, gym, and wall mirrors — any size, any finish",
    },
    "emergency-glass": {
        "name": "Emergency Glass",
        "desc": "Same-day board-up and urgent glass replacement",
    },
}

# ── Cities by county for service pages ────────────────────────────
CITIES_BY_COUNTY = {
    "San Fernando Valley": [
        ("reseda", "Reseda"),
        ("northridge", "Northridge"),
        ("woodland-hills", "Woodland Hills"),
        ("canoga-park", "Canoga Park"),
        ("chatsworth", "Chatsworth"),
        ("van-nuys", "Van Nuys"),
        ("sherman-oaks", "Sherman Oaks"),
        ("encino", "Encino"),
        ("tarzana", "Tarzana"),
        ("north-hollywood", "North Hollywood"),
        ("studio-city", "Studio City"),
        ("burbank", "Burbank"),
        ("glendale", "Glendale"),
    ],
    "Los Angeles County": [
        ("los-angeles", "Los Angeles"),
        ("pasadena", "Pasadena"),
        ("santa-monica", "Santa Monica"),
        ("long-beach", "Long Beach"),
        ("torrance", "Torrance"),
        ("inglewood", "Inglewood"),
        ("compton", "Compton"),
        ("downey", "Downey"),
        ("culver-city", "Culver City"),
        ("malibu", "Malibu"),
    ],
    "Ventura County": [
        ("thousand-oaks", "Thousand Oaks"),
        ("simi-valley", "Simi Valley"),
        ("camarillo", "Camarillo"),
        ("oxnard", "Oxnard"),
        ("ventura", "Ventura"),
        ("moorpark", "Moorpark"),
    ],
    "San Bernardino &amp; Riverside Counties": [
        ("rancho-cucamonga", "Rancho Cucamonga"),
        ("ontario", "Ontario"),
        ("fontana", "Fontana"),
        ("riverside", "Riverside"),
        ("corona", "Corona"),
        ("san-bernardino", "San Bernardino"),
        ("moreno-valley", "Moreno Valley"),
        ("rialto", "Rialto"),
    ],
}

def make_service_city_section():
    """HTML section for service pages listing cities served."""
    county_html = ""
    for county, cities in CITIES_BY_COUNTY.items():
        links = " &nbsp;·&nbsp; ".join(
            f'<a href="/{slug}" style="color:var(--blue);white-space:nowrap;">{name}</a>'
            for slug, name in cities
        )
        county_html += f"""
        <div style="margin-bottom:20px;">
          <strong style="font-size:.85rem;text-transform:uppercase;letter-spacing:.08em;color:var(--text-mid);">{county}</strong>
          <p style="margin-top:8px;font-size:.95rem;line-height:1.9;color:var(--text);">{links}</p>
        </div>"""

    return f"""
  <section class="content-section reveal" style="background:var(--bg-soft);">
    <div class="container" style="max-width:900px;">
      <span class="section-label">Service Area</span>
      <h2>Cities We Serve Across Southern California</h2>
      <p style="color:var(--text-mid);margin-bottom:36px;line-height:1.8;">We're based in Reseda and travel throughout Los Angeles, Ventura, San Bernardino, and Riverside Counties. C-17 Licensed · CSLB #1125850 · Free estimates.</p>
      {county_html}
      <p style="margin-top:24px;font-size:.9rem;color:var(--text-mid);">Don't see your city? <a href="/service-areas" style="color:var(--blue);">View the full service area list →</a></p>
    </div>
  </section>
"""

def make_city_service_section(city_name):
    """HTML section for city pages listing service links."""
    service_cards = ""
    for slug, info in SERVICE_PAGES.items():
        service_cards += f"""
        <a href="/{slug}" style="display:block;padding:20px 24px;background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r-lg);text-decoration:none;transition:box-shadow var(--t),border-color var(--t);" onmouseover="this.style.boxShadow='var(--sh-md)';this.style.borderColor='var(--blue-lt)'" onmouseout="this.style.boxShadow='';this.style.borderColor='var(--border)'">
          <strong style="color:var(--coal);font-size:1rem;">{info["name"]}</strong>
          <p style="color:var(--text-mid);font-size:.88rem;margin-top:6px;line-height:1.6;">{info["desc"]}</p>
          <span style="color:var(--blue);font-size:.85rem;margin-top:8px;display:inline-block;">Learn more →</span>
        </a>"""

    return f"""
  <section style="background:var(--bg-soft);padding:64px 0;" class="reveal">
    <div class="container" style="max-width:900px;">
      <span class="section-label">What We Offer</span>
      <h2>Glass Services Available in <em>{city_name}</em></h2>
      <p style="color:var(--text-mid);margin-bottom:36px;line-height:1.8;">Every service we provide is available in {city_name}. Click a service to learn more about pricing, process, and what to expect.</p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;">
        {service_cards}
      </div>
    </div>
  </section>
"""

# ── Process service pages ──────────────────────────────────────────
CTA_BAND_PATTERN = re.compile(r'(\s*<section class="cta-band")')
CITY_SECTION_HTML = make_service_city_section()

fixed_service = 0
for slug in SERVICE_PAGES:
    path = f"{slug}.html"
    if not os.path.exists(path):
        print(f"  MISSING {path}")
        continue
    with open(path) as f:
        content = f.read()
    if 'Cities We Serve Across Southern California' in content:
        print(f"  SKIP {path} — already has city section")
        continue
    # Insert before cta-band
    new_content = CTA_BAND_PATTERN.sub(CITY_SECTION_HTML + r'\1', content, count=1)
    if new_content == content:
        print(f"  WARN {path} — cta-band not found, check manually")
        continue
    with open(path, "w") as f:
        f.write(new_content)
    print(f"  FIXED service page: {path}")
    fixed_service += 1

print(f"\nService pages: {fixed_service} updated")

# ── Process city pages ─────────────────────────────────────────────
# All .html files that are city pages (exclude non-city pages)
NON_CITY = {
    'index.html','about.html','contact.html','services.html',
    'service-areas.html','blog.html','gallery.html','review.html',
    'privacy-policy.html','shower-enclosures.html','window-repair.html',
    'storefront-glass.html','custom-mirrors.html','emergency-glass.html',
}

# City slug → display name (derive from slug)
def slug_to_name(slug):
    return slug.replace('-', ' ').title()

FAQ_SECTION_PATTERN = re.compile(r'(\s*<!-- FAQ -->)')

fixed_city = 0
skipped_city = 0
for fname in sorted(os.listdir('.')):
    if not fname.endswith('.html') or fname in NON_CITY:
        continue
    slug = fname[:-5]
    city_name = slug_to_name(slug)

    with open(fname) as f:
        content = f.read()

    if 'Glass Services Available in' in content:
        skipped_city += 1
        continue

    # Get actual city name from H1 if possible
    h1_match = re.search(r'<h1[^>]*>.*?in\s+<em>([^<]+)</em>', content)
    if h1_match:
        city_name = h1_match.group(1).replace(', CA', '')

    section_html = make_city_service_section(city_name)

    # Insert before <!-- FAQ --> comment
    new_content = FAQ_SECTION_PATTERN.sub(section_html + r'\1', content, count=1)
    if new_content == content:
        print(f"  WARN {fname} — FAQ comment not found")
        skipped_city += 1
        continue

    with open(fname, "w") as f:
        f.write(new_content)
    fixed_city += 1

print(f"City pages: {fixed_city} updated, {skipped_city} skipped")
print("Done.")
