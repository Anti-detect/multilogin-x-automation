# Multilogin X — Antidetect Browser Automation, API & Cloud Phone Guide

[![GitHub](https://img.shields.io/github/stars/Anti-detect/multilogin-x-automation?style=social)](https://github.com/Anti-detect/multilogin-x-automation)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **Unofficial community developer resource** for [Multilogin](https://multilogin.com) antidetect browser automation, browser fingerprint management, residential proxy workflows, and cloud phone integration. Not affiliated with Multilogin official support.

**Repository:** [github.com/Anti-detect/multilogin-x-automation](https://github.com/Anti-detect/multilogin-x-automation)

Multilogin is an **antidetect browser** platform for multi-accounting, affiliate marketing, e-commerce, social media management, and ad operations. This repository provides practical guides and starter scripts for **Multilogin X** — isolated browser profiles, fingerprint spoofing, Puppeteer/Selenium/Playwright automation, REST API integration, and **cloud phones** (real Android devices in the cloud).

**Get started:** [Multilogin pricing & plans](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Languages / 语言 / Языки

| Language | README |
|----------|--------|
| English | You are here |
| 中文 (简体) | [README.zh-CN.md](README.zh-CN.md) |
| Русский | [README.ru.md](README.ru.md) |
| Tiếng Việt | [README.vi.md](README.vi.md) |
| Bahasa Indonesia | [README.id.md](README.id.md) |
| Português (Brasil) | [README.pt-BR.md](README.pt-BR.md) |

---

## Quick links

| Resource | Description |
|----------|-------------|
| [Getting started](docs/getting-started.md) | Install Multilogin X, create your first browser profile |
| [Cloud phones guide](docs/cloud-phones-guide.md) | Android cloud phone setup, billing, mobile multi-accounting |
| [API quick start](docs/api-quick-start.md) | Authentication, tokens, profile CRUD via REST API |
| [Automation](docs/automation-playwright-selenium.md) | Puppeteer, Selenium, Playwright with Multilogin |
| [Promo codes](docs/promo-codes.md) | Current discount codes and how to apply them |
| [Multilogin vs GoLogin](docs/multilogin-vs-gologin.md) | Antidetect browser comparison for teams |
| [Multilogin vs AdsPower](docs/multilogin-vs-adspower.md) | Feature comparison for scale operations |

---

## What is an antidetect browser?

An **antidetect browser** (also called anti-detect browser or fingerprint browser) creates isolated browser environments where each profile appears as a unique physical device. Unlike standard browsers or simple proxy extensions, antidetect platforms manage:

- **Browser fingerprint** — canvas, WebGL, fonts, timezone, hardware signals
- **Cookie & storage isolation** — no cross-profile data leakage
- **Proxy binding** — residential or datacenter IP per profile
- **Team collaboration** — shared workspaces with role-based access

Multilogin X is widely used for TikTok accounts, Facebook ads, Instagram automation, Amazon seller accounts, Google Ads, and affiliate marketing workflows where account isolation matters.

Official documentation: [multilogin.com/help](https://multilogin.com/help)

---

## Why Multilogin for multi-accounting?

Multilogin creates **fully isolated browser environments** — each profile behaves like a separate physical device with its own cookies, cache, and fingerprint. Key capabilities:

- **Mimic & Stealthfox** — real Chrome and Firefox browser cores, not Chromium wrappers
- **Browser fingerprint spoofing** — canvas, WebGL, fonts, timezone, and hardware signals based on real-user data
- **Built-in residential proxies** — region-specific IPs without third-party setup
- **Cloud phones** — genuine Android hardware identifiers (not emulators) for TikTok, Instagram, Facebook mobile workflows
- **Team workspaces** — role-based access, profile sharing, and transfer
- **Automation API** — headless mode, Postman collections, Python scripts, Playwright/Selenium/Puppeteer

[View plans & pricing →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Pricing overview (2026)

| Plan | Profiles | Proxy bonus | Cloud phone minutes | API |
|------|----------|-------------|---------------------|-----|
| Trial ($2 / 3 days) | 5 | 200 MB (one-time) | 60 min (one-time) | Yes |
| Pro 10 | 10 | 1 GB/month | 60 min/month | 50 RPM |
| Pro 50 | 50 | 3 GB/month | 75 min/month | 100 RPM |
| Pro 100 | 100 | 5 GB/month | 150 min/month | 100 RPM |
| Business 300+ | 300–10,000 | 10 GB/month | 450+ min/month | 100 RPM |

Annual billing saves ~35%. Full pricing: [multilogin.com/pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Promo codes

| Code | Applies to |
|------|------------|
| **SAAS50** | New subscriptions — 50% off |
| **MIN50** | Cloud phone plans — 50% off |

Enter the code at checkout on the [pricing page](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549). Details: [docs/promo-codes.md](docs/promo-codes.md)

---

## Python examples

Starter scripts for common automation tasks (requires Pro 10+ for automation token):

```bash
cd examples/python
pip install -r requirements.txt
export MLX_EMAIL="your@email.com"
export MLX_PASSWORD="your_password"
python get_automation_token.py
python start_profile.py --profile-id YOUR_PROFILE_ID
```

See [examples/python/README.md](examples/python/README.md) for full usage.

---

## Repository structure

```
docs/
  getting-started.md              # Multilogin X onboarding
  cloud-phones-guide.md           # Cloud phone vs emulator, Android versions
  api-quick-start.md              # REST API endpoints and auth flow
  automation-playwright-selenium.md
  promo-codes.md                  # Discount codes FAQ
  multilogin-vs-gologin.md        # Antidetect browser comparison
  multilogin-vs-adspower.md       # Antidetect browser comparison
examples/
  python/                         # Starter automation scripts
DISCLAIMER.md                     # Affiliate & community disclosure
README.zh-CN.md                   # Chinese README
README.ru.md                      # Russian README
README.vi.md                      # Vietnamese README
README.id.md                      # Indonesian README
README.pt-BR.md                   # Brazilian Portuguese README
```

---

## GitHub topics (suggested)

`multilogin` · `multilogin-x` · `antidetect-browser` · `anti-detect-browser` · `browser-fingerprint` · `fingerprint-browser` · `cloud-phone` · `multi-accounting` · `affiliate-marketing` · `browser-automation` · `puppeteer` · `selenium` · `playwright` · `residential-proxy` · `tiktok-accounts` · `facebook-accounts` · `instagram-automation` · `gologin-alternative` · `adspower-alternative` · `dolphin-anty-alternative`

---

## Related resources

- [Multilogin official help center](https://multilogin.com/help)
- [Multilogin API documentation](https://multilogin.com/help/en_US/api)
- [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Disclaimer

This is an **unofficial community repository** maintained by independent developers for educational purposes. Multilogin® is a trademark of its respective owner. Some links are affiliate links — see [DISCLAIMER.md](DISCLAIMER.md). For official support, contact Multilogin through their in-app chat or [help center](https://multilogin.com/help).

Contributions welcome via pull request.
