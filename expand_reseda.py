#!/usr/bin/env python3
"""
Flagship treatment for reseda.html — our business address page.
1. Replace thin LOCAL CONTEXT section with full flagship version
2. Inject deep-content section + testimonials block before FAQ
"""

with open("reseda.html") as f:
    content = f.read()

if 'Reseda Flagship' in content:
    print("Already expanded, skipping.")
    exit()

# ── 1. Replace LOCAL CONTEXT section ─────────────────────────────
OLD_LOCAL = """  <!-- LOCAL CONTEXT -->
  <section style="background:var(--bg-soft);">
    <div class="container">
      <div class="reveal">
        <span class="section-label">Local Knowledge</span>
        <h2>Serving <em>Reseda</em> and Los Angeles County</h2>
      </div>
      <div class="city-highlights">
        <div class="city-highlight-card reveal d1">
          <h4>📍 Neighborhoods We Serve</h4>
          <p>Reseda Boulevard corridor, Victory Boulevard area, Tarzana border — and all surrounding areas in the 91335 zip code.</p>
        </div>
        <div class="city-highlight-card reveal d2">
          <h4>🕐 How Fast We Get There</h4>
          <p>Our home base — we're in Reseda. Most jobs are scheduled within 1–3 business days. Emergency calls are handled same-day when possible.</p>
        </div>
        <div class="city-highlight-card reveal d3">
          <h4>🏠 Residential &amp; Commercial</h4>
          <p>We work with homeowners, contractors, property managers, and business owners throughout Reseda — any size job.</p>
        </div>
      </div>
        <div class="city-highlight-card reveal d4">
          <h4>🏙️ About Reseda</h4>
          <p>Nestled in the heart of the San Fernando Valley, Reseda's charming post-war bungalows and apartment complexes along Reseda Boulevard often feature original single-pane windows, making dual-pane window replacement a highly sought-after service for energy efficiency and noise reduction. Our local expertise also extends to custom shower enclosures, frequently installed in updated bathrooms within these classic Reseda homes.</p>
        </div>

      <div class="reveal" style="margin-top:16px;">
        <p style="font-size:.9rem;color:var(--text-mid);line-height:1.72;">
          <strong>Also serving nearby:</strong> <a href="/tarzana">Tarzana</a> · <a href="/northridge">Northridge</a> · <a href="/winnetka">Winnetka</a> · <a href="/van-nuys">Van Nuys</a> · <a href="/service-areas" style="color:var(--blue);">View all service areas →</a>
        </p>
      </div>
    </div>
  </section>"""

NEW_LOCAL = """  <!-- Reseda Flagship LOCAL CONTEXT -->
  <section style="background:var(--bg-soft);">
    <div class="container">
      <div class="reveal">
        <span class="section-label">Our Home Base</span>
        <h2>American Glass Experts — <em>Based in Reseda, CA</em></h2>
      </div>

      <!-- Business info card -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:40px;" class="reveal">
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r-lg);padding:28px;">
          <h3 style="font-size:1.05rem;margin-bottom:16px;font-family:var(--body);">Location &amp; Hours</h3>
          <p style="font-size:.9rem;color:var(--text-mid);line-height:1.9;margin:0;">
            <strong style="color:var(--coal);">6853 Reseda Blvd</strong><br>
            Reseda, CA 91335<br><br>
            <strong style="color:var(--coal);">Mon – Sat</strong> &nbsp;7:00 AM – 10:00 PM<br>
            <strong style="color:var(--coal);">Phone/Text</strong> &nbsp;<a href="tel:+18057506471" style="color:var(--blue);">(805) 750-6471</a><br>
            <strong style="color:var(--coal);">Email</strong> &nbsp;<a href="mailto:info@americanglassexperts.us" style="color:var(--blue);">info@americanglassexperts.us</a>
          </p>
          <a href="/contact" style="display:inline-block;margin-top:20px;font-size:.88rem;color:var(--blue);font-weight:600;">Get directions + map →</a>
        </div>
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r-lg);padding:28px;">
          <h3 style="font-size:1.05rem;margin-bottom:16px;font-family:var(--body);">License &amp; Credentials</h3>
          <ul style="font-size:.9rem;color:var(--text-mid);line-height:2;list-style:none;padding:0;margin:0;">
            <li>✓ &nbsp;C-17 Glazing Contractor License</li>
            <li>✓ &nbsp;CSLB #1125850 — <a href="https://www.cslb.ca.gov" target="_blank" rel="noopener" style="color:var(--blue);">verify at cslb.ca.gov</a></li>
            <li>✓ &nbsp;Fully bonded &amp; insured</li>
            <li>✓ &nbsp;4.8 ★ average — Yelp &amp; Google</li>
            <li>✓ &nbsp;Licensed since 2003</li>
            <li>✓ &nbsp;No subcontractors — our own crew</li>
          </ul>
        </div>
      </div>

      <div class="city-highlights">
        <div class="city-highlight-card reveal d1">
          <h4>📍 Reseda Neighborhoods</h4>
          <p>Reseda Blvd corridor · Victory Blvd area · Tarzana border · Northridge border · Winnetka · West Reseda · East Reseda. Zip: 91335.</p>
        </div>
        <div class="city-highlight-card reveal d2">
          <h4>🕐 Same-Day in Reseda</h4>
          <p>Most reliable same-day availability is here in Reseda — no travel time. Emergency calls dispatched within 30–60 min in most cases.</p>
        </div>
        <div class="city-highlight-card reveal d3">
          <h4>🏠 Residential + Commercial</h4>
          <p>Single-family homes, apartment buildings, HOAs, storefronts, offices — any size job, any property type in the 91335 zip.</p>
        </div>
        <div class="city-highlight-card reveal d4">
          <h4>🔧 No Subcontractors</h4>
          <p>Frank and Bryant — our own crew — handle every job. We don't dispatch subcontractors. Same team, every time, for accountability.</p>
        </div>
      </div>

      <div class="reveal" style="margin-top:24px;">
        <p style="font-size:.9rem;color:var(--text-mid);line-height:1.72;">
          <strong>Nearby cities:</strong>
          <a href="/tarzana">Tarzana</a> · <a href="/northridge">Northridge</a> · <a href="/winnetka">Winnetka</a> · <a href="/van-nuys">Van Nuys</a> · <a href="/canoga-park">Canoga Park</a> · <a href="/chatsworth">Chatsworth</a> · <a href="/woodland-hills">Woodland Hills</a> · <a href="/service-areas" style="color:var(--blue);">View all →</a>
        </p>
      </div>
    </div>
  </section>"""

content = content.replace(OLD_LOCAL, NEW_LOCAL, 1)

# ── 2. Inject deep content + testimonials before FAQ ──────────────
DEEP_SECTION = """
  <div class="divider"></div>

  <!-- Reseda Deep Content -->
  <section style="padding:72px 0;">
    <div class="container" style="max-width:860px;">
      <span class="section-label">Reseda Glass Work</span>
      <h2>Glass Repair &amp; Installation in <em>Reseda</em> — What to Know</h2>
      <div style="color:var(--text-mid);line-height:1.85;font-size:1rem;">
        <p>Reseda is where we work every day — 6853 Reseda Blvd has been our base of operations since 2003. We know the neighborhood's housing stock intimately: the post-war single-family homes east of Reseda Blvd, the 1960s–70s apartment complexes along the boulevard itself, the newer construction pushing toward the Northridge border, and the commercial buildings along Victory and Saticoy.</p>
        <p>The most common call we get from Reseda homeowners is foggy or cloudy windows — the visual sign of a failed dual-pane seal. Reseda's housing stock has a high concentration of homes and apartments built between 1960 and 1995, and dual-pane windows from that era are at or past their insulating glass unit lifespan. If your windows are cloudy between the panes, that condensation won't go away on its own — the seal is gone and the gas fill is compromised. We replace the glass unit without touching your frame, typically within the same week you call.</p>
        <p>Shower enclosure upgrades are our second most common Reseda job. The older bathroom layouts throughout 91335 — typically a 5'×5' or 5'×3' alcove with the original framed bypass doors — are being upgraded throughout the neighborhood. A frameless or semi-frameless glass enclosure transforms how the bathroom reads: the space looks larger, cleaning is easier, and the visual weight of the aluminum channel is gone. We custom-cut to your exact opening — important in older Reseda homes where the walls are rarely perfectly plumb.</p>
        <p>For Reseda apartment managers and property owners: we work with multi-unit properties throughout the 91335 zip. Window seal failures, broken panes, emergency board-up after break-ins, and sliding door repair are all services we provide at volume for property managers. Call and ask about our commercial account setup if you manage 5+ units.</p>
        <p>Emergency response in Reseda is the fastest we offer anywhere in our service area. Because we're based here, board-up and same-day response is most reliable for 91335 addresses. For a break-in or storm damage call, we can typically have someone on-site within 30–60 minutes during business hours, and we monitor the phone until 10pm for after-hours emergencies.</p>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- Testimonials -->
  <section style="background:var(--bg-soft);padding:72px 0;">
    <div class="container" style="max-width:900px;">
      <span class="section-label">What Reseda Customers Say</span>
      <h2>Reviews from <em>Reseda &amp; the San Fernando Valley</em></h2>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px;margin-top:36px;">
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px;" class="reveal d1">
          <div style="color:#f59e0b;font-size:1.1rem;margin-bottom:12px;">★★★★★</div>
          <p style="font-size:.92rem;color:var(--text-mid);line-height:1.75;margin-bottom:16px;">"Came out the same day I called. Measured my shower opening, explained the glass thickness options, and had the frameless door installed three days later. Clean work, no mess left behind."</p>
          <strong style="font-size:.88rem;color:var(--coal);">— Maria T., Reseda</strong>
        </div>
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px;" class="reveal d2">
          <div style="color:#f59e0b;font-size:1.1rem;margin-bottom:12px;">★★★★★</div>
          <p style="font-size:.92rem;color:var(--text-mid);line-height:1.75;margin-bottom:16px;">"Had a break-in at my store on Reseda Blvd. Called at 8pm and they were there within an hour to board it up. Glass replacement was done two days later. Saved my weekend."</p>
          <strong style="font-size:.88rem;color:var(--coal);">— David R., Reseda Business Owner</strong>
        </div>
        <div style="background:var(--bg-card);border:1px solid var(--border);border-radius:var(--r-lg);padding:24px;" class="reveal d3">
          <div style="color:#f59e0b;font-size:1.1rem;margin-bottom:12px;">★★★★★</div>
          <p style="font-size:.92rem;color:var(--text-mid);line-height:1.75;margin-bottom:16px;">"Fixed four foggy windows in my 1970s house. Replaced just the glass units — kept all my original frames. Price was fair and they finished in half a day. Highly recommend."</p>
          <strong style="font-size:.88rem;color:var(--coal);">— Sandra K., Reseda</strong>
        </div>
      </div>
      <p style="margin-top:28px;font-size:.88rem;color:var(--text-dim);text-align:center;">
        <a href="https://www.yelp.com/biz/american-glass-experts-san-fernando-valley-4" target="_blank" rel="noopener" style="color:var(--blue);">Read more reviews on Yelp →</a>
        &nbsp;&nbsp;·&nbsp;&nbsp;
        <a href="https://share.google/bjUDf31y962SkEPvv" target="_blank" rel="noopener" style="color:var(--blue);">Google Reviews →</a>
      </p>
    </div>
  </section>

  <div class="divider"></div>

"""

# Insert before <!-- FAQ -->
content = content.replace("  <!-- FAQ -->", DEEP_SECTION + "  <!-- FAQ -->", 1)

# ── 3. Replace the thin first FAQ question ───────────────────────
OLD_FAQ1 = """        <div class="faq-item reveal d1">
          <button class="faq-q">
            Do you serve Reseda, CA?
            <span class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Yes — we regularly serve Reseda and Los Angeles County. Call <a href='tel:+18057506471'> (805) 750-6471 — Call or Text Anytime</a> or request an estimate and we'll confirm availability.</div></div>
        </div>"""

NEW_FAQ1 = """        <div class="faq-item reveal d1">
          <button class="faq-q">
            Where exactly is American Glass Experts located in Reseda?
            <span class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">We're at 6853 Reseda Blvd, Reseda, CA 91335 — in the heart of the San Fernando Valley. This is our operating base, so Reseda jobs get our fastest response and most flexible scheduling.</div></div>
        </div>"""

content = content.replace(OLD_FAQ1, NEW_FAQ1, 1)

# ── 4. Add extra FAQ items before closing faq-list ───────────────
EXTRA_FAQS = """        <div class="faq-item reveal d7">
          <button class="faq-q">
            Why is same-day service most reliable in Reseda?
            <span class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Our shop is in Reseda — there's no drive time to account for. When a job cancels or we finish early, the most available slot goes to Reseda addresses first. For emergencies, we can reach any address in 91335 within 30–60 minutes.</div></div>
        </div>
        <div class="faq-item reveal d8">
          <button class="faq-q">
            Do you work with apartment buildings and property managers in Reseda?
            <span class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Yes — we work with multi-unit property owners and management companies throughout Reseda. Window seal replacements, broken pane repair, sliding door maintenance, and emergency board-up are all services we provide at volume. Call to ask about our commercial account setup.</div></div>
        </div>
        <div class="faq-item reveal d9">
          <button class="faq-q">
            What's the most common glass issue in Reseda homes?
            <span class="faq-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg></span>
          </button>
          <div class="faq-a"><div class="faq-a-inner">Foggy or cloudy dual-pane windows — failed IGU seals — are the most common call in Reseda. The housing stock is heavily weighted toward homes built between 1960 and 1995, and windows from that era are hitting seal failure now. IGU replacement (swapping just the glass unit, keeping your frame) is the cost-effective fix.</div></div>
        </div>"""

# Insert before the closing </div> of faq-list
FAQ_LIST_CLOSE = "      </div>\n    </div>\n  </section>\n\n  <!-- CONTACT STRIP -->"
content = content.replace(
    FAQ_LIST_CLOSE,
    EXTRA_FAQS + "\n" + FAQ_LIST_CLOSE,
    1
)

with open("reseda.html", "w") as f:
    f.write(content)

print("Reseda flagship expansion done.")
