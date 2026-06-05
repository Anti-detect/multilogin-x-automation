# Multilogin X — Антидетект-браузер: автоматизация, API и облачные телефоны

[![GitHub](https://img.shields.io/github/stars/Anti-detect/multilogin-x-automation?style=social)](https://github.com/Anti-detect/multilogin-x-automation)

> **Неофициальный ресурс для разработчиков** по [Multilogin](https://multilogin.com) — антидетект-браузер, управление отпечатками браузера, резидентные прокси и облачные телефоны. Не связан с официальной поддержкой Multilogin.

**Репозиторий:** [github.com/Anti-detect/multilogin-x-automation](https://github.com/Anti-detect/multilogin-x-automation)

Multilogin — платформа **антидетект-браузера** для мультиаккаунтинга, партнёрского маркетинга, e-commerce, SMM и рекламных кампаний. В этом репозитории — руководства и скрипты для **Multilogin X**: изолированные профили, подмена отпечатков, автоматизация Puppeteer/Selenium/Playwright, REST API и **облачные телефоны** (реальные Android-устройства в облаке).

**Начать:** [Тарифы Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

[English](README.md) · [中文](README.zh-CN.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Português](README.pt-BR.md)

---

## Что такое антидетект-браузер?

**Антидетект-браузер** (antidetect browser) создаёт изолированные браузерные среды, где каждый профиль выглядит как отдельное физическое устройство. Multilogin X управляет:

- **Отпечатком браузера** — Canvas, WebGL, шрифты, часовой пояс, аппаратные параметры
- **Изоляцией cookie и хранилища** — без утечек между профилями
- **Привязкой прокси** — резидентный или датацентровый IP на профиль
- **Командной работой** — рабочие пространства и роли

Применение: TikTok, Facebook Ads, Instagram, Amazon, Google Ads, арбитраж трафика.

---

## Быстрые ссылки

| Документ | Описание |
|----------|----------|
| [Начало работы](docs/getting-started.md) | Установка Multilogin X, первый профиль |
| [Облачные телефоны](docs/cloud-phones-guide.md) | Настройка Android cloud phone |
| [API](docs/api-quick-start.md) | REST API, токены, CRUD профилей |
| [Автоматизация](docs/automation-playwright-selenium.md) | Puppeteer, Selenium, Playwright |
| [Промокоды](docs/promo-codes.md) | Скидочные коды |
| [Multilogin vs GoLogin](docs/multilogin-vs-gologin.md) | Сравнение антидетект-браузеров |
| [Multilogin vs AdsPower](docs/multilogin-vs-adspower.md) | Сравнение антидетект-браузеров |

---

## Промокоды

| Код | Применение |
|-----|------------|
| **SAAS50** | Новые подписки — скидка 50% |
| **MIN50** | Облачные телефоны — скидка 50% |

Введите код на [странице тарифов](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

---

## Возможности Multilogin

- **Mimic & Stealthfox** — настоящие ядра Chrome и Firefox
- **Подмена отпечатков** — Canvas, WebGL, шрифты, timezone
- **Встроенные резидентные прокси**
- **Облачные телефоны** — реальные Android ID, не эмулятор
- **API автоматизации** — headless, Python, Playwright/Selenium/Puppeteer

[Тарифы и цены →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Python-примеры

```bash
cd examples/python
pip install -r requirements.txt
export MLX_EMAIL="your@email.com"
export MLX_PASSWORD="your_password"
python get_automation_token.py
python start_profile.py --profile-id YOUR_PROFILE_ID
```

Подробнее: [examples/python/README.md](examples/python/README.md).

---

## Отказ от ответственности

Неофициальный репозиторий для образовательных целей. Multilogin® — товарный знак правообладателя. Некоторые ссылки содержат партнёрские параметры — см. [DISCLAIMER.md](DISCLAIMER.md). Официальная поддержка: [multilogin.com/help](https://multilogin.com/help).
