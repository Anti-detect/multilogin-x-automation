# Multilogin API quick start

Multilogin X exposes a REST API for profile management, automation, and team workflows. Automation access requires **Pro 10** or higher.

Official reference: [multilogin.com/help/en_US/api](https://multilogin.com/help/en_US/api)

**Need a plan with API access?** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549) — use promo **SAAS50** for 50% off new subscriptions.

## Base URL

```
https://api.multilogin.com
```

Local agent (profile start/stop):

```
http://localhost:45000
```

Port may vary — check agent settings in the desktop app.

## Authentication flow

1. **Sign in** with email/password → receive session token
2. **Generate automation token** (Pro 10+) from dashboard or API
3. Pass token in `Authorization: Bearer <token>` header

Example scripts: [examples/python/](../examples/python/)

## Key endpoints

| Action | Method | Endpoint |
|--------|--------|----------|
| Sign in | POST | `/user/signin` |
| Get automation token | GET | `/user/automation_token` |
| List profiles | GET | `/profile` |
| Create profile | POST | `/profile/create` |
| Start profile | GET | `/profile/start?profileId={id}` |
| Stop profile | GET | `/profile/stop?profileId={id}` |
| Update profile | POST | `/profile/update` |
| Export cookies | GET | `/profile/export_cookies?profileId={id}` |

Rate limits depend on plan (50–100 requests per minute on Pro/Business tiers).

## Python example

```python
import os
import requests

API = "https://api.multilogin.com"

def sign_in(email: str, password: str) -> str:
    resp = requests.post(f"{API}/user/signin", json={
        "email": email,
        "password": password,
    })
    resp.raise_for_status()
    return resp.json()["data"]["token"]

token = sign_in(os.environ["MLX_EMAIL"], os.environ["MLX_PASSWORD"])
headers = {"Authorization": f"Bearer {token}"}

profiles = requests.get(f"{API}/profile", headers=headers)
print(profiles.json())
```

Full working scripts with error handling are in [examples/python/](../examples/python/).

## Automation methods

| Method | Best for |
|--------|----------|
| REST API + Python | Custom pipelines, bulk operations |
| Postman collection | Low-code testing, team onboarding |
| CLI | Quick profile start/stop from terminal |
| Puppeteer / Selenium / Playwright | Browser-level scripting via debugger port |
| Headless mode | Server-side automation without GUI |

See [automation-playwright-selenium.md](automation-playwright-selenium.md).

## Security notes

- Store tokens in environment variables, never in git
- Rotate automation tokens periodically
- Use workspace roles to limit team API access
- Enable 2FA on all workspace accounts

## Resources

- [Multilogin API beginner's guide](https://multilogin.com/help/en_US/multilogin-api-automation-beginners-guide)
- [Postman automation setup](https://multilogin.com/help/en_US/how-to-set-up-multilogin-automation-with-postman)
- [Python login example (official)](https://multilogin.com/help/en_US/how-to-log-in-to-multilogin-with-python)
