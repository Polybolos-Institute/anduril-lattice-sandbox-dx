"""Validate ontology/door_defaults.json shape."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY = ROOT / "ontology" / "door_defaults.json"


def test_door_defaults_shape():
    data = json.loads(ONTOLOGY.read_text(encoding="utf-8"))
    assert data["version"] == 1
    sources = data["sources"]
    assert "mavlink_ownship" in sources
    assert "opensky_adsb" in sources
    for key, src in sources.items():
        assert "ontology" in src, key
        assert "template" in src["ontology"], key
        assert "platformType" in src["ontology"], key
        assert "milView" in src, key
        assert "provenance" in src, key
    assert isinstance(data["common_platform_types"], list)
    assert "ADS-B AIRPLANE" in data["common_platform_types"]
