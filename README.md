# anduril-lattice-sandbox-dx

Anduril Lattice Sandboxes **developer experience** kit + a small **ontology cheat sheet** for
people writing Lattice doors. Built by [Polybolos Institute](https://www.polybolos.org).

No C2 core. No ROE. No engagement ICD. Docs and helpers only.
**Independent sample - not an Anduril product.**

## What's in here

| Path | Purpose |
|------|---------|
| [`docs/AUTH_CHECKLIST.md`](docs/AUTH_CHECKLIST.md) | Which token is which (Bearer vs client vs env JWT vs UI user) |
| [`docs/SANDBOX_LIFECYCLE.md`](docs/SANDBOX_LIFECYCLE.md) | Expiry / idle / reconnect habits |
| [`docs/WINDOWS_TLS.md`](docs/WINDOWS_TLS.md) | Live HTTPS vs `anduril-mock-lattice` HTTP loopback |
| [`ontology/door_defaults.json`](ontology/door_defaults.json) | Suggested entity fields for common door sources |
| [`ontology/README.md`](ontology/README.md) | How to use the cheat sheet (fail-closed guidance) |
| [`scripts/auth_check.py`](scripts/auth_check.py) | OAuth-only smoke (`--auth-only` style) |

## Quick start

```bash
cd anduril-lattice-sandbox-dx
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
copy .env.example .env
# fill LATTICE_* then:
python scripts/auth_check.py
```

Against [anduril-mock-lattice](https://github.com/Polybolos-Institute/anduril-mock-lattice):

```powershell
# terminal A
python -m mock_lattice   # from the anduril-mock-lattice repo

# terminal B
$env:LATTICE_ENDPOINT="127.0.0.1:8765"
$env:LATTICE_CLIENT_ID="test-client-id"
$env:LATTICE_CLIENT_SECRET="test-client-secret"
$env:LATTICE_ENV_TOKEN="test-sandbox-token"
python scripts/auth_check.py
```

## Related doors

- [anduril-mavlink-lattice-bridge](https://github.com/Polybolos-Institute/anduril-mavlink-lattice-bridge)
- [anduril-opensky-lattice-bridge](https://github.com/Polybolos-Institute/anduril-opensky-lattice-bridge)
- [anduril-dump1090-lattice-bridge](https://github.com/Polybolos-Institute/anduril-dump1090-lattice-bridge)
- [anduril-lattice-rest-winhttp](https://github.com/Polybolos-Institute/anduril-lattice-rest-winhttp)
- [anduril-lattice-stream-watcher](https://github.com/Polybolos-Institute/anduril-lattice-stream-watcher)
- [anduril-lattice-entity-fixtures](https://github.com/Polybolos-Institute/anduril-lattice-entity-fixtures)
- [anduril-mock-lattice](https://github.com/Polybolos-Institute/anduril-mock-lattice)

## License

MIT - see [LICENSE](LICENSE).

Anduril® and Lattice® are trademarks of Anduril Industries.
This is an independent DX sample, not an Anduril product.
