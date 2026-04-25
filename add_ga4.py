#!/usr/bin/env python3
"""
Add GA4 tracking snippet to all HTML pages.
Usage: python3 add_ga4.py G-XXXXXXXXXX
"""
import sys, os, glob

if len(sys.argv) != 2 or not sys.argv[1].startswith('G-'):
    print("Usage: python3 add_ga4.py G-XXXXXXXXXX")
    sys.exit(1)

MEASUREMENT_ID = sys.argv[1]

GA4_SNIPPET = f"""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{MEASUREMENT_ID}');
</script>"""

# All HTML files — root + blog/
html_files = glob.glob("*.html") + glob.glob("blog/*.html")

updated = 0
skipped = 0
for path in sorted(html_files):
    with open(path) as f:
        content = f.read()
    if MEASUREMENT_ID in content or 'googletagmanager' in content:
        skipped += 1
        continue
    # Insert just before </head>
    if '</head>' not in content:
        print(f"  WARN {path} — no </head> found")
        continue
    new_content = content.replace('</head>', GA4_SNIPPET + '\n</head>', 1)
    with open(path, "w") as f:
        f.write(new_content)
    updated += 1

print(f"GA4 ({MEASUREMENT_ID}) added to {updated} pages, {skipped} already had tracking.")
