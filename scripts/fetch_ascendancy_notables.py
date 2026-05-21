"""
Mass-fetch Fextralife PoE 2 Ascendancy notable pages.

Reads names from the `### All Ascendancy Skills` section of
raw/Clippings/Skills.md (lines starting with `| ##### `) and downloads each
as <Name>.md into raw/Clippings/ascendancy-notables/.

Some entries duplicate skill names (notable that grants a skill, e.g.
"Bleeding Concoction"). We still fetch them — notable pages describe the
notable's passive effect, distinct from the skill page.

Usage:
    python scripts/fetch_ascendancy_notables.py [--force] [--limit N]
"""

from __future__ import annotations
import argparse
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_skills import fetch, extract_markdown, write_clipping, safe_filename, url_for

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "raw" / "Clippings" / "Skills.md"
OUT_DIR = ROOT / "raw" / "Clippings" / "ascendancy-notables"

ROW_RE = re.compile(r"^\| ##### (.+?) \|")


def read_names(index_path: Path) -> list[str]:
    text = index_path.read_text(encoding="utf-8")
    start = text.find("### All Ascendancy Skills")
    if start == -1:
        raise RuntimeError("Ascendancy section not found")
    section = text[start:]
    names: list[str] = []
    seen: set[str] = set()
    for line in section.splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = m.group(1).strip()
        if name.lower() == "skill name":  # table header
            continue
        if name in seen:
            continue
        seen.add(name)
        names.append(name)
    return names


def process(name: str, *, force: bool) -> str:
    out_path = OUT_DIR / f"{safe_filename(name)}.md"
    if out_path.exists() and not force:
        return "skip"
    url = url_for(name)
    html = fetch(url)
    if html is None:
        return "404"
    body = extract_markdown(html)
    if body is None or len(body) < 200:
        print(f"  ! empty content for {name}")
        return "fail"
    write_clipping(name, url, body, out_path)
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", type=str, default="")
    ap.add_argument("--delay", type=float, default=1.0)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if args.only:
        names = [n.strip() for n in args.only.split(",") if n.strip()]
    else:
        names = read_names(INDEX_FILE)
        if args.limit:
            names = names[: args.limit]

    print(f"Total notables to process: {len(names)}")
    counts = {"ok": 0, "skip": 0, "fail": 0, "404": 0}
    misses: list[str] = []
    for i, name in enumerate(names, 1):
        print(f"[{i}/{len(names)}] {name}")
        result = process(name, force=args.force)
        counts[result] += 1
        if result == "404":
            misses.append(name)
        if result == "ok":
            time.sleep(args.delay)

    print("\n=== Summary ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    if misses:
        print("\n404 list:")
        for n in misses:
            print(f"  - {n}")
    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
