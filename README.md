# anduril-lattice-sandbox-dx

## Status & recognition (factual)
**OASW(SO/LIC) Accelerator Event - July 2026 (GoColosseum)**  
Submission status: **Selected**. Per the portal, Selected means the submission was found **technically meritorious** and is under evaluation/consideration. 
**AFRL engagement - April 2026**  
COMMAND HOTL materials were provided to Air Force Research Laboratory contacts at their request:
- **Col Christopher Rondeau (AFRL/RQ):** after receiving the package, requested permission to share it with additional colleagues while **building out this portfolio**; permission granted (**portfolio review / distribution interest**).
- **Isaac Weintraub, PhD (Control Science Center, Air Warfare Directorate / RA):** detailed technical Q&A on risk awareness, weaponeering, kinematics, and coordination. He wrote that the exchange helped him understand **"the state of the art"** and what can be gained through **future partnerships**, and indicated he would convey **SBIR** topic materials and/or partnering.
That is attributed scientific and portfolio dialogue. 
**Technology maturity**  
Command HOTL is assessed at **TRL 5** (lab / SITL / controlled demo / Lattice developer sandbox). Decision-C2 / human-on-the-loop authority lineage. 
**Lattice**  
Sandbox / interoperability evidence (including documented scale publish-ingest work) supports Lattice-edge integration feasibility. Not a production Lattice mesh claim. Independent of Anduril; samples are not Anduril products.
**Inquiries:** mark.brown@polybolos.org  
CAGE: 1AVY9 · UEI: RUSHH9B2UQV3 · Polybolos Institute

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

## Contact

This repository is the open foundation (MIT).

Polybolos Institute also maintains a proprietary catalog of additional capabilities that are not published here. Contact us to discuss production deployment and commercial licensing.

mark.brown@polybolos.org · https://www.polybolos.org
