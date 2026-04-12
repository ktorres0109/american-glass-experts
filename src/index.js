export default {
  async fetch(request, env) {
    const response = await env.ASSETS.fetch(request);

    const newHeaders = new Headers(response.headers);

    // HSTS — force HTTPS for 1 year, include subdomains
    newHeaders.set('Strict-Transport-Security', 'max-age=31536000; includeSubDomains; preload');

    // Prevent clickjacking
    newHeaders.set('X-Frame-Options', 'DENY');

    // Stop MIME sniffing
    newHeaders.set('X-Content-Type-Options', 'nosniff');

    // Control referrer info sent to third parties
    newHeaders.set('Referrer-Policy', 'strict-origin-when-cross-origin');

    // Permissions policy — disable features we don't use
    newHeaders.set('Permissions-Policy', 'camera=(), microphone=(), geolocation=(), payment=()');

    // CSP — allow own origin + Google Fonts + Web3Forms + Cloudflare Insights
    newHeaders.set(
      'Content-Security-Policy',
      [
        "default-src 'self'",
        "script-src 'self' 'unsafe-inline' https://static.cloudflareinsights.com",
        "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com",
        "font-src 'self' https://fonts.gstatic.com",
        "img-src 'self' data: https:",
        "connect-src 'self' https://api.web3forms.com https://cloudflareinsights.com",
        "form-action 'self' https://api.web3forms.com",
        "frame-ancestors 'none'",
        "base-uri 'self'",
      ].join('; ')
    );

    return new Response(response.body, {
      status: response.status,
      statusText: response.statusText,
      headers: newHeaders,
    });
  },
};
