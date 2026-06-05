# Browser automation with Multilogin

Multilogin X supports industry-standard automation frameworks. Each profile exposes a **debugger port** when started, allowing Puppeteer, Selenium, and Playwright to connect to an already-fingerprinted browser session.

## How it works

1. Start a profile via API or desktop app
2. API response includes `port` (debugger address)
3. Connect your automation framework to `127.0.0.1:{port}`
4. Script runs inside the isolated, fingerprinted browser
5. Stop profile when done

This approach keeps fingerprint management in Multilogin while you control page-level actions in code.

## Playwright (Python)

```python
from playwright.sync_api import sync_playwright

DEBUGGER_PORT = 9222  # from profile start response

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(f"http://127.0.0.1:{DEBUGGER_PORT}")
    context = browser.contexts[0]
    page = context.pages[0] if context.pages else context.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

## Selenium (Python)

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

## Puppeteer (Node.js)

```javascript
const puppeteer = require("puppeteer-core");

const browser = await puppeteer.connect({
  browserURL: "http://127.0.0.1:9222",
});
const pages = await browser.pages();
const page = pages[0] || await browser.newPage();
await page.goto("https://example.com");
console.log(await page.title());
await browser.disconnect();
```

## Headless mode

For server deployments (Linux VPS, CI pipelines):

1. Configure agent for headless mode in Multilogin settings
2. Enable auto-launch on system startup
3. Use API to start profiles without GUI

Guide: [How to use headless mode](https://multilogin.com/help/en_US/how-to-use-headless-mode)

## CLI automation

Multilogin provides a CLI for basic operations:

```bash
# Start profile (paths vary by OS — check agent install directory)
mlx profile start --profile-id <UUID>
mlx profile stop --profile-id <UUID>
```

See [Basic automation with CLI](https://multilogin.com/help/en_US/basic-automation-with-cli).

## Recommended workflow for scale

1. Create profile templates via API (fingerprint + proxy presets)
2. Bulk-create profiles from templates
3. Queue start/stop jobs with a task runner
4. Connect Playwright/Selenium per job
5. Export cookies via API for session persistence

Starter scripts: [examples/python/start_profile.py](../examples/python/start_profile.py)

**Multilogin plans with automation API:** [pricing page](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — promo **SAAS50** for new subscriptions.

## External tools

Multilogin integrates with CAPTCHA solvers, SMS verification pools, and other automation helpers. See [external automation tools](https://multilogin.com/help/en_US/external-automation-tools) in the official docs.
