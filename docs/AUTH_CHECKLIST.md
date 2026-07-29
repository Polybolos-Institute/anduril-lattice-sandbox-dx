# Auth checklist (Lattice Sandboxes)

Use this before debugging “Lattice is broken.” Most failures are **wrong token in the wrong header**.

## Four different credentials

| Name | Where you get it | Used for | Header / field |
|------|------------------|----------|----------------|
| **Sandboxes Bearer** | Sandboxes portal → **Account & Security** → Bearer tokens | All API calls to any of *your* envs | `Anduril-Sandbox-Authorization: Bearer …` |
| **Client ID** | Environment details (per env) | OAuth client-credentials | form `client_id` |
| **Client Secret** | Environment details (per env) | OAuth client-credentials | form `client_secret` |
| **OAuth access token** | `POST /api/v1/oauth/token` response | Entity PUT / stream after login | `Authorization: Bearer …` |

Also on the env page (easy to confuse):

| Name | Used for | API? |
|------|----------|------|
| **Lattice User** (`user@internal.local`) | Lattice **UI** login only | **No** |
| **Lattice Password** | Lattice **UI** login only | **No** |
| **Lattice Environment / Auth Token** (JWT, often `x_ut: service`) | Some SDK samples call this “environment token” | **Do not** put this in `Anduril-Sandbox-Authorization` if you use client-credentials OAuth (causes **401**) |

## Correct OAuth flow

```http
POST https://{LATTICE_ENDPOINT}/api/v1/oauth/token
Anduril-Sandbox-Authorization: Bearer {SANDBOXES_BEARER}
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}
```

Expect **HTTP 200** and JSON `access_token` + `expires_in` (~1800).

Then:

```http
PUT https://{LATTICE_ENDPOINT}/api/v1/entities
Authorization: Bearer {access_token}
Anduril-Sandbox-Authorization: Bearer {SANDBOXES_BEARER}
Content-Type: application/json

{ ... entity with entityId ... }
```

## Env var convention (Polybolos doors)

| Variable | Maps to |
|----------|---------|
| `LATTICE_ENDPOINT` | host:port (no path), e.g. `lattice-abc.env.sandboxes.developer.anduril.com:443` |
| `LATTICE_CLIENT_ID` | Client ID |
| `LATTICE_CLIENT_SECRET` | Client Secret |
| `LATTICE_ENV_TOKEN` | **Sandboxes Bearer** (name is historical - it is *not* the Environment JWT) |

## Common failures

| Symptom | Likely cause |
|---------|----------------|
| OAuth **401** | Environment JWT used as Sandboxes Bearer; or wrong client id/secret for this env |
| OAuth / PUT connection reset | Dead/expired env, or Windows TLS path issues - try `auth_check.py`, then [mock-lattice](https://github.com/Polybolos-Institute/mock-lattice) offline |
| PUT **403** mid-batch | Sandbox intake limit - count ok/fail; do not invent permanent client throttle as “the fix” |
| UI works, API fails | UI user/password ≠ API credentials |

## Smoke

```bash
python scripts/auth_check.py
```
