# Getting started with Multilogin X

This guide walks through the first steps after signing up for Multilogin — from installation to launching your first isolated browser profile.

**Sign up:** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## 1. Create an account

1. Visit [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
2. Choose a plan (the **$2 / 3-day trial** includes 5 profiles, proxy traffic, and cloud phone minutes)
3. Apply promo code **SAAS50** at checkout for 50% off eligible plans
4. Download the desktop app for your OS (Windows, macOS, or Linux)

System requirements: [multilogin.com/help — system requirements](https://multilogin.com/help)

## 2. Install and sign in

- Run the installer and log in with your workspace credentials
- Enable **2FA** (recommended) under account settings
- The Multilogin **agent** runs locally and communicates with cloud profiles

## 3. Create your first browser profile

1. Click **Create profile** in the dashboard
2. Choose storage: **local** (on your machine) or **cloud** (accessible from any device)
3. Select browser core: **Mimic** (Chromium-based) or **Stealthfox** (Firefox-based)
4. Configure fingerprint: use a preset template or customize OS, screen, timezone, WebGL, fonts
5. Attach a proxy (built-in residential proxy or your own SOCKS5/HTTP proxy)
6. Save and click **Start** — a new isolated browser window opens

Each profile is completely separate: no shared cookies, cache, or fingerprint data.

## 4. Try a cloud phone (mobile profile)

Cloud phones are real Android devices hosted in the cloud — not emulators.

1. Go to **Mobile profiles** in the dashboard
2. Create a profile and select Android version (9–15 available)
3. Launch the device — billing starts per minute ($0.011/min, credits roll over)
4. Use **MIN50** promo code when purchasing cloud phone plans for 50% off

See [cloud-phones-guide.md](cloud-phones-guide.md) for details.

## 5. Enable automation (Pro 10+)

Automation token access starts from **Pro 10**:

1. Go to **Settings → Automation**
2. Generate an automation token
3. Use the token with the REST API or Python scripts in `examples/python/`

See [api-quick-start.md](api-quick-start.md) and [automation-playwright-selenium.md](automation-playwright-selenium.md).

## Common workflows

| Use case | Recommended setup |
|----------|-------------------|
| Facebook / Google ads | Mimic + residential proxy matching target geo |
| TikTok / Instagram mobile | Cloud phone + matching region proxy |
| E-commerce (Amazon, eBay) | Separate profile per seller account |
| Web scraping | Headless Mimic + rotating proxies via API |
| Team operations | Business plan + workspace roles |

## Next steps

- [API quick start](api-quick-start.md) — programmatic profile management
- [Automation with Playwright/Selenium](automation-playwright-selenium.md)
- [Promo codes FAQ](promo-codes.md)
- [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)
