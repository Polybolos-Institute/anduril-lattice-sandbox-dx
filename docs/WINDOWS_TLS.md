# Windows TLS notes

## Live Sandboxes

- Prefer a **native TLS stack** that already works on your machine (e.g. WinHTTP in C++ doors).
- Python `requests` on some Windows setups hits **connection reset** to `*.sandboxes.developer.anduril.com` even when TCP:443 succeeds.
- If Python OAuth fails but C++ / curl / browser works, treat it as a **client TLS path** issue, not bad credentials - verify with `scripts/auth_check.py` and a second client.

## Offline / CI

Use [mock-lattice](https://github.com/Polybolos-Institute/mock-lattice) on loopback **HTTP**:

```text
LATTICE_ENDPOINT=127.0.0.1:8765
LATTICE_CLIENT_ID=test-client-id
LATTICE_CLIENT_SECRET=test-client-secret
LATTICE_ENV_TOKEN=test-sandbox-token
```

Polybolos doors treat `127.0.0.1` / `localhost` as **HTTP** so CI does not need TLS.

## Checklist

1. `Test-NetConnection lattice-….env.sandboxes.developer.anduril.com -Port 443`
2. `python scripts/auth_check.py`
3. If reset persists: new sandbox env, or develop against `mock-lattice` until the network path is healthy
