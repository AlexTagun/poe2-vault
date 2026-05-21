"""
Parse the 22 ascendancy class pages for ALL notable/passive node URLs,
deduplicate, diff against already-downloaded notables, fetch the rest.

Reads: raw/Clippings/ascendancies/*.md
Writes new files to: raw/Clippings/ascendancy-notables/

Usage:
    python scripts/fetch_all_notables.py [--force] [--dry-run]
"""

from __future__ import annotations
import argparse
import re
import sys
import time
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_skills import fetch, extract_markdown, write_clipping, safe_filename, BASE_URL

ROOT = Path(__file__).resolve().parent.parent
ASC_DIR = ROOT / "raw" / "Clippings" / "ascendancies"
OUT_DIR = ROOT / "raw" / "Clippings" / "ascendancy-notables"

LINK_RE = re.compile(r'\((/([^"\s)]+))\s+"Path of Exile 2 [^"]+"\)')
# Header that starts the skills table
SECTION_RE = re.compile(
    r"^### Path of Exile 2 \(PoE 2\) .+? (?:Skills|Skill Gems)\b",
    re.MULTILINE,
)


def url_to_name(slug: str) -> str:
    decoded = urllib.parse.unquote(slug)
    return decoded.replace("+", " ")


def extract_from(path: Path) -> set[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    m = SECTION_RE.search(text)
    if not m:
        print(f"  ! no Skills section in {path.name}")
        return set()
    section = text[m.end():]
    # Stop at next H3
    end = re.search(r"^### ", section, re.MULTILINE)
    if end:
        section = section[: end.start()]
    out: set[tuple[str, str]] = set()
    for path_part, slug in LINK_RE.findall(section):
        name = url_to_name(slug)
        # Filter out things that are clearly not notable/passive nodes
        if any(kw in name.lower() for kw in (
            "skill+gem", "support+gem", "stats", "passive+skills",
            "weapons", "ascendanc", "wiki", "elemental+damage+passive",
        )):
            continue
        url = BASE_URL + path_part
        out.add((name, url))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--delay", type=float, default=1.0)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    all_targets: dict[str, str] = {}
    for asc_file in sorted(ASC_DIR.glob("*.md")):
        found = extract_from(asc_file)
        print(f"{asc_file.stem}: {len(found)} links")
        for name, url in found:
            all_targets.setdefault(name, url)

    print(f"\nTotal unique links across ascendancies: {len(all_targets)}")

    # Diff against existing
    existing = {p.stem for p in OUT_DIR.glob("*.md")}
    new = {n: u for n, u in all_targets.items() if safe_filename(n) not in existing}
    print(f"Already have: {len(all_targets) - len(new)}, new to fetch: {len(new)}")

    if args.dry_run:
        for n, u in sorted(new.items()):
            print(f"  NEW {n}  ->  {u}")
        return 0

    counts = {"ok": 0, "skip": 0, "fail": 0, "404": 0}
    items = sorted(new.items())
    for i, (name, url) in enumerate(items, 1):
        print(f"[{i}/{len(items)}] {name}")
        out_path = OUT_DIR / f"{safe_filename(name)}.md"
        if out_path.exists() and not args.force:
            counts["skip"] += 1
            continue
        html = fetch(url)
        if html is None:
            counts["404"] += 1
            print(f"  ! 404")
            continue
        body = extract_markdown(html)
        if body is None or len(body) < 200:
            counts["fail"] += 1
            print(f"  ! empty")
            continue
        write_clipping(name, url, body, out_path)
        counts["ok"] += 1
        time.sleep(args.delay)

    print("\n=== Summary ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
