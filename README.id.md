# Multilogin X — Panduan browser antidetect, API & cloud phone

[![GitHub](https://img.shields.io/github/stars/Anti-detect/multilogin-x-automation?style=social)](https://github.com/Anti-detect/multilogin-x-automation)

> **Sumber daya komunitas tidak resmi** untuk [Multilogin](https://multilogin.com) — browser antidetect, manajemen browser fingerprint, proxy residential, dan cloud phone. Tidak afiliasi dengan dukungan resmi Multilogin.

**Repositori:** [github.com/Anti-detect/multilogin-x-automation](https://github.com/Anti-detect/multilogin-x-automation)

Multilogin adalah platform **browser antidetect** untuk multi-akun, affiliate marketing, e-commerce, manajemen media sosial, dan operasi iklan. Repositori ini berisi panduan praktis dan skrip starter untuk **Multilogin X** — profil browser terisolasi, spoofing fingerprint, otomasi Puppeteer/Selenium/Playwright, REST API, dan **cloud phone** (perangkat Android asli di cloud).

**Mulai:** [Harga & paket Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

[English](README.md) · [中文](README.zh-CN.md) · [Русский](README.ru.md) · [Tiếng Việt](README.vi.md) · [Português](README.pt-BR.md)

---

## Apa itu browser antidetect?

**Browser antidetect** (anti-detect browser) membuat lingkungan browser terisolasi di mana setiap profil terlihat seperti perangkat fisik unik. Multilogin X mengelola:

- **Browser fingerprint** — canvas, WebGL, font, timezone, sinyal hardware
- **Isolasi cookie & storage** — tanpa kebocoran antar profil
- **Binding proxy** — IP residential atau datacenter per profil
- **Kolaborasi tim** — workspace dengan akses berbasis peran

Penggunaan umum: akun TikTok, Facebook Ads, Instagram, Amazon, Google Ads, affiliate marketing.

---

## Tautan cepat

| Dokumen | Deskripsi |
|---------|-----------|
| [Memulai](docs/getting-started.md) | Instal Multilogin X, buat profil pertama |
| [Cloud phone](docs/cloud-phones-guide.md) | Setup Android cloud phone |
| [API](docs/api-quick-start.md) | REST API, token, manajemen profil |
| [Otomasi](docs/automation-playwright-selenium.md) | Puppeteer, Selenium, Playwright |
| [Kode promo](docs/promo-codes.md) | Kode diskon saat ini |
| [Multilogin vs GoLogin](docs/multilogin-vs-gologin.md) | Perbandingan browser antidetect |
| [Multilogin vs AdsPower](docs/multilogin-vs-adspower.md) | Perbandingan browser antidetect |

---

## Kode promo

| Kode | Berlaku untuk |
|------|---------------|
| **SAAS50** | Langganan baru — diskon 50% |
| **MIN50** | Paket cloud phone — diskon 50% |

Masukkan kode di [halaman harga](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

---

## Fitur Multilogin

- **Mimic & Stealthfox** — inti Chrome dan Firefox asli
- **Spoofing fingerprint** — canvas, WebGL, font, timezone
- **Proxy residential bawaan**
- **Cloud phone** — ID Android asli, bukan emulator
- **API otomasi** — headless, Python, Playwright/Selenium/Puppeteer

[Lihat paket & harga →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Contoh Python

```bash
cd examples/python
pip install -r requirements.txt
export MLX_EMAIL="your@email.com"
export MLX_PASSWORD="your_password"
python get_automation_token.py
python start_profile.py --profile-id YOUR_PROFILE_ID
```

Detail: [examples/python/README.md](examples/python/README.md).

---

## Disclaimer

Repositori komunitas tidak resmi untuk tujuan edukasi. Multilogin® adalah merek dagang pemiliknya masing-masing. Beberapa tautan berisi parameter affiliate — lihat [DISCLAIMER.md](DISCLAIMER.md). Dukungan resmi: [multilogin.com/help](https://multilogin.com/help).
