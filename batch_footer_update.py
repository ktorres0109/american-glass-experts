#!/usr/bin/env python3
"""
Adds Terms + Privacy links to footer-bottom across all HTML files.
Handles both single-line and multiline variants of the Sitemap/Service Areas div.
"""
import os
import re
import glob

BASE = "/Users/kel/Documents/projects/american-glass-experts"

# Pattern: matches the sitemap+service-areas div in both multiline and single-line forms
# The div has style="display:flex;gap:20px;" and contains the two links
OLD_PATTERN = re.compile(
    r'<div style="display:flex;gap:20px;">\s*'
    r'<a href="sitemap\.xml">Sitemap</a>\s*'
    r'<a href="/service-areas">Service Areas</a>\s*'
    r'</div>',
    re.DOTALL
)

NEW_SNIPPET = '<div style="display:flex;gap:20px;"><a href="/terms-of-service">Terms</a><a href="/privacy-policy">Privacy</a><a href="sitemap.xml">Sitemap</a><a href="/service-areas">Service Areas</a></div>'

html_files = glob.glob(os.path.join(BASE, "**/*.html"), recursive=True) + \
             glob.glob(os.path.join(BASE, "*.html"))
# deduplicate
html_files = list(set(html_files))

# skip generated/backup files
SKIP = {"batch_footer_update.py", "batch_nav_update.py"}

matched = []
for f in sorted(html_files):
    if any(s in f for s in SKIP):
        continue
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    if OLD_PATTERN.search(content):
        matched.append(f)

print(f"DRY RUN: {len(matched)} files match the old footer pattern")
for f in matched[:10]:
    print(f"  {os.path.relpath(f, BASE)}")
if len(matched) > 10:
    print(f"  ... and {len(matched)-10} more")

confirm = input("\nProceed with replacement? (yes/no): ").strip().lower()
if confirm != "yes":
    print("Aborted.")
    exit(0)

changed = 0
errors = []
for f in matched:
    try:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
        new_content = OLD_PATTERN.sub(NEW_SNIPPET, content)
        if new_content != content:
            with open(f, "w", encoding="utf-8") as fh:
                fh.write(new_content)
            changed += 1
    except Exception as e:
        errors.append((f, str(e)))

print(f"\nDone: {changed} files updated")
if errors:
    print(f"Errors ({len(errors)}):")
    for f, e in errors:
        print(f"  {f}: {e}")
