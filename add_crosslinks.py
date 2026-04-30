#!/usr/bin/env python3
"""
Add blog ↔ city cross-links.
1. Blog posts → city pill links (service areas callout before </main>)
2. City pages → blog post cards (related reading before <!-- FOOTER -->)
"""
import os, re, glob

ROOT = "/Users/kel/Documents/projects/american-glass-experts"

# ── BLOG POST DATA ─────────────────────────────────────────────────────────────
BLOGS = {
    "frameless-shower-door-cost-los-angeles": {
        "title": "How Much Does a Frameless Shower Door Cost in LA? (2026)",
        "label": "Cost Guide · 2026",
    },
    "glass-shower-door-installation-los-angeles": {
        "title": "Glass Shower Door Installation: What to Expect",
        "label": "Installation Guide",
    },
    "foggy-window-repair-los-angeles": {
        "title": "Foggy Window Repair vs. Replacement in Los Angeles",
        "label": "Window Guide",
    },
    "emergency-glass-repair-los-angeles": {
        "title": "Emergency Glass Repair in Los Angeles: What to Do First",
        "label": "Emergency Guide",
    },
    "storefront-glass-replacement-los-angeles": {
        "title": "Storefront Glass Replacement: A Contractor's Guide",
        "label": "Storefront Guide",
    },
    "commercial-storefront-glass-repair-los-angeles": {
        "title": "Commercial Storefront Glass Repair in Los Angeles",
        "label": "Commercial Guide",
    },
}

# ── BLOG → CITY MAPPING ────────────────────────────────────────────────────────
# 6 contextually relevant cities per post
BLOG_CITIES = {
    "frameless-shower-door-cost-los-angeles": [
        ("Burbank",        "burbank"),
        ("Glendale",       "glendale"),
        ("Pasadena",       "pasadena"),
        ("Woodland Hills", "woodland-hills"),
        ("Calabasas",      "calabasas"),
        ("Sherman Oaks",   "sherman-oaks"),
    ],
    "glass-shower-door-installation-los-angeles": [
        ("Calabasas",        "calabasas"),
        ("Hidden Hills",     "hidden-hills"),
        ("Malibu",           "malibu"),
        ("Sherman Oaks",     "sherman-oaks"),
        ("Encino",           "encino"),
        ("Pasadena",         "pasadena"),
    ],
    "foggy-window-repair-los-angeles": [
        ("Pasadena",       "pasadena"),
        ("Glendale",       "glendale"),
        ("Burbank",        "burbank"),
        ("San Marino",     "san-marino"),
        ("South Pasadena", "south-pasadena"),
        ("Alhambra",       "alhambra"),
    ],
    "emergency-glass-repair-los-angeles": [
        ("Los Angeles",    "los-angeles"),
        ("Burbank",        "burbank"),
        ("Glendale",       "glendale"),
        ("North Hollywood","north-hollywood"),
        ("Long Beach",     "long-beach"),
        ("Van Nuys",       "van-nuys"),
    ],
    "storefront-glass-replacement-los-angeles": [
        ("Los Angeles",      "los-angeles"),
        ("Burbank",          "burbank"),
        ("Glendale",         "glendale"),
        ("Ontario",          "ontario"),
        ("Rancho Cucamonga", "rancho-cucamonga"),
        ("Long Beach",       "long-beach"),
    ],
    "commercial-storefront-glass-repair-los-angeles": [
        ("Los Angeles",    "los-angeles"),
        ("Glendale",       "glendale"),
        ("Burbank",        "burbank"),
        ("Long Beach",     "long-beach"),
        ("San Bernardino", "san-bernardino"),
        ("Ontario",        "ontario"),
    ],
}

# ── CITY → BLOG MAPPING ────────────────────────────────────────────────────────
# Each city gets 2 blog posts based on region/type

LA_SFV = ["arleta","canoga-park","chatsworth","encino","granada-hills","mission-hills",
           "north-hills","northridge","pacoima","panorama-city","reseda","san-fernando",
           "sherman-oaks","studio-city","sylmar","tarzana","valley-village","van-nuys",
           "west-hills","winnetka","woodland-hills","north-hollywood","burbank","glendale",
           "calabasas","hidden-hills","santa-clarita"]

LA_WEST = ["los-angeles","culver-city","inglewood","hawthorne","gardena","compton","carson",
           "torrance","el-segundo","santa-monica","malibu","pacific-palisades","topanga-canyon",
           "long-beach","lakewood","downey","pico-rivera","montebello","monterey-park"]

LA_SGV = ["pasadena","south-pasadena","san-marino","alhambra","san-gabriel","temple-city",
          "monrovia","duarte","azusa","el-monte","la-puente","west-covina","covina","glendora",
          "diamond-bar","pomona","la-verne","san-dimas","walnut","claremont","whittier","baldwin-park"]

VENTURA = ["agoura-hills","bell-canyon","camarillo","fillmore","moorpark","newbury-park",
           "oak-park","oxnard","port-hueneme","santa-paula","simi-valley","thousand-oaks",
           "ventura","westlake-village"]

SB = ["adelanto","apple-valley","big-bear-lake","calimesa","chino","chino-hills","colton",
      "fontana","grand-terrace","hesperia","loma-linda","montclair","ontario","rancho-cucamonga",
      "redlands","rialto","san-bernardino","upland","victorville","yucaipa"]

RIVERSIDE = ["banning","beaumont","canyon-lake","corona","eastvale","hemet","jurupa-valley",
             "lake-elsinore","menifee","moreno-valley","murrieta","norco","perris","riverside",
             "rubidoux","san-jacinto","sun-city","temecula","wildomar","winchester"]

DESERT = ["cathedral-city","coachella","desert-hot-springs","indian-wells","indio","la-quinta",
          "palm-desert","palm-springs","rancho-mirage"]

def get_city_blogs(slug):
    if slug in LA_WEST:
        return ["storefront-glass-replacement-los-angeles",
                "frameless-shower-door-cost-los-angeles"]
    elif slug in LA_SGV:
        return ["frameless-shower-door-cost-los-angeles",
                "foggy-window-repair-los-angeles"]
    elif slug in VENTURA:
        return ["frameless-shower-door-cost-los-angeles",
                "foggy-window-repair-los-angeles"]
    elif slug in SB:
        return ["frameless-shower-door-cost-los-angeles",
                "storefront-glass-replacement-los-angeles"]
    elif slug in RIVERSIDE:
        return ["frameless-shower-door-cost-los-angeles",
                "emergency-glass-repair-los-angeles"]
    elif slug in DESERT:
        return ["frameless-shower-door-cost-los-angeles",
                "glass-shower-door-installation-los-angeles"]
    else:  # SFV default
        return ["frameless-shower-door-cost-los-angeles",
                "foggy-window-repair-los-angeles"]


# ── HTML BUILDERS ─────────────────────────────────────────────────────────────

def blog_city_section(blog_slug):
    cities = BLOG_CITIES[blog_slug]
    pills = "\n      ".join(
        f'<a href="/{slug}" style="display:inline-block;padding:8px 18px;background:var(--bg-card);'
        f'border:1.5px solid var(--border-md);border-radius:20px;font-size:.83rem;font-weight:500;'
        f'color:var(--text);transition:all .2s;" '
        f'onmouseover="this.style.borderColor=\'var(--blue)\';this.style.color=\'var(--blue)\'" '
        f'onmouseout="this.style.borderColor=\'var(--border-md)\';this.style.color=\'var(--text)\'">'
        f'{name}</a>'
        for name, slug in cities
    )
    return f'''
<section style="background:var(--bg-soft);border-top:1px solid var(--border);padding:56px 0;">
  <div class="container" style="max-width:820px;margin:0 auto;">
    <span class="section-label">Service Areas</span>
    <h2 style="font-size:clamp(1.3rem,2vw,1.6rem);margin-bottom:10px;">We Serve <em>Southern California</em></h2>
    <p style="color:var(--text-mid);font-size:.92rem;margin-bottom:24px;">Based in Reseda — serving Los Angeles, Ventura, San Bernardino, and Riverside Counties. Free on-site estimates.</p>
    <div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:20px;">
      {pills}
    </div>
    <p style="font-size:.85rem;color:var(--text-mid);">Don\'t see your city? <a href="/service-areas" style="color:var(--blue);font-weight:500;">View all 131 service areas →</a></p>
  </div>
</section>'''


def city_blog_section(city_display, city_slug, blog_slugs):
    cards = ""
    for b in blog_slugs:
        info = BLOGS[b]
        cards += (
            f'<a href="/blog/{b}" style="display:block;padding:20px 24px;background:var(--bg-card);'
            f'border:1.5px solid var(--border);border-radius:var(--r-lg);transition:all .2s;text-decoration:none;" '
            f'onmouseover="this.style.borderColor=\'var(--blue)\';this.style.transform=\'translateY(-2px)\'" '
            f'onmouseout="this.style.borderColor=\'var(--border)\';this.style.transform=\'translateY(0)\'">'
            f'<div style="font-size:.68rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;'
            f'color:var(--blue);margin-bottom:8px;">{info["label"]}</div>'
            f'<div style="font-size:.95rem;font-weight:600;color:var(--charcoal);line-height:1.4;">{info["title"]}</div>'
            f'<div style="font-size:.82rem;color:var(--blue);margin-top:10px;font-weight:500;">Read the guide →</div>'
            f'</a>'
        )
    return f'''
  <!-- RELATED GUIDES -->
  <section style="padding:64px 0;background:var(--bg-soft);border-top:1px solid var(--border);">
    <div class="container">
      <span class="section-label">Related Reading</span>
      <h2 style="font-size:clamp(1.3rem,2vw,1.6rem);margin-bottom:24px;">Glass Guides for <em>{city_display}</em> Homeowners</h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;max-width:720px;">
        {cards}
      </div>
    </div>
  </section>
'''


# ── APPLY ─────────────────────────────────────────────────────────────────────

blog_updated = 0
city_updated = 0

# 1. Blog → city links
for blog_slug, cities in BLOG_CITIES.items():
    path = os.path.join(ROOT, "blog", f"{blog_slug}.html")
    if not os.path.exists(path):
        print(f"SKIP (not found): {path}")
        continue
    with open(path) as f:
        content = f.read()
    if "Service Areas" in content and "View all 131 service areas" in content:
        print(f"SKIP (already has section): {blog_slug}")
        continue
    section = blog_city_section(blog_slug)
    new_content = content.replace("</main>\n<!-- FOOTER -->", f"{section}\n</main>\n<!-- FOOTER -->", 1)
    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        blog_updated += 1
        print(f"  ✓ blog: {blog_slug}")

# 2. City → blog links
all_city_slugs = list(set(LA_SFV + LA_WEST + LA_SGV + VENTURA + SB + RIVERSIDE + DESERT))

# Also grab display names from meta title
for slug in all_city_slugs:
    path = os.path.join(ROOT, f"{slug}.html")
    if not os.path.exists(path):
        continue
    with open(path) as f:
        content = f.read()
    if "Related Guides" in content or "Related Reading" in content:
        continue

    # Get display name from page title
    m = re.search(r'<title>([^|<]+)', content)
    city_display = slug.replace("-", " ").title()
    if m:
        raw = m.group(1).strip()
        # "Glass Repair in Burbank, CA" → "Burbank"
        cm = re.search(r'in ([^,<]+),', raw)
        if cm:
            city_display = cm.group(1).strip()

    blog_slugs = get_city_blogs(slug)
    section = city_blog_section(city_display, slug, blog_slugs)

    new_content = content.replace("  <!-- FOOTER -->\n  <footer", f"{section}\n  <!-- FOOTER -->\n  <footer", 1)
    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        city_updated += 1

print(f"\nBlog posts updated: {blog_updated}/6")
print(f"City pages updated: {city_updated}/{len(all_city_slugs)}")
