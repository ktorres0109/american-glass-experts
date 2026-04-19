#!/usr/bin/env python3
"""Add WebPage + BreadcrumbList JSON-LD to service sub-pages."""
import os

BASE = '/tmp/age'

SERVICE_PAGES = [
    {
        'file': 'shower-enclosures.html',
        'slug': 'shower-enclosures',
        'name': 'Shower Enclosures',
        'description': 'Custom frameless and framed shower enclosures for Los Angeles and Southern California homes.'
    },
    {
        'file': 'window-repair.html',
        'slug': 'window-repair',
        'name': 'Window Repair & Replacement',
        'description': 'Professional window repair and replacement services in Los Angeles — broken seals, foggy glass, cracked panes.'
    },
    {
        'file': 'storefront-glass.html',
        'slug': 'storefront-glass',
        'name': 'Storefront & Commercial Glass',
        'description': 'Commercial storefront glass installation and repair for Los Angeles area businesses.'
    },
    {
        'file': 'custom-mirrors.html',
        'slug': 'custom-mirrors',
        'name': 'Custom Mirrors',
        'description': 'Custom-cut mirrors for bathrooms, closets, gyms, and decorative applications across Los Angeles.'
    },
    {
        'file': 'emergency-glass.html',
        'slug': 'emergency-glass',
        'name': 'Emergency Glass Repair',
        'description': 'Emergency glass repair and board-up services in Los Angeles — break-ins, storm damage, same-day response.'
    },
]

for page in SERVICE_PAGES:
    fpath = os.path.join(BASE, page['file'])
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'BreadcrumbList' in content and 'WebPage' in content:
        print(f"Skipping {page['file']} — already has both schemas")
        continue

    url = f"https://www.americanglassexperts.us/{page['slug']}"
    schema_block = f'''<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "{page['name']}",
  "description": "{page['description']}",
  "url": "{url}",
  "isPartOf": {{
    "@type": "WebSite",
    "name": "American Glass Experts Inc.",
    "url": "https://www.americanglassexperts.us/"
  }},
  "breadcrumb": {{
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://www.americanglassexperts.us/"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "Services",
        "item": "https://www.americanglassexperts.us/services"
      }},
      {{
        "@type": "ListItem",
        "position": 3,
        "name": "{page['name']}",
        "item": "{url}"
      }}
    ]
  }}
}}</script>\n'''

    # Insert before the existing <script type="application/ld+json"> on the Service schema line
    old_tag = '<script type="application/ld+json">{'
    new_content = content.replace(old_tag, schema_block + old_tag, 1)

    if new_content == content:
        print(f"WARNING: Could not find insertion point in {page['file']}")
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"  Updated: {page['file']}")

print("Done.")
