"""
Fetch the 22 ascendancy class pages (Stormweaver, Witchhunter, etc.).

Reads canonical URL list parsed from raw/Clippings/Ascendancies.md.
Saves to raw/Clippings/ascendancies/<Name>.md.

Usage:
    python scripts/fetch_ascendancy_classes.py [--force]
"""

from __future__ import annotations
import argparse
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_skills import fetch, extract_markdown, write_clipping, safe_filename, BASE_URL

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "raw" / "Clippings" / "Ascendancies.md"
OUT_DIR = ROOT / "raw" / "Clippings" / "ascendancies"

KNOWN = {
    "Witchhunter", "Gemling Legionnaire", "Tactician",
    "Invoker", "Acolyte of Chayula", "Martial Artist",
    "Deadeye", "Pathfinder",
    "Amazon", "Ritualist", "Spirit Walker",
    "Stormweaver", "Chronomancer", "Disciple of Varashta",
    "Warbringer", "Titan", "Smith of Kitava",
    "Blood Mage", "Infernalist", "Lich",
    "Oracle", "Shaman",
}

LINK_RE = re.compile(r"\[([A-Z][A-Za-z' ]+?)\]\((/[A-Za-z'\+]+) \"Path of Exile 2")


def read_targets() -> list[tuple[str, str]]:
    text = INDEX_FILE.read_text(encoding="utf-8")
    seen: set[str] = set()
    targets: list[tuple[str, str]] = []
    for name, path in LINK_RE.findall(text):
        n = name.strip()
        if n in KNOWN and n not in seen:
            seen.add(n)
            targets.append((n, BASE_URL + path))
    return targets


def process(name: str, url: str, *, force: bool) -> str:
    out_path = OUT_DIR / f"{safe_filename(name)}.md"
    if out_path.exists() and not force:
        return "skip"
    html = fetch(url)
    if html is None:
        return "404"
    body = extract_markdown(html)
    if body is None or len(body) < 200:
        return "fail"
    write_clipping(name, url, body, out_path)
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--delay", type=float, default=1.0)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    targets = read_targets()
    print(f"Total ascendancies to process: {len(targets)}")
    counts = {"ok": 0, "skip": 0, "fail": 0, "404": 0}
    for i, (name, url) in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {name}")
        r = process(name, url, force=args.force)
        counts[r] += 1
        if r == "ok":
            time.sleep(args.delay)
    print("\n=== Summary ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
