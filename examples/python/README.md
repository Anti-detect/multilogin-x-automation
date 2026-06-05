# Multilogin X Python examples

Starter scripts for Multilogin REST API automation.

## Prerequisites

- Multilogin X desktop app installed and agent running
- **Pro 10+** plan for automation token (optional for basic sign-in)
- Python 3.9+

## Setup

```bash
pip install -r requirements.txt

# Windows PowerShell
$env:MLX_EMAIL = "your@email.com"
$env:MLX_PASSWORD = "your_password"

# Linux / macOS
export MLX_EMAIL="your@email.com"
export MLX_PASSWORD="your_password"
```

## Scripts

### get_automation_token.py

Sign in and retrieve session + automation tokens.

```bash
python get_automation_token.py
```

### start_profile.py

Start a profile through the local agent. Returns debugger port for Playwright/Selenium.

```bash
python start_profile.py --profile-id YOUR-PROFILE-UUID
```

Find profile IDs in the Multilogin dashboard or via `GET /profile` API.

## Agent URL

Default local agent: `http://localhost:45000`

Override if your agent uses a different port:

```bash
export MLX_AGENT_URL="http://localhost:35000"
```

## Security

Never commit credentials. Use environment variables or a local `.env` file (gitignored).

## Links

- [API quick start](../../docs/api-quick-start.md)
- [Automation guide](../../docs/automation-playwright-selenium.md)
- [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — promo: **SAAS50** / **MIN50**
