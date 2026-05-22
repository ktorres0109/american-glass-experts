#!/usr/bin/env python3
"""Remove <section class="contact-strip">...</section> from HTML files."""
import re, sys, os

ROOT = "/Users/kel/Documents/projects/american-glass-experts"

# Matches the entire contact-strip section including trailing blank lines
STRIP_RE = re.compile(
    r'\n?[ \t]*<section class="contact-strip">.*?</section>\n?',
    re.DOTALL
)

files = sys.argv[1:]  # pass file paths as args
changed = 0
for path in files:
    with open(path, encoding="utf-8") as f:
        content = f.read()
    new = STRIP_RE.sub('\n', content)
    if new != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        changed += 1
        print(f"  DONE: {os.path.basename(path)}")
    else:
        print(f"  SKIP: {os.path.basename(path)}")
print(f"\n{changed} files changed.")
