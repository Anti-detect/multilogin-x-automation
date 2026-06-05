#!/usr/bin/env python3
"""Start a Multilogin profile via the local agent."""

import argparse
import os
import sys

import requests

API_BASE = "https://api.multilogin.com"
AGENT_BASE = os.environ.get("MLX_AGENT_URL", "http://localhost:45000")


def get_token(email: str, password: str) -> str:
    resp = requests.post(
        f"{API_BASE}/user/signin",
        json={"email": email, "password": password},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()["data"]["token"]


def start_profile(token: str, profile_id: str) -> dict:
    resp = requests.get(
        f"{AGENT_BASE}/api/v1/profile/start",
        params={"profileId": profile_id},
        headers={"Authorization": f"Bearer {token}"},
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    parser = argparse.ArgumentParser(description="Start a Multilogin browser profile")
    parser.add_argument("--profile-id", required=True, help="Profile UUID")
    args = parser.parse_args()

    email = os.environ.get("MLX_EMAIL")
    password = os.environ.get("MLX_PASSWORD")
    if not email or not password:
        print("Set MLX_EMAIL and MLX_PASSWORD environment variables.", file=sys.stderr)
        sys.exit(1)

    token = get_token(email, password)
    result = start_profile(token, args.profile_id)

    print("Profile started.")
    print(result)

    port = result.get("data", {}).get("port") or result.get("port")
    if port:
        print(f"\nConnect Playwright/Selenium to: 127.0.0.1:{port}")


if __name__ == "__main__":
    main()
