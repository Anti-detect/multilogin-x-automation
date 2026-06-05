# Multilogin X — 反检测浏览器自动化、API 与云手机指南

[![GitHub](https://img.shields.io/github/stars/Anti-detect/multilogin-x-automation?style=social)](https://github.com/Anti-detect/multilogin-x-automation)

> **非官方社区开发者资源**，面向 [Multilogin](https://multilogin.com) 反检测浏览器（antidetect browser）自动化、浏览器指纹管理、住宅代理与云手机工作流。与 Multilogin 官方支持无关。

**仓库地址：** [github.com/Anti-detect/multilogin-x-automation](https://github.com/Anti-detect/multilogin-x-automation)

Multilogin 是一款专业的**反检测浏览器**平台，适用于多账号运营、联盟营销、跨境电商、社交媒体管理与广告投放。本仓库提供 **Multilogin X** 实用教程与示例脚本：独立浏览器配置文件、指纹伪装、Puppeteer/Selenium/Playwright 自动化、REST API 集成，以及**云手机**（云端真实 Android 设备）。

**立即开始：** [Multilogin 价格与套餐](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

[English README](README.md) · [Русский](README.ru.md) · [Tiếng Việt](README.vi.md) · [Bahasa Indonesia](README.id.md) · [Português](README.pt-BR.md)

---

## 什么是反检测浏览器？

**反检测浏览器**（antidetect browser / 指纹浏览器）为每个配置文件创建完全隔离的浏览器环境，使每个账号看起来像独立的真实设备。Multilogin X 管理：

- **浏览器指纹** — Canvas、WebGL、字体、时区、硬件参数
- **Cookie 与存储隔离** — 配置文件之间无数据泄露
- **代理绑定** — 每个配置文件独立住宅或数据中心 IP
- **团队协作** — 工作区与角色权限管理

常见用途：TikTok 多账号、Facebook 广告、Instagram 自动化、Amazon 卖家账号、Google Ads、联盟营销。

---

## 快速导航

| 文档 | 说明 |
|------|------|
| [入门指南](docs/getting-started.md) | 安装 Multilogin X，创建第一个浏览器配置文件 |
| [云手机指南](docs/cloud-phones-guide.md) | Android 云手机设置与计费 |
| [API 快速入门](docs/api-quick-start.md) | REST API 认证与配置文件管理 |
| [自动化教程](docs/automation-playwright-selenium.md) | Puppeteer、Selenium、Playwright |
| [优惠码说明](docs/promo-codes.md) | 折扣码与使用方法 |
| [Multilogin vs GoLogin](docs/multilogin-vs-gologin.md) | 反检测浏览器对比 |
| [Multilogin vs AdsPower](docs/multilogin-vs-adspower.md) | 反检测浏览器对比 |

---

## 优惠码

| 代码 | 适用范围 |
|------|----------|
| **SAAS50** | 新订阅 — 5 折 |
| **MIN50** | 云手机套餐 — 5 折 |

在 [价格页面](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) 结账时输入优惠码。

---

## Multilogin 核心功能

- **Mimic & Stealthfox** — 真实 Chrome 与 Firefox 内核
- **指纹伪装** — 基于真实用户数据的 Canvas、WebGL、字体、时区
- **内置住宅代理** — 无需额外配置第三方代理
- **云手机** — 真实 Android 硬件标识，非模拟器
- **自动化 API** — 无头模式、Python 脚本、Playwright/Selenium/Puppeteer

[查看套餐与价格 →](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

---

## Python 示例

```bash
cd examples/python
pip install -r requirements.txt
export MLX_EMAIL="your@email.com"
export MLX_PASSWORD="your_password"
python get_automation_token.py
python start_profile.py --profile-id YOUR_PROFILE_ID
```

详见 [examples/python/README.md](examples/python/README.md)。

---

## 免责声明

本仓库由独立开发者维护，仅供学习参考。Multilogin® 为其各自所有者的商标。部分链接含联盟追踪参数 — 详见 [DISCLAIMER.md](DISCLAIMER.md)。官方支持请访问 [multilogin.com/help](https://multilogin.com/help)。
