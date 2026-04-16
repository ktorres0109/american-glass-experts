#!/usr/bin/env python3
"""
Add og:image + twitter card to all HTML files.

Pages with existing og:type  → insert og:image + twitter after og:type line
City pages (no og: tags)     → insert full og block + twitter after canonical
"""
import os
import re
import glob

BASE = os.path.dirname(os.path.abspath(__file__))
OG_IMAGE_URL = "https://www.americanglassexperts.us/logo-icon.png"

OG_IMAGE_TAGS = (
    '  <meta property="og:image" content="' + OG_IMAGE_URL + '" />\n'
    '  <meta property="og:image:width" content="390" />\n'
    '  <meta property="og:image:height" content="380" />\n'
    '  <meta name="twitter:card" content="summary" />\n'
    '  <meta name="twitter:image" content="' + OG_IMAGE_URL + '" />\n'
)


def build_og_block(title, description, canonical):
    """Full og block for city pages that have none."""
    return (
        f'  <meta property="og:title" content="{title}" />\n'
        f'  <meta property="og:description" content="{description}" />\n'
        f'  <meta property="og:url" content="{canonical}" />\n'
        f'  <meta property="og:type" content="website" />\n'
        f'  <meta property="og:image" content="{OG_IMAGE_URL}" />\n'
        f'  <meta property="og:image:width" content="390" />\n'
        f'  <meta property="og:image:height" content="380" />\n'
        f'  <meta name="twitter:card" content="summary" />\n'
        f'  <meta name="twitter:image" content="{OG_IMAGE_URL}" />\n'
    )


def process(path):
    with open(path, encoding='utf-8') as f:
        content = f.read()

    if 'og:image' in content:
        return 'skip'

    # Pages with existing og:type — just add image + twitter after it
    og_type_match = re.search(
        r'(<meta property="og:type" content="[^"]*" />)', content
    )
    if og_type_match:
        old = og_type_match.group(1)
        content = content.replace(old, old + '\n' + OG_IMAGE_TAGS, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return 'og:type insert'

    # City pages — extract title/desc/canonical and build full og block
    title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
    desc_m = re.search(r'<meta name="description" content="([^"]+)"', content)
    canon_m = re.search(r'<link rel="canonical" href="([^"]+)"', content)

    if not (title_m and desc_m and canon_m):
        return 'no-match'

    title = title_m.group(1).replace('&amp;', '&')
    description = desc_m.group(1)
    canonical = canon_m.group(1)

    og_block = build_og_block(title, description, canonical)

    # Insert after canonical line
    canon_line = canon_m.group(0)
    content = content.replace(canon_line, canon_line + '\n' + og_block, 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return 'full og insert'


if __name__ == '__main__':
    patterns = [
        f'{BASE}/*.html',
        f'{BASE}/blog/*.html',
    ]
    files = []
    for p in patterns:
        files.extend(glob.glob(p))

    counts = {}
    for path in sorted(files):
        result = process(path)
        counts[result] = counts.get(result, 0) + 1
        if result != 'skip':
            print(f'  {result}: {os.path.relpath(path, BASE)}')

    print(f'\nDone: {counts}')
