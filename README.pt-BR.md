# Multilogin X — Guia de navegador antidetect, API e cloud phone

[![GitHub](https://img.shields.io/github/stars/Anti-detect/multilogin-x-automation?style=social)](https://github.com/Anti-detect/multilogin-x-automation)

> **Recurso comunitário não oficial** para [Multilogin](https://multilogin.com) — navegador antidetect, gerenciamento de browser fingerprint, proxies residenciais e cloud phones. Não afiliado ao suporte oficial da Multilogin.

**Repositório:** [github.com/Anti-detect/multilogin-x-automation](https://github.com/Anti-detect/multilogin-x-automation)

Multilogin é uma plataforma de **navegador antidetect** para multi-contas, marketing de afiliados, e-commerce, gestão de redes sociais e operações de anúncios. Este repositório oferece guias práticos e scripts iniciais para **Multilogin X** — perfis de navegador isolados, spoofing de fingerprint, automação Puppeteer/Selenium/Playwright, REST API e **cloud phones** (dispositivos Android reais na nuvem).

**Começar:** [Preços e planos Multilogin](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

[English](README.md) · [中文](README.zh-CN.md) · [Русский](README.ru.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md)

---

## O que é um navegador antidetect?

Um **navegador antidetect** (anti-detect browser) cria ambientes de navegador isolados onde cada perfil parece um dispositivo físico único. O Multilogin X gerencia:

- **Browser fingerprint** — canvas, WebGL, fontes, fuso horário, sinais de hardware
- **Isolamento de cookies e storage** — sem vazamento entre perfis
- **Vinculação de proxy** — IP residencial ou datacenter por perfil
- **Colaboração em equipe** — workspaces com acesso baseado em funções

Usos comuns: contas TikTok, Facebook Ads, Instagram, Amazon, Google Ads, marketing de afiliados.

---

## Links rápidos

| Documento | Descrição |
|-----------|-----------|
| [Primeiros passos](docs/getting-started.md) | Instalar Multilogin X, criar primeiro perfil |
| [Cloud phones](docs/cloud-phones-guide.md) | Configuração de Android cloud phone |
| [API](docs/api-quick-start.md) | REST API, tokens, gestão de perfis |
| [Automação](docs/automation-playwright-selenium.md) | Puppeteer, Selenium, Playwright |
| [Códigos promo](docs/promo-codes.md) | Códigos de desconto atuais |
| [Multilogin vs GoLogin](docs/multilogin-vs-gologin.md) | Comparação de navegadores antidetect |
| [Multilogin vs AdsPower](docs/multilogin-vs-adspower.md) | Comparação de navegadores antidetect |

---

## Códigos promocionais

| Código | Aplica-se a |
|--------|-------------|
| **SAAS50** | Novas assinaturas — 50% de desconto |
| **MIN50** | Planos cloud phone — 50% de desconto |

Insira o código na [página de preços](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549).

---

## Recursos do Multilogin

- **Mimic & Stealthfox** — núcleos reais Chrome e Firefox
- **Spoofing de fingerprint** — canvas, WebGL, fontes, timezone
- **Proxies residenciais integrados**
- **Cloud phones** — IDs Android reais, não emulador
- **API de automação** — headless, Python, Playwright/Selenium/Puppeteer

[Ver planos e preços →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Exemplos Python

```bash
cd examples/python
pip install -r requirements.txt
export MLX_EMAIL="your@email.com"
export MLX_PASSWORD="your_password"
python get_automation_token.py
python start_profile.py --profile-id YOUR_PROFILE_ID
```

Detalhes: [examples/python/README.md](examples/python/README.md).

---

## Aviso legal

Repositório comunitário não oficial para fins educacionais. Multilogin® é marca registrada de seus respectivos proprietários. Alguns links contêm parâmetros de afiliado — veja [DISCLAIMER.md](DISCLAIMER.md). Suporte oficial: [multilogin.com/help](https://multilogin.com/help).
