"""Fetch the immutable IIIF schema into this checkout's ignored cache; never vendor it."""

import hashlib
import json
import re
import sys
import tempfile
import urllib.request
from pathlib import Path

PIN = Path("standards/iiif-presentation-3-3891f47/pin.json")
CACHE = Path("standards/.cache/iiif-presentation-3-3891f47/iiif_3_0.json")


def fetch(root=None):
    """Return a hash-verified file, downloading only when absent. All failures propagate."""
    root = Path(__file__).resolve().parents[1] if root is None else Path(root)
    pin = json.loads((root / PIN).read_text(encoding="utf-8"))
    source = pin["files"]["iiif_3_0.json"]
    url = (
        f"https://raw.githubusercontent.com/IIIF/presentation-validator/"
        f"{pin['commit']}/schema/iiif_3_0.json"
    )
    if (
        pin["repo"] != "IIIF/presentation-validator"
        or not re.fullmatch(r"[0-9a-f]{40}", pin["commit"])
        or source["path"] != "schema/iiif_3_0.json"
        or source["url"] != url
        or not re.fullmatch(r"[0-9a-f]{64}", source["sha256"])
    ):
        raise ValueError(
            "invalid IIIF schema pin: expected an immutable raw GitHub URL and SHA-256"
        )

    target = root / CACHE
    cached = target.exists()
    if cached:
        raw = target.read_bytes()
    else:
        # iiif-prezi3 utils/regenerate_skeleton.py, read 31 October 2026:
        # https://github.com/iiif-prezi/iiif-prezi3/blob/main/utils/regenerate_skeleton.py
        # Fetch at use; here the URL is a full commit, never a moving branch.
        # Python 3.11 urllib.request (urlopen context manager, timeout), read 31 October 2026:
        # https://docs.python.org/3.11/library/urllib.request.html
        with urllib.request.urlopen(url, timeout=30) as response:
            raw = response.read()
    actual = hashlib.sha256(raw).hexdigest()
    if actual != source["sha256"]:
        raise ValueError(
            f"IIIF schema SHA-256 mismatch: expected {source['sha256']}, got {actual}; "
            f"refusing {target if target.exists() else url}"
        )
    if not cached:
        target.parent.mkdir(parents=True, exist_ok=True)
        # Publish complete, verified bytes atomically; parallel callers never see a partial file.
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as handle:
                temporary = Path(handle.name)
                handle.write(raw)
            temporary.replace(target)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
    return target


if __name__ == "__main__":
    try:
        print(fetch())
    except (OSError, ValueError, KeyError, TypeError) as error:
        sys.exit(f"IIIF schema fetch failed: {error}")
