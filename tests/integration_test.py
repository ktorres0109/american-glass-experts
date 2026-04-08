import os
import re
from playwright.sync_api import sync_playwright, expect

def test_city_search_filtering():
    """
    E2E test for the city search filtering functionality on service-areas.html.
    Verifies that:
    1. All cities and regions are initially visible.
    2. Typing a city name filters out non-matching cities and regions.
    3. Typing a non-existent city shows the 'no results' message.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Intercept external network requests (fonts, analytics, etc.) to prevent timeouts
        # but allow local file loading.
        page.route(re.compile(r"https?://.*"), lambda route: route.abort())

        # Load the local HTML file
        file_path = os.path.abspath("service-areas.html")
        page.goto(f"file://{file_path}")

        # Define locators
        search_input = page.locator('#citySearch')
        reseda_card = page.locator('.city-card[data-city="Reseda"]')
        van_nuys_card = page.locator('.city-card[data-city="Van Nuys"]')
        ventura_region = page.locator('.region', has_text="Ventura County")
        no_results = page.locator('#no-results')

        # 1. Initial State Verification
        expect(reseda_card).to_be_visible()
        expect(van_nuys_card).to_be_visible()
        expect(ventura_region).to_be_visible()
        expect(no_results).to_be_hidden()

        # 2. Filter by "Reseda"
        print("Testing filter: 'Reseda'...")
        search_input.fill('Reseda')

        # expect() automatically waits for the condition to be met
        expect(reseda_card).to_be_visible()
        expect(van_nuys_card).to_be_hidden()
        expect(ventura_region).to_be_hidden()

        # 3. Filter with no matches
        print("Testing filter: 'NonExistentCity'...")
        search_input.fill('NonExistentCity')

        expect(reseda_card).to_be_hidden()
        expect(van_nuys_card).to_be_hidden()
        expect(no_results).to_be_visible()

        # 4. Clear filter
        print("Testing clear filter...")
        search_input.fill('')
        expect(reseda_card).to_be_visible()
        expect(van_nuys_card).to_be_visible()
        expect(ventura_region).to_be_visible()
        expect(no_results).to_be_hidden()

        browser.close()
        print("Integration test PASSED")

if __name__ == "__main__":
    try:
        test_city_search_filtering()
    except Exception as e:
        print(f"Test FAILED: {e}")
        exit(1)
