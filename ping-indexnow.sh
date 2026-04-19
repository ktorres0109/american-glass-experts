#!/usr/bin/env bash
# IndexNow submission for americanglassexperts.us
# Run after deploying changes to notify Bing/Yandex of updated URLs.
# Usage: ./ping-indexnow.sh

KEY="faa237c5f0e41eee3f2be30cfcc96af2"
HOST="www.americanglassexperts.us"
KEY_LOCATION="https://www.americanglassexperts.us/${KEY}.txt"

curl -X POST "https://api.indexnow.org/indexnow" \
  -H "Content-Type: application/json; charset=utf-8" \
  -d @- <<JSON
{
  "host": "${HOST}",
  "key": "${KEY}",
  "keyLocation": "${KEY_LOCATION}",
  "urlList": [
    "https://www.americanglassexperts.us/",
    "https://www.americanglassexperts.us/services",
    "https://www.americanglassexperts.us/contact",
    "https://www.americanglassexperts.us/gallery",
    "https://www.americanglassexperts.us/service-areas",
    "https://www.americanglassexperts.us/about",
    "https://www.americanglassexperts.us/blog",
    "https://www.americanglassexperts.us/shower-enclosures",
    "https://www.americanglassexperts.us/window-repair",
    "https://www.americanglassexperts.us/storefront-glass",
    "https://www.americanglassexperts.us/custom-mirrors",
    "https://www.americanglassexperts.us/emergency-glass",
    "https://www.americanglassexperts.us/blog/foggy-window-repair-los-angeles",
    "https://www.americanglassexperts.us/blog/frameless-shower-door-cost-los-angeles",
    "https://www.americanglassexperts.us/blog/storefront-glass-replacement-los-angeles",
    "https://www.americanglassexperts.us/blog/emergency-glass-repair-los-angeles"
  ]
}
JSON

echo ""
echo "IndexNow ping sent. HTTP 200 = accepted, 202 = queued."
