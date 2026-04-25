#!/usr/bin/env python3
"""
Fix geo coordinates in all city HTML pages.
All pages currently have Reseda's coords (34.2005, -118.5339).
Replace with actual city-center coordinates.
"""

import re
import os

# City slug → (latitude, longitude)
CITY_COORDS = {
    "adelanto": (34.5825, -117.4328),
    "agoura-hills": (34.1531, -118.7618),
    "alhambra": (34.0953, -118.1270),
    "apple-valley": (34.5008, -117.1859),
    "arleta": (34.2459, -118.4240),
    "azusa": (34.1336, -117.9076),
    "baldwin-park": (34.0853, -117.9609),
    "banning": (33.9253, -116.8761),
    "beaumont": (33.9297, -116.9772),
    "bell-canyon": (34.2020, -118.7112),
    "big-bear-lake": (34.2439, -116.9114),
    "burbank": (34.1808, -118.3090),
    "calabasas": (34.1575, -118.6389),
    "calimesa": (34.0017, -117.0597),
    "camarillo": (34.2164, -119.0376),
    "canoga-park": (34.2008, -118.5978),
    "canyon-lake": (33.6839, -117.2706),
    "carson": (33.8317, -118.2820),
    "cathedral-city": (33.7797, -116.4653),
    "chatsworth": (34.2570, -118.6040),
    "chino": (34.0122, -117.6889),
    "chino-hills": (33.9939, -117.7325),
    "claremont": (34.0967, -117.7198),
    "coachella": (33.6803, -116.1739),
    "colton": (34.0739, -117.3136),
    "compton": (33.8958, -118.2201),
    "corona": (33.8753, -117.5664),
    "covina": (34.0900, -117.8903),
    "culver-city": (34.0211, -118.3965),
    "desert-hot-springs": (33.9611, -116.5017),
    "diamond-bar": (34.0289, -117.8103),
    "downey": (33.9400, -118.1328),
    "duarte": (34.1394, -117.9773),
    "eastvale": (33.9528, -117.5814),
    "el-monte": (34.0686, -118.0275),
    "el-segundo": (33.9192, -118.4165),
    "encino": (34.1584, -118.5009),
    "fillmore": (34.3992, -118.9178),
    "fontana": (34.0922, -117.4350),
    "gardena": (33.8883, -118.3089),
    "glendale": (34.1425, -118.2551),
    "glendora": (34.1361, -117.8653),
    "granada-hills": (34.2817, -118.5040),
    "grand-terrace": (34.0333, -117.3128),
    "hawthorne": (33.9164, -118.3525),
    "hemet": (33.7475, -116.9719),
    "hesperia": (34.4264, -117.3009),
    "hidden-hills": (34.1706, -118.6656),
    "indian-wells": (33.7181, -116.3411),
    "indio": (33.7206, -116.2156),
    "inglewood": (33.9617, -118.3531),
    "jurupa-valley": (33.9972, -117.4854),
    "la-puente": (34.0317, -117.9495),
    "la-quinta": (33.6633, -116.3100),
    "la-verne": (34.1008, -117.7678),
    "lake-elsinore": (33.6681, -117.3273),
    "lakewood": (33.8536, -118.1339),
    "loma-linda": (34.0483, -117.2611),
    "long-beach": (33.7701, -118.1937),
    "los-angeles": (34.0522, -118.2437),
    "malibu": (34.0259, -118.7798),
    "menifee": (33.6971, -117.1850),
    "mission-hills": (34.2681, -118.4674),
    "monrovia": (34.1442, -117.9992),
    "montclair": (34.0775, -117.6892),
    "montebello": (34.0159, -118.1134),
    "monterey-park": (34.0625, -118.1228),
    "moorpark": (34.2858, -118.8817),
    "moreno-valley": (33.9375, -117.2306),
    "murrieta": (33.5539, -117.2139),
    "newbury-park": (34.1847, -118.9134),
    "norco": (33.9289, -117.5489),
    "north-hills": (34.2353, -118.4787),
    "north-hollywood": (34.1872, -118.3800),
    "northridge": (34.2286, -118.5355),
    "oak-park": (34.1817, -118.7609),
    "ontario": (34.0633, -117.6509),
    "oxnard": (34.1975, -119.1771),
    "pacific-palisades": (34.0769, -118.5265),
    "pacoima": (34.2686, -118.4048),
    "palm-desert": (33.7222, -116.3744),
    "palm-springs": (33.8303, -116.5453),
    "panorama-city": (34.2233, -118.4462),
    "pasadena": (34.1478, -118.1445),
    "perris": (33.7825, -117.2286),
    "pico-rivera": (33.9828, -118.0967),
    "pomona": (34.0553, -117.7500),
    "port-hueneme": (34.1478, -119.1951),
    "rancho-cucamonga": (34.1064, -117.5931),
    "rancho-mirage": (33.7400, -116.4128),
    "redlands": (34.0556, -117.1825),
    "reseda": (34.2005, -118.5359),  # business address — keep exact
    "rialto": (34.1064, -117.3703),
    "riverside": (33.9533, -117.3961),
    "rubidoux": (33.9975, -117.4028),
    "san-bernardino": (34.1083, -117.2898),
    "san-dimas": (34.1067, -117.8067),
    "san-fernando": (34.2819, -118.4389),
    "san-gabriel": (34.0961, -118.1058),
    "san-jacinto": (33.7836, -116.9589),
    "san-marino": (34.1211, -118.1067),
    "santa-clarita": (34.3917, -118.5426),
    "santa-monica": (34.0195, -118.4912),
    "santa-paula": (34.3542, -119.0595),
    "sherman-oaks": (34.1511, -118.4489),
    "simi-valley": (34.2694, -118.7815),
    "south-pasadena": (34.1161, -118.1512),
    "studio-city": (34.1394, -118.3959),
    "sun-city": (33.7261, -117.1989),
    "sylmar": (34.3083, -118.4512),
    "tarzana": (34.1669, -118.5495),
    "temecula": (33.4936, -117.1484),
    "temple-city": (34.1067, -118.0578),
    "thousand-oaks": (34.1706, -118.8376),
    "topanga-canyon": (34.0931, -118.5998),
    "torrance": (33.8358, -118.3406),
    "upland": (34.0975, -117.6484),
    "valley-village": (34.1681, -118.3936),
    "van-nuys": (34.1897, -118.4489),
    "ventura": (34.2747, -119.2290),
    "victorville": (34.5361, -117.2928),
    "walnut": (34.0214, -117.8656),
    "west-covina": (34.0686, -117.9390),
    "west-hills": (34.2008, -118.6643),
    "westlake-village": (34.1469, -118.8198),
    "whittier": (33.9792, -118.0328),
    "wildomar": (33.5989, -117.2794),
    "winchester": (33.7061, -117.0869),
    "winnetka": (34.2131, -118.5740),
    "woodland-hills": (34.1684, -118.6059),
    "yucaipa": (34.0336, -117.0431),
}

# Regex to match the GeoCoordinates block (handles whitespace variations)
GEO_PATTERN = re.compile(
    r'("@type":\s*"GeoCoordinates",\s*\n\s*"latitude":\s*)[\d.]+(\s*,\s*\n\s*"longitude":\s*)[\d.-]+',
    re.MULTILINE
)

def fix_file(slug, lat, lng):
    path = f"{slug}.html"
    if not os.path.exists(path):
        return False
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Count how many GeoCoordinates blocks exist
    matches = list(GEO_PATTERN.finditer(content))
    if not matches:
        print(f"  SKIP {slug} — no GeoCoordinates found")
        return False

    # Replace ALL occurrences (some pages have 2-3 schema blocks)
    new_content = GEO_PATTERN.sub(
        lambda m: f'{m.group(1)}{lat}{m.group(2)}{lng}',
        content
    )

    if new_content == content:
        print(f"  SKIP {slug} — already correct or no change")
        return False

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"  FIXED {slug}: ({lat}, {lng}) — {len(matches)} block(s)")
    return True

fixed = 0
skipped = 0
for slug, (lat, lng) in sorted(CITY_COORDS.items()):
    result = fix_file(slug, lat, lng)
    if result:
        fixed += 1
    else:
        skipped += 1

print(f"\nDone: {fixed} fixed, {skipped} skipped")
