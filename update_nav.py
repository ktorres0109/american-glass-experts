#!/usr/bin/env python3
"""
Update nav across all HTML files to add Services dropdown with service page links.
Also adds FAQ schema to index.html.
"""
import os
import glob

DROPDOWN_CSS = """
.nav-dropdown { position: relative; }
.nav-sub { display: none; position: absolute; top: 100%; left: 0; min-width: 210px; background: var(--bg-nav); border: 1px solid var(--border); border-radius: 8px; padding: 6px; box-shadow: var(--sh-md); z-index: 1000; list-style: none; margin: 0; }
.nav-dropdown:hover .nav-sub { display: block; }
.nav-sub li { margin: 0; padding: 0; }
.nav-sub li a { display: block; padding: 8px 12px; border-radius: 6px; font-size: .82rem; color: var(--text); white-space: nowrap; font-weight: 400; }
.nav-sub li a:hover { background: var(--bg-soft); color: var(--blue); }"""

CSS_ANCHOR = ".nav-links a.active { color: var(--blue); font-weight: 600; }"

# Desktop nav replacements
DESKTOP_SERVICES_PATTERNS = [
    # city pages + index.html (indented)
    ("      <li><a href=\"/services\">Services</a></li>",
     "      <li class=\"nav-dropdown\"><a href=\"/services\">Services ▾</a><ul class=\"nav-sub\">"
     "<li><a href=\"/shower-enclosures\">Shower Enclosures</a></li>"
     "<li><a href=\"/window-repair\">Window Repair</a></li>"
     "<li><a href=\"/storefront-glass\">Storefront Glass</a></li>"
     "<li><a href=\"/custom-mirrors\">Custom Mirrors</a></li>"
     "<li><a href=\"/emergency-glass\">Emergency Glass</a></li>"
     "</ul></li>"),
    # blog pages (no indent)
    ("<li><a href=\"/services\">Services</a></li>",
     "<li class=\"nav-dropdown\"><a href=\"/services\">Services ▾</a><ul class=\"nav-sub\">"
     "<li><a href=\"/shower-enclosures\">Shower Enclosures</a></li>"
     "<li><a href=\"/window-repair\">Window Repair</a></li>"
     "<li><a href=\"/storefront-glass\">Storefront Glass</a></li>"
     "<li><a href=\"/custom-mirrors\">Custom Mirrors</a></li>"
     "<li><a href=\"/emergency-glass\">Emergency Glass</a></li>"
     "</ul></li>"),
    # service pages (has active class, no space before class)
    ("<li><a href=\"/services\"class=\"active\">Services</a></li>",
     "<li class=\"nav-dropdown\"><a href=\"/services\" class=\"active\">Services ▾</a><ul class=\"nav-sub\">"
     "<li><a href=\"/shower-enclosures\">Shower Enclosures</a></li>"
     "<li><a href=\"/window-repair\">Window Repair</a></li>"
     "<li><a href=\"/storefront-glass\">Storefront Glass</a></li>"
     "<li><a href=\"/custom-mirrors\">Custom Mirrors</a></li>"
     "<li><a href=\"/emergency-glass\">Emergency Glass</a></li>"
     "</ul></li>"),
]

# Mobile nav: nav-mobile pattern (city pages + index.html)
MOBILE_NAV_OLD = '  <a href="/services">Services <span>→</span></a>'
MOBILE_NAV_NEW = ('  <a href="/services">Services <span>→</span></a>\n'
                  '  <a href="/shower-enclosures" style="padding-left:28px;font-size:.85rem;opacity:.85;">Shower Enclosures <span>→</span></a>\n'
                  '  <a href="/window-repair" style="padding-left:28px;font-size:.85rem;opacity:.85;">Window Repair <span>→</span></a>\n'
                  '  <a href="/storefront-glass" style="padding-left:28px;font-size:.85rem;opacity:.85;">Storefront Glass <span>→</span></a>\n'
                  '  <a href="/custom-mirrors" style="padding-left:28px;font-size:.85rem;opacity:.85;">Custom Mirrors <span>→</span></a>\n'
                  '  <a href="/emergency-glass" style="padding-left:28px;font-size:.85rem;opacity:.85;">Emergency Glass <span>→</span></a>')

# Mobile nav: nav-mobile-menu pattern (service + blog pages)
MOBILE_MENU_SERVICES_OLD = '<li><a href="/services">Services</a></li>'
MOBILE_MENU_SERVICES_NEW = ('<li><a href="/services">Services</a></li>\n'
                             '<li><a href="/shower-enclosures" style="padding-left:20px;font-size:.85rem;opacity:.85;">Shower Enclosures</a></li>\n'
                             '<li><a href="/window-repair" style="padding-left:20px;font-size:.85rem;opacity:.85;">Window Repair</a></li>\n'
                             '<li><a href="/storefront-glass" style="padding-left:20px;font-size:.85rem;opacity:.85;">Storefront Glass</a></li>\n'
                             '<li><a href="/custom-mirrors" style="padding-left:20px;font-size:.85rem;opacity:.85;">Custom Mirrors</a></li>\n'
                             '<li><a href="/emergency-glass" style="padding-left:20px;font-size:.85rem;opacity:.85;">Emergency Glass</a></li>')

# Service pages mobile menu (active class)
MOBILE_MENU_SERVICES_ACTIVE_OLD = '<li><a href="/services"class="active">Services</a></li>'
MOBILE_MENU_SERVICES_ACTIVE_NEW = ('<li><a href="/services" class="active">Services</a></li>\n'
                                    '<li><a href="/shower-enclosures" style="padding-left:20px;font-size:.85rem;opacity:.85;">Shower Enclosures</a></li>\n'
                                    '<li><a href="/window-repair" style="padding-left:20px;font-size:.85rem;opacity:.85;">Window Repair</a></li>\n'
                                    '<li><a href="/storefront-glass" style="padding-left:20px;font-size:.85rem;opacity:.85;">Storefront Glass</a></li>\n'
                                    '<li><a href="/custom-mirrors" style="padding-left:20px;font-size:.85rem;opacity:.85;">Custom Mirrors</a></li>\n'
                                    '<li><a href="/emergency-glass" style="padding-left:20px;font-size:.85rem;opacity:.85;">Emergency Glass</a></li>')


FAQ_SCHEMA = """
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "How much does a frameless shower enclosure cost in Los Angeles?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Frameless shower enclosures in Los Angeles typically range from $1,200 to $3,500 depending on size, glass thickness, and hardware finish. American Glass Experts provides free in-home estimates — call (805) 750-6471."
        }
      },
      {
        "@type": "Question",
        "name": "Do you offer emergency glass repair?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. American Glass Experts provides emergency glass repair and board-up services across Los Angeles, Ventura, San Bernardino, and Riverside Counties. Same-day response available — call (805) 750-6471 any time."
        }
      },
      {
        "@type": "Question",
        "name": "Are you a licensed glass contractor in California?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. American Glass Experts holds a California C-17 Glazing Contractor License (CSLB #1125850). We are fully licensed, bonded, and insured."
        }
      },
      {
        "@type": "Question",
        "name": "What areas do you serve?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "We serve Los Angeles County, Ventura County, San Bernardino County, and Riverside County — over 130 cities across Southern California including Los Angeles, Thousand Oaks, Burbank, Pasadena, Ontario, Riverside, and Palm Springs."
        }
      },
      {
        "@type": "Question",
        "name": "How long does glass installation take?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Most residential window replacements and mirror installations are completed in one day. Custom shower enclosures typically require a measurement visit followed by a 1–2 day fabrication and installation window. Storefront glass depends on project scope."
        }
      },
      {
        "@type": "Question",
        "name": "Do you replace foggy or broken double-pane windows?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Yes. We replace foggy, cracked, or broken insulated glass units (IGUs) without replacing the entire window frame. This restores clarity and energy efficiency at a fraction of full window replacement cost."
        }
      }
    ]
  }
  </script>"""


def process_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already updated
    if 'nav-dropdown' in content:
        return False

    changed = False

    # 1. Add dropdown CSS
    if CSS_ANCHOR in content:
        content = content.replace(CSS_ANCHOR, CSS_ANCHOR + DROPDOWN_CSS)
        changed = True

    # 2. Desktop nav — try each pattern
    for old, new in DESKTOP_SERVICES_PATTERNS:
        if old in content:
            content = content.replace(old, new)
            changed = True
            break

    # 3. Mobile nav
    if MOBILE_NAV_OLD in content:
        content = content.replace(MOBILE_NAV_OLD, MOBILE_NAV_NEW)
        changed = True
    elif MOBILE_MENU_SERVICES_ACTIVE_OLD in content:
        content = content.replace(MOBILE_MENU_SERVICES_ACTIVE_OLD, MOBILE_MENU_SERVICES_ACTIVE_NEW)
        changed = True
    elif MOBILE_MENU_SERVICES_OLD in content:
        # Only replace first occurrence (in nav-mobile-menu), not the desktop nav one
        # The desktop nav was already replaced above, so remaining occurrence is in mobile menu
        content = content.replace(MOBILE_MENU_SERVICES_OLD, MOBILE_MENU_SERVICES_NEW, 1)
        changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)

    return changed


def add_faq_schema(path):
    """Add FAQPage schema to index.html after the existing ld+json script."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'FAQPage' in content:
        print("FAQ schema already present, skipping")
        return False

    # Insert after closing </script> of the first ld+json block
    marker = '  </script>\n\n  <link rel="preconnect"'
    if marker not in content:
        print(f"WARNING: marker not found in {path}")
        return False

    content = content.replace(marker, '  </script>\n' + FAQ_SCHEMA + '\n\n  <link rel="preconnect"', 1)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return True


if __name__ == '__main__':
    base = '/tmp/ags'
    files = glob.glob(f'{base}/*.html') + glob.glob(f'{base}/blog/*.html')

    updated = 0
    skipped = 0
    for path in sorted(files):
        result = process_file(path)
        if result:
            updated += 1
        else:
            skipped += 1
            print(f"  SKIP (already updated or no match): {os.path.basename(path)}")

    print(f"\nNav update: {updated} files updated, {skipped} skipped")

    # FAQ schema
    faq_result = add_faq_schema(f'{base}/index.html')
    print(f"FAQ schema: {'added' if faq_result else 'already present'}")
