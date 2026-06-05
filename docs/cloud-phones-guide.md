# Multilogin cloud phones guide

Multilogin **cloud phones** are fully functional Android devices running on real smartphone hardware in the cloud. They are designed for safe multi-accounting on mobile-first platforms.

**Get started:** [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Cloud phone vs Android emulator

| | Cloud phone (Multilogin) | Android emulator |
|--|--------------------------|------------------|
| Hardware IDs | Genuine device identifiers | Simulated / detectable |
| Detection risk | Low — appears as physical device | High — easily flagged |
| Data persistence | Login states and apps persist | Often resets |
| Use case | TikTok, Instagram, mobile apps | Development/testing only |

Multilogin is **not an Android emulator**. Each cloud phone maintains persistent data, app environments, and unique device fingerprints.

## Supported Android versions

Android 9, 10, 11, 12, 13, 14, and 15 — choose based on your target app requirements.

## Billing

- **Pay per minute**: $0.011/min when the device is running
- Timer starts on launch, stops when you press **Stop** in the dashboard
- Minutes are purchased as credits; unused minutes roll over
- Bulk minute packages offer up to 30% discount

Plan bonuses (monthly):

| Plan | Included minutes |
|------|------------------|
| Trial | 60 (one-time) |
| Pro 10 | 60 |
| Pro 50 | 75 |
| Pro 100 | 150 |
| Business 300+ | 450+ |

Purchase additional minutes in-app: **Billing → Buy mobile minutes**.

## Promo code for cloud phones

Use **MIN50** at checkout for **50% off cloud phone plans**.

Signup with discount: [Multilogin pricing](https://multilogin.com/pricing/?utm_source=saas&utm_medium=partner&a_aid=saas&a_bid=f5fad549)

## Setup workflow

1. Create a mobile profile from the dashboard
2. Select Android version and region
3. Connect Multilogin proxy or custom proxy matching your target geo
4. Launch the cloud phone and install apps from the built-in store
5. Log in to your accounts — each profile stays isolated

## Best practices

- Match proxy country to app store region
- Use one cloud phone profile per account cluster
- Stop devices when not in use to conserve minutes
- Enable 2FA on workspace accounts
- Use tags and folders to organize profiles at scale

## Related

- [Getting started](getting-started.md)
- [API quick start](api-quick-start.md) — bulk mobile profile creation via API
- [Promo codes](promo-codes.md)
