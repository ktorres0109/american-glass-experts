#!/usr/bin/env python3
"""
Add noindex to city pages that are too far from Reseda for local pack potential.
These waste crawl budget. Add <meta name="robots" content="noindex,follow"> to head.
"""
import re, os

# Cities 50+ miles from Reseda with near-zero local pack potential
NOINDEX_SLUGS = [
    "adelanto", "apple-valley", "banning", "beaumont", "big-bear-lake",
    "calimesa", "cathedral-city", "coachella", "desert-hot-springs",
    "hemet", "hesperia", "indian-wells", "indio", "la-quinta",
    "palm-desert", "palm-springs", "perris", "rancho-mirage",
    "san-jacinto", "sun-city", "temecula", "victorville",
    "wildomar", "winchester", "yucaipa",
]

ROBOTS_META = '<meta name="robots" content="noindex,follow" />'
INSERT_AFTER = re.compile(r'(<link rel="canonical"[^>]+>)')

updated = 0
for slug in NOINDEX_SLUGS:
    path = f"{slug}.html"
    if not os.path.exists(path):
        continue
    with open(path) as f:
        content = f.read()
    if 'noindex' in content:
        print(f"  SKIP {slug} — already noindex")
        continue
    new_content = INSERT_AFTER.sub(r'\1\n  ' + ROBOTS_META, content, count=1)
    if new_content == content:
        print(f"  WARN {slug} — canonical not found")
        continue
    with open(path, "w") as f:
        f.write(new_content)
    print(f"  NOINDEX {slug}")
    updated += 1

print(f"\nDone: {updated} pages noindexed")
