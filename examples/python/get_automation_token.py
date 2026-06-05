#!/usr/bin/env python3
"""Sign in to Multilogin X and print the session + automation tokens."""

import os
import sys

import requests

API_BASE = "https://api.multilogin.com"


def sign_in(email: str, password: str) -> dict:
    resp = requests.post(
        f"{API_BASE}/user/signin",
        json={"email": email, "password": password},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def get_automation_token(session_token: str) -> dict:
    resp = requests.get(
        f"{API_BASE}/user/automation_token",
        headers={"Authorization": f"Bearer {session_token}"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    email = os.environ.get("MLX_EMAIL")
    password = os.environ.get("MLX_PASSWORD")

    if not email or not password:
        print("Set MLX_EMAIL and MLX_PASSWORD environment variables.", file=sys.stderr)
        sys.exit(1)

    data = sign_in(email, password)
    session_token = data.get("data", {}).get("token")
    if not session_token:
        print("Sign-in succeeded but no token returned.", file=sys.stderr)
        sys.exit(1)

    print(f"Session token: {session_token[:20]}...")

    try:
        auto = get_automation_token(session_token)
        auto_token = auto.get("data", {}).get("token", auto.get("data"))
        print(f"Automation token: {auto_token}")
    except requests.HTTPError as exc:
        print(
            f"Automation token unavailable (Pro 10+ required): {exc.response.status_code}",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
