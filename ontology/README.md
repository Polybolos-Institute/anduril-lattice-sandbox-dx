# Ontology cheat sheet (door-facing)

Suggested Lattice entity fields for **publish doors**. This is not a C2 class
map and not an engagement ICD.

## Rules of thumb

1. Always set `entityId`, `isLive`, `expiryTime`, `location.position`, `ontology`, `provenance`.
2. Prefer Lattice UI vocabulary for `platformType` when you know it (e.g. `ADS-B AIRPLANE`, `UAV`).
3. If you do **not** know the type, publish as unknown **or** skip - do not invent a specific combat class.
4. `provenance.dataType` should reflect the sensor (`adsb`, `mavlink_telemetry`, `ais`, …).
5. Ownship / cooperative vehicles: `DISPOSITION_FRIENDLY`. Uncorrelated public ADS-B: usually `DISPOSITION_UNKNOWN`.

## Files

- [`door_defaults.json`](door_defaults.json) - machine-readable defaults keyed by door source

## Out of scope

Mapping into any private engage taxonomy, ROE, or authority matrix. Those stay in your C2 product, not in this kit.
