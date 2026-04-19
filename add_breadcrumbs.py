#!/usr/bin/env python3
"""Add BreadcrumbList JSON-LD to all city pages after the twitter:image meta tag."""
import os
import re
import glob

# Non-city pages to exclude
EXCLUDE = {
    'index.html', 'about.html', 'contact.html', 'gallery.html',
    'services.html', 'service-areas.html', 'privacy-policy.html',
    'review.html', 'shower-enclosures.html', 'window-repair.html',
    'storefront-glass.html', 'custom-mirrors.html', 'emergency-glass.html'
}

BASE = '/tmp/age'

city_files = [
    f for f in glob.glob(os.path.join(BASE, '*.html'))
    if os.path.basename(f) not in EXCLUDE
]

TWITTER_IMG_PATTERN = re.compile(
    r'(<meta name="twitter:image"[^>]*?>)', re.IGNORECASE
)

H1_PATTERN = re.compile(r'<h1[^>]*?>(.*?)</h1>', re.DOTALL | re.IGNORECASE)
TITLE_PATTERN = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)

updated = 0
skipped = 0

for fpath in sorted(city_files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has BreadcrumbList
    if 'BreadcrumbList' in content:
        skipped += 1
        continue

    slug = os.path.basename(fpath).replace('.html', '')

    # Extract city name from H1 (fallback to title)
    h1_match = H1_PATTERN.search(content)
    if h1_match:
        # Strip inner HTML tags
        city_name = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        # Remove trailing "Glass Repair..." suffix if present, keep just city
        # H1 is typically "Glass Repair & Installation in CITYNAME, CA"
        city_match = re.search(r'\bin\s+([A-Za-z\s\-]+),?\s*CA', city_name)
        if city_match:
            city_name = city_match.group(1).strip()
        else:
            # Just clean it up
            city_name = city_name.split(',')[0].strip()
    else:
        # Fallback: title tag
        title_match = TITLE_PATTERN.search(content)
        if title_match:
            title = title_match.group(1)
            city_match = re.search(r'\bin\s+([A-Za-z\s\-]+),?\s*CA', title)
            if city_match:
                city_name = city_match.group(1).strip()
            else:
                city_name = slug.replace('-', ' ').title()
        else:
            city_name = slug.replace('-', ' ').title()

    breadcrumb_json = f'''  <script type="application/ld+json">
{{
  "@context": "https://schema.org",
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
      "name": "Service Areas",
      "item": "https://www.americanglassexperts.us/service-areas"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{city_name}",
      "item": "https://www.americanglassexperts.us/{slug}"
    }}
  ]
}}
  </script>'''

    # Insert after the twitter:image meta tag
    new_content = TWITTER_IMG_PATTERN.sub(
        r'\1\n' + breadcrumb_json,
        content,
        count=1
    )

    if new_content == content:
        print(f"WARNING: Could not find twitter:image in {slug}")
        skipped += 1
        continue

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    updated += 1
    print(f"  Updated: {slug} → {city_name}")

print(f"\nDone. Updated: {updated}, Skipped (already had breadcrumb or no match): {skipped}")
