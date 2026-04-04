# American Glass Experts Inc. — Website

Static HTML/CSS website for American Glass Experts Inc., a glass repair and installation company based in Reseda, CA.

**Live site:** https://www.americanglassexperts.us

## Pages

| File | Description |
|---|---|
| `index.html` | Homepage — services, why us, service areas |
| `contact.html` | Contact form (Web3Forms) + business hours |
| `reseda.html` | Reseda, CA location SEO page |

## Before Launch Checklist

- [x] Phone number: (805) 750-6471
- [ ] Web3Forms key — open `contact.html`, find `YOUR_WEB3FORMS_ACCESS_KEY`, replace with key from https://web3forms.com (free)
- [ ] Photos — replace `img-placeholder` divs with real `<img>` tags

## Deployment (Cloudflare Pages — Free)

1. Push this repo to GitHub (already done).
2. Go to https://pages.cloudflare.com → New project → Connect GitHub → select `american-glass-experts`.
3. Leave build settings blank (no build command needed — pure HTML).
4. Click Deploy. You get a free `*.pages.dev` URL immediately.
5. Add custom domain `americanglassexperts.us` after transferring it from Wix.

## Domain Transfer: Wix → Cloudflare Registrar

1. Wix Dashboard → Domains → find `americanglassexperts.us` → unlock it → request EPP/transfer auth code.
2. Cloudflare Dashboard → Registrar → Transfer a Domain → paste the EPP code.
3. Approve the confirmation email Wix sends you.
4. Transfer takes 5–7 days. After it completes, DNS is already at Cloudflare — point it to Pages.

## Design Tokens

| Token | Value |
|---|---|
| Accent (mint) | `#7ec8c8` |
| Background (navy) | `#1a2e44` |
| Dark navy | `#111e2e` |
| Heading font | Cormorant Garamond |
| Body font | Jost |
