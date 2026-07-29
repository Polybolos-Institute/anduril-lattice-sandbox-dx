# Sandbox lifecycle

Lattice Sandboxes environments are short-lived. Plan for churn.

## Limits (Developer Program / docs)

- Concurrent environments: limited (often **2**)
- Max lifetime: on the order of **~12 hours**
- Idle lifetime: on the order of **~2 hours** without UI activity or API traffic
- OAuth `access_token`: typically **~30 minutes** (`expires_in`); refresh via `/oauth/token`

Exact numbers can change - check current Anduril Sandboxes docs.

## Operator habits

1. **Create env → copy Resource Endpoint + Client ID + Client Secret immediately.**
2. Keep Sandboxes Bearer in a local gitignored file (stable across envs).
3. When TCP works but TLS resets, the env is usually **gone** - create a new one; do not only rotate the Bearer.
4. Keep the env warm during demos: periodic `auth_check.py` or a light entity PUT.
5. After idle expiry, update endpoint + client id/secret; Bearer usually stays.

## Endpoint shape

UI links may look like:

`https://aivideo-….lattice-XXXX.env.sandboxes.developer.anduril.com/`

API host for doors:

`lattice-XXXX.env.sandboxes.developer.anduril.com:443`

Strip service prefixes; keep the `lattice-XXXX.env.sandboxes…` host.
