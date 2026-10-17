#!/usr/bin/env python3
"""
Generate unique meta descriptions for all 138 residential city pages.
Run dry-run first, then write.
"""

import os, re, glob, sys

BASE = '/Users/kel/Documents/projects/american-glass-experts'

# (display_name, county, region)
# regions: sfv_close, sfv_far, la_west, la_east, la_south, ventura, sb, riverside, desert
CITIES = {
    'adelanto':          ('Adelanto',          'San Bernardino County', 'high_desert'),
    'agoura-hills':      ('Agoura Hills',       'Los Angeles County',    'la_west'),
    'alhambra':          ('Alhambra',           'Los Angeles County',    'la_east'),
    'apple-valley':      ('Apple Valley',       'San Bernardino County', 'high_desert'),
    'arcadia':           ('Arcadia',            'Los Angeles County',    'la_east'),
    'arleta':            ('Arleta',             'Los Angeles County',    'sfv_far'),
    'azusa':             ('Azusa',              'Los Angeles County',    'la_east'),
    'baldwin-park':      ('Baldwin Park',       'Los Angeles County',    'la_east'),
    'banning':           ('Banning',            'Riverside County',      'riverside'),
    'beaumont':          ('Beaumont',           'Riverside County',      'riverside'),
    'bell-canyon':       ('Bell Canyon',        'Los Angeles County',    'la_west'),
    'bellflower':        ('Bellflower',         'Los Angeles County',    'la_south'),
    'beverly-hills':     ('Beverly Hills',      'Los Angeles County',    'la_west'),
    'big-bear-lake':     ('Big Bear Lake',      'San Bernardino County', 'mountain'),
    'burbank':           ('Burbank',            'Los Angeles County',    'sfv_far'),
    'calabasas':         ('Calabasas',          'Los Angeles County',    'la_west'),
    'calimesa':          ('Calimesa',           'Riverside County',      'riverside'),
    'camarillo':         ('Camarillo',          'Ventura County',        'ventura'),
    'canoga-park':       ('Canoga Park',        'Los Angeles County',    'sfv_close'),
    'canyon-lake':       ('Canyon Lake',        'Riverside County',      'riverside'),
    'carson':            ('Carson',             'Los Angeles County',    'la_south'),
    'cathedral-city':    ('Cathedral City',     'Riverside County',      'desert'),
    'cerritos':          ('Cerritos',           'Los Angeles County',    'la_south'),
    'chatsworth':        ('Chatsworth',         'Los Angeles County',    'sfv_close'),
    'chino-hills':       ('Chino Hills',        'San Bernardino County', 'sb'),
    'chino':             ('Chino',              'San Bernardino County', 'sb'),
    'claremont':         ('Claremont',          'Los Angeles County',    'la_east'),
    'coachella':         ('Coachella',          'Riverside County',      'desert'),
    'colton':            ('Colton',             'San Bernardino County', 'sb'),
    'compton':           ('Compton',            'Los Angeles County',    'la_south'),
    'corona':            ('Corona',             'Riverside County',      'riverside'),
    'covina':            ('Covina',             'Los Angeles County',    'la_east'),
    'culver-city':       ('Culver City',        'Los Angeles County',    'la_west'),
    'desert-hot-springs':('Desert Hot Springs', 'Riverside County',      'desert'),
    'diamond-bar':       ('Diamond Bar',        'Los Angeles County',    'la_east'),
    'downey':            ('Downey',             'Los Angeles County',    'la_south'),
    'duarte':            ('Duarte',             'Los Angeles County',    'la_east'),
    'eastvale':          ('Eastvale',           'Riverside County',      'riverside'),
    'el-monte':          ('El Monte',           'Los Angeles County',    'la_east'),
    'el-segundo':        ('El Segundo',         'Los Angeles County',    'la_west'),
    'encino':            ('Encino',             'Los Angeles County',    'sfv_far'),
    'fillmore':          ('Fillmore',           'Ventura County',        'ventura'),
    'fontana':           ('Fontana',            'San Bernardino County', 'sb'),
    'gardena':           ('Gardena',            'Los Angeles County',    'la_south'),
    'glendale':          ('Glendale',           'Los Angeles County',    'sfv_far'),
    'glendora':          ('Glendora',           'Los Angeles County',    'la_east'),
    'granada-hills':     ('Granada Hills',      'Los Angeles County',    'sfv_close'),
    'grand-terrace':     ('Grand Terrace',      'San Bernardino County', 'sb'),
    'hawthorne':         ('Hawthorne',          'Los Angeles County',    'la_south'),
    'hemet':             ('Hemet',              'Riverside County',      'riverside'),
    'hesperia':          ('Hesperia',           'San Bernardino County', 'high_desert'),
    'hidden-hills':      ('Hidden Hills',       'Los Angeles County',    'la_west'),
    'indian-wells':      ('Indian Wells',       'Riverside County',      'desert'),
    'indio':             ('Indio',              'Riverside County',      'desert'),
    'inglewood':         ('Inglewood',          'Los Angeles County',    'la_west'),
    'jurupa-valley':     ('Jurupa Valley',      'Riverside County',      'riverside'),
    'la-habra':          ('La Habra',           'Los Angeles County',    'la_east'),
    'la-puente':         ('La Puente',          'Los Angeles County',    'la_east'),
    'la-quinta':         ('La Quinta',          'Riverside County',      'desert'),
    'la-verne':          ('La Verne',           'Los Angeles County',    'la_east'),
    'lake-elsinore':     ('Lake Elsinore',      'Riverside County',      'riverside'),
    'lakewood':          ('Lakewood',           'Los Angeles County',    'la_south'),
    'loma-linda':        ('Loma Linda',         'San Bernardino County', 'sb'),
    'long-beach':        ('Long Beach',         'Los Angeles County',    'la_south'),
    'los-angeles':       ('Los Angeles',        'Los Angeles County',    'la_west'),
    'malibu':            ('Malibu',             'Los Angeles County',    'la_west'),
    'menifee':           ('Menifee',            'Riverside County',      'riverside'),
    'mission-hills':     ('Mission Hills',      'Los Angeles County',    'sfv_close'),
    'monrovia':          ('Monrovia',           'Los Angeles County',    'la_east'),
    'montclair':         ('Montclair',          'San Bernardino County', 'sb'),
    'montebello':        ('Montebello',         'Los Angeles County',    'la_east'),
    'monterey-park':     ('Monterey Park',      'Los Angeles County',    'la_east'),
    'moorpark':          ('Moorpark',           'Ventura County',        'ventura'),
    'moreno-valley':     ('Moreno Valley',      'Riverside County',      'riverside'),
    'murrieta':          ('Murrieta',           'Riverside County',      'riverside'),
    'newbury-park':      ('Newbury Park',       'Ventura County',        'ventura'),
    'norco':             ('Norco',              'Riverside County',      'riverside'),
    'north-hills':       ('North Hills',        'Los Angeles County',    'sfv_close'),
    'north-hollywood':   ('North Hollywood',    'Los Angeles County',    'sfv_far'),
    'northridge':        ('Northridge',         'Los Angeles County',    'sfv_close'),
    'norwalk':           ('Norwalk',            'Los Angeles County',    'la_south'),
    'oak-park':          ('Oak Park',           'Ventura County',        'ventura'),
    'ontario':           ('Ontario',            'San Bernardino County', 'sb'),
    'oxnard':            ('Oxnard',             'Ventura County',        'ventura'),
    'pacific-palisades': ('Pacific Palisades',  'Los Angeles County',    'la_west'),
    'pacoima':           ('Pacoima',            'Los Angeles County',    'sfv_close'),
    'palm-desert':       ('Palm Desert',        'Riverside County',      'desert'),
    'palm-springs':      ('Palm Springs',       'Riverside County',      'desert'),
    'panorama-city':     ('Panorama City',      'Los Angeles County',    'sfv_close'),
    'pasadena':          ('Pasadena',           'Los Angeles County',    'la_east'),
    'perris':            ('Perris',             'Riverside County',      'riverside'),
    'pico-rivera':       ('Pico Rivera',        'Los Angeles County',    'la_east'),
    'pomona':            ('Pomona',             'Los Angeles County',    'la_east'),
    'port-hueneme':      ('Port Hueneme',       'Ventura County',        'ventura'),
    'rancho-cucamonga':  ('Rancho Cucamonga',   'San Bernardino County', 'sb'),
    'rancho-mirage':     ('Rancho Mirage',      'Riverside County',      'desert'),
    'redlands':          ('Redlands',           'San Bernardino County', 'sb'),
    'reseda':            ('Reseda',             'Los Angeles County',    'home'),
    'rialto':            ('Rialto',             'San Bernardino County', 'sb'),
    'riverside':         ('Riverside',          'Riverside County',      'riverside'),
    'rubidoux':          ('Rubidoux',           'Riverside County',      'riverside'),
    'san-bernardino':    ('San Bernardino',     'San Bernardino County', 'sb'),
    'san-dimas':         ('San Dimas',          'Los Angeles County',    'la_east'),
    'san-fernando':      ('San Fernando',       'Los Angeles County',    'sfv_far'),
    'san-gabriel':       ('San Gabriel',        'Los Angeles County',    'la_east'),
    'san-jacinto':       ('San Jacinto',        'Riverside County',      'riverside'),
    'san-marino':        ('San Marino',         'Los Angeles County',    'la_east'),
    'santa-clarita':     ('Santa Clarita',      'Los Angeles County',    'la_east'),
    'santa-monica':      ('Santa Monica',       'Los Angeles County',    'la_west'),
    'santa-paula':       ('Santa Paula',        'Ventura County',        'ventura'),
    'sherman-oaks':      ('Sherman Oaks',       'Los Angeles County',    'sfv_far'),
    'simi-valley':       ('Simi Valley',        'Ventura County',        'ventura'),
    'south-pasadena':    ('South Pasadena',     'Los Angeles County',    'la_east'),
    'studio-city':       ('Studio City',        'Los Angeles County',    'sfv_far'),
    'sun-city':          ('Sun City',           'Riverside County',      'riverside'),
    'sylmar':            ('Sylmar',             'Los Angeles County',    'sfv_close'),
    'tarzana':           ('Tarzana',            'Los Angeles County',    'sfv_close'),
    'temecula':          ('Temecula',           'Riverside County',      'riverside'),
    'temple-city':       ('Temple City',        'Los Angeles County',    'la_east'),
    'thousand-oaks':     ('Thousand Oaks',      'Ventura County',        'ventura'),
    'topanga-canyon':    ('Topanga Canyon',     'Los Angeles County',    'la_west'),
    'torrance':          ('Torrance',           'Los Angeles County',    'la_south'),
    'upland':            ('Upland',             'San Bernardino County', 'sb'),
    'valley-village':    ('Valley Village',     'Los Angeles County',    'sfv_far'),
    'van-nuys':          ('Van Nuys',           'Los Angeles County',    'sfv_close'),
    'ventura':           ('Ventura',            'Ventura County',        'ventura'),
    'victorville':       ('Victorville',        'San Bernardino County', 'high_desert'),
    'walnut':            ('Walnut',             'Los Angeles County',    'la_east'),
    'west-covina':       ('West Covina',        'Los Angeles County',    'la_east'),
    'west-hills':        ('West Hills',         'Los Angeles County',    'sfv_close'),
    'west-hollywood':    ('West Hollywood',     'Los Angeles County',    'la_west'),
    'westlake-village':  ('Westlake Village',   'Los Angeles County',    'la_west'),
    'whittier':          ('Whittier',           'Los Angeles County',    'la_south'),
    'wildomar':          ('Wildomar',           'Riverside County',      'riverside'),
    'winchester':        ('Winchester',         'Riverside County',      'riverside'),
    'winnetka':          ('Winnetka',           'Los Angeles County',    'sfv_close'),
    'woodland-hills':    ('Woodland Hills',     'Los Angeles County',    'sfv_close'),
    'yucaipa':           ('Yucaipa',            'San Bernardino County', 'sb'),
}

# Service phrase variants — short (2-3 items max)
SERVICES = [
    "shower enclosures, window repair, custom mirrors",
    "frameless showers, storefront glass, mirrors",
    "shower doors, window replacement, mirrors",
    "shower enclosures, storefronts, custom mirrors",
    "window repair, frameless showers, mirrors",
    "shower doors, dual-pane windows, custom mirrors",
    "shower enclosures, window installation, mirrors",
    "frameless showers, windows, storefront glass",
]

# CTA variants — short
CTAS = [
    "Free estimates. (805) 750-6471.",
    "Call (805) 750-6471.",
    "Free estimate. (805) 750-6471.",
    "(805) 750-6471.",
]

# License variants — short
LICENSES = [
    "C-17 Licensed.",
    "Licensed C-17 glazier.",
    "CSLB #1125850.",
    "C-17 contractor.",
]

def pick(lst, slug, offset=0):
    return lst[(hash(slug) + offset) % len(lst)]

def shorten(desc, max_len=155):
    """Progressively shorten a description that's too long."""
    replacements = [
        ("Licensed C-17 glazier.", "C-17 Licensed."),
        ("C-17 Licensed contractor.", "C-17 Licensed."),
        ("C-17 Licensed, CSLB #1125850.", "C-17 Licensed."),
        ("C-17 contractor.", "C-17 Licensed."),
        ("Free estimates. (805) 750-6471.", "(805) 750-6471."),
        ("Free estimate. (805) 750-6471.", "(805) 750-6471."),
        ("Call (805) 750-6471.", "(805) 750-6471."),
        (", Los Angeles County", ""),
        (", San Bernardino County", ""),
        (", Riverside County", ""),
        (", Ventura County", ""),
        (" for glass repair and installation", " for glass repair"),
        (", San Fernando Valley", ""),
    ]
    for old, new in replacements:
        if len(desc) <= max_len:
            break
        desc = desc.replace(old, new)
    return desc


def generate_description(slug, name, county, region):
    svc = pick(SERVICES, slug, 0)
    cta = pick(CTAS, slug, 1)
    lic = pick(LICENSES, slug, 2)

    if region == 'home':
        return shorten(f"Glass repair in our own backyard — American Glass Experts is based in Reseda. {svc.capitalize()}. {lic} {cta}")

    if region == 'sfv_close':
        templates = [
            f"Glass repair in {name} — we're based nearby in Reseda. {svc.capitalize()}. {lic} {cta}",
            f"{name} glass services from your local Reseda team. {svc.capitalize()}. {lic} {cta}",
            f"Glass contractor in {name}, minutes from our Reseda shop. {svc.capitalize()}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'sfv_far':
        templates = [
            f"Glass repair & installation in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"{name} glass contractor — {svc}. Based in Reseda, San Fernando Valley. {lic} {cta}",
            f"Serving {name} for {svc}. C-17 Licensed glazier based in Reseda. {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'la_west':
        templates = [
            f"Custom glass in {name} — {svc}. {lic} {cta}",
            f"Glass contractor serving {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"Glass repair in {name} — {svc}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'la_east':
        templates = [
            f"Glass repair & installation in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"Licensed glass contractor serving {name}. {svc.capitalize()}. {lic} {cta}",
            f"Glass services in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'la_south':
        templates = [
            f"Glass repair in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"Serving {name} for {svc}. {lic} {cta}",
            f"Glass contractor in {name}, {county} — {svc}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'ventura':
        templates = [
            f"Glass repair in {name}, Ventura County. {svc.capitalize()}. {lic} {cta}",
            f"Serving {name}, {county} for glass repair and installation. {svc.capitalize()}. {lic} {cta}",
            f"Licensed glass contractor in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'sb':
        templates = [
            f"Glass repair & installation in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"Glass contractor serving {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"Licensed glass services in {name}, San Bernardino County. {svc.capitalize()}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'riverside':
        templates = [
            f"Glass repair in {name}, Riverside County. {svc.capitalize()}. {lic} {cta}",
            f"Licensed glass contractor serving {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"Glass services in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'desert':
        templates = [
            f"Glass contractor in {name}, Riverside County. {svc.capitalize()}. {lic} {cta}",
            f"Glass repair & installation in {name}, {county}. {svc.capitalize()}. {lic} {cta}",
            f"Serving {name} for {svc}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'high_desert':
        templates = [
            f"Glass repair in {name}, San Bernardino County. {svc.capitalize()}. {lic} {cta}",
            f"Glass contractor serving {name}, {county}. {svc.capitalize()}. {lic} {cta}",
        ]
        return shorten(templates[hash(slug) % len(templates)])

    if region == 'mountain':
        return shorten(f"Glass repair and installation in {name}, {county}. {svc.capitalize()}. {lic} {cta}")

    # fallback
    return shorten(f"Glass repair & installation in {name}, {county}. {svc.capitalize()}. {lic} {cta}")


def update_file(filepath, slug, dry_run=True):
    name, county, region = CITIES[slug]
    new_desc = generate_description(slug, name, county, region)

    # Validate length
    if len(new_desc) > 160:
        print(f"  WARN: {slug} description {len(new_desc)} chars (>160): {new_desc}")

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match meta description tag
    pattern = r'(<meta name="description" content=")([^"]*)("/>|" />)'
    match = re.search(pattern, content)
    if not match:
        print(f"  SKIP: no meta description found in {slug}")
        return False

    old_desc = match.group(2)
    new_content = re.sub(pattern, rf'\g<1>{new_desc}\3', content, count=1)

    if dry_run:
        print(f"  {slug} ({len(new_desc)} chars):\n    OLD: {old_desc[:80]}...\n    NEW: {new_desc}")
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

    return True


def main():
    dry_run = '--write' not in sys.argv
    if dry_run:
        print("=== DRY RUN (pass --write to apply) ===\n")
    else:
        print("=== WRITING FILES ===\n")

    updated = 0
    skipped = 0
    too_long = 0

    for slug, (name, county, region) in sorted(CITIES.items()):
        filepath = os.path.join(BASE, f'{slug}.html')
        if not os.path.exists(filepath):
            print(f"  MISSING FILE: {slug}.html")
            skipped += 1
            continue

        desc = generate_description(slug, name, county, region)
        if len(desc) > 160:
            too_long += 1

        if update_file(filepath, slug, dry_run=dry_run):
            updated += 1
        else:
            skipped += 1

    print(f"\n{'DRY RUN' if dry_run else 'WRITTEN'}: {updated} files, {skipped} skipped, {too_long} over 160 chars")

    if dry_run:
        print("\nRun with --write to apply changes.")


if __name__ == '__main__':
    main()
