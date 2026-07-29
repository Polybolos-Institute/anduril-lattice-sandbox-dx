#!/usr/bin/env python3
"""OAuth-only smoke against Lattice Sandboxes or mock-lattice."""

from __future__ import annotations

import os
import sys

import requests
from dotenv import load_dotenv


def normalize_base(endpoint: str) -> tuple[str, str]:
    host = endpoint.strip()
    scheme = "https"
    if host.startswith("http://"):
        scheme = "http"
        host = host[len("http://") :]
    elif host.startswith("https://"):
        host = host[len("https://") :]
    host = host.rstrip("/")
    bare = host.split(":")[0].lower()
    if scheme == "https" and bare in ("127.0.0.1", "localhost", "::1"):
        scheme = "http"
    return host, f"{scheme}://{host}"


def main() -> int:
    load_dotenv()
    endpoint = os.environ.get("LATTICE_ENDPOINT", "").strip()
    client_id = os.environ.get("LATTICE_CLIENT_ID", "").strip()
    client_secret = os.environ.get("LATTICE_CLIENT_SECRET", "").strip()
    env_token = os.environ.get("LATTICE_ENV_TOKEN", "").strip()

    missing = [
        name
        for name, val in (
            ("LATTICE_ENDPOINT", endpoint),
            ("LATTICE_CLIENT_ID", client_id),
            ("LATTICE_CLIENT_SECRET", client_secret),
            ("LATTICE_ENV_TOKEN", env_token),
        )
        if not val
    ]
    if missing:
        print(f"[auth_check] missing: {' '.join(missing)}", file=sys.stderr)
        return 1

    host, base = normalize_base(endpoint)
    url = f"{base}/api/v1/oauth/token"
    headers = {
        "Anduril-Sandbox-Authorization": f"Bearer {env_token}",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    print(f"[auth_check] POST {url}")
    try:
        r = requests.post(url, headers=headers, data=data, timeout=30)
    except requests.RequestException as e:
        print(f"[auth_check] FAIL connection: {e}", file=sys.stderr)
        print(
            "[auth_check] hint: see docs/WINDOWS_TLS.md or use mock-lattice",
            file=sys.stderr,
        )
        return 1

    if r.status_code != 200:
        print(f"[auth_check] FAIL HTTP {r.status_code} body={r.text[:240]}", file=sys.stderr)
        print("[auth_check] hint: see docs/AUTH_CHECKLIST.md", file=sys.stderr)
        return 1

    body = r.json()
    token = body.get("access_token", "")
    expires = body.get("expires_in")
    if not token:
        print("[auth_check] FAIL: no access_token", file=sys.stderr)
        return 1

    print(
        f"[auth_check] OK endpoint={host} expires_in={expires} "
        f"token_prefix={token[:12]}…"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
