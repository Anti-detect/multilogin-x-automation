# Multilogin X — Hướng dẫn trình duyệt antidetect, API & cloud phone

[![GitHub](https://img.shields.io/github/stars/Anti-detect/multilogin-x-automation?style=social)](https://github.com/Anti-detect/multilogin-x-automation)

> **Tài nguyên cộng đồng không chính thức** dành cho [Multilogin](https://multilogin.com) — trình duyệt antidetect, quản lý browser fingerprint, proxy residential và cloud phone. Không liên kết với hỗ trợ chính thức của Multilogin.

**Repo:** [github.com/Anti-detect/multilogin-x-automation](https://github.com/Anti-detect/multilogin-x-automation)

Multilogin là nền tảng **trình duyệt antidetect** (anti-detect browser) phục vụ nuôi nhiều tài khoản, affiliate marketing, thương mại điện tử, quản lý mạng xã hội và chạy quảng cáo. Repo này cung cấp hướng dẫn và script mẫu cho **Multilogin X**: profile trình duyệt cô lập, giả mạo fingerprint, tự động hóa Puppeteer/Selenium/Playwright, REST API và **cloud phone** (thiết bị Android thật trên cloud).

**Bắt đầu:** [Bảng giá Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

[English](README.md) · [中文](README.zh-CN.md) · [Русский](README.ru.md) · [Bahasa Indonesia](README.id.md) · [Português](README.pt-BR.md)

---

## Trình duyệt antidetect là gì?

**Trình duyệt antidetect** tạo môi trường trình duyệt cô lập — mỗi profile giống một thiết bị vật lý riêng. Multilogin X quản lý:

- **Browser fingerprint** — canvas, WebGL, font, timezone, thông số phần cứng
- **Cô lập cookie & storage** — không rò rỉ dữ liệu giữa các profile
- **Gắn proxy** — IP residential hoặc datacenter theo từng profile
- **Làm việc nhóm** — workspace và phân quyền

Ứng dụng phổ biến: nuôi TikTok, Facebook Ads, Instagram, Amazon, Google Ads, affiliate.

---

## Liên kết nhanh

| Tài liệu | Mô tả |
|----------|-------|
| [Bắt đầu](docs/getting-started.md) | Cài Multilogin X, tạo profile đầu tiên |
| [Cloud phone](docs/cloud-phones-guide.md) | Thiết lập Android cloud phone |
| [API](docs/api-quick-start.md) | REST API, token, quản lý profile |
| [Tự động hóa](docs/automation-playwright-selenium.md) | Puppeteer, Selenium, Playwright |
| [Mã giảm giá](docs/promo-codes.md) | Mã khuyến mãi hiện tại |
| [Multilogin vs GoLogin](docs/multilogin-vs-gologin.md) | So sánh antidetect browser |
| [Multilogin vs AdsPower](docs/multilogin-vs-adspower.md) | So sánh antidetect browser |

---

## Mã giảm giá

| Mã | Áp dụng |
|----|---------|
| **SAAS50** | Đăng ký mới — giảm 50% |
| **MIN50** | Gói cloud phone — giảm 50% |

Nhập mã tại [trang bảng giá](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

---

## Tính năng Multilogin

- **Mimic & Stealthfox** — lõi Chrome và Firefox thật
- **Giả mạo fingerprint** — canvas, WebGL, font, timezone
- **Proxy residential tích hợp**
- **Cloud phone** — ID Android thật, không phải emulator
- **API tự động hóa** — headless, Python, Playwright/Selenium/Puppeteer

[Xem gói & giá →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Ví dụ Python

```bash
cd examples/python
pip install -r requirements.txt
export MLX_EMAIL="your@email.com"
export MLX_PASSWORD="your_password"
python get_automation_token.py
python start_profile.py --profile-id YOUR_PROFILE_ID
```

Chi tiết: [examples/python/README.md](examples/python/README.md).

---

## Tuyên bố miễn trừ

Repo cộng đồng không chính thức, chỉ phục vụ mục đích học tập. Multilogin® là nhãn hiệu của chủ sở hữu tương ứng. Một số liên kết có tham số affiliate — xem [DISCLAIMER.md](DISCLAIMER.md). Hỗ trợ chính thức: [multilogin.com/help](https://multilogin.com/help).
