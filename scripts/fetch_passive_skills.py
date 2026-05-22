"""
Fetch Fextralife Passive Skill pages (Notables + Keystones).

Many passives don't have individual pages — high 404 rate is expected.
Index source (raw/Clippings/Passive Skills.md) already has names/type/effect
for all 1100 passives; per-page fetches are bonus for those that exist.

Strategy:
- Parse Notable + Keystone names from the index table
- Strip leading "..." prefix (some names like "...and I Shall Rage" — URL
  uses no ellipsis)
- Skip names already present as files anywhere in raw/Clippings/
- Fetch the rest; no sleep on 404

Usage:
    python scripts/fetch_passive_skills.py [--force] [--dry-run]
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
INDEX_FILE = ROOT / "raw" / "Clippings" / "Passive Skills.md"
OUT_DIR = ROOT / "raw" / "Clippings" / "passive-skills"

ROW_RE = re.compile(r"^\| ([^|]+?) \| (Notable|Keystone) \|", re.MULTILINE)


def read_names() -> list[str]:
    text = INDEX_FILE.read_text(encoding="utf-8")
    seen: set[str] = set()
    names: list[str] = []
    for raw, _type in ROW_RE.findall(text):
        name = raw.strip()
        # Strip leading "..." (a few notables have ellipsis prefix in index)
        name = re.sub(r"^\.{3}\s*", "", name)
        if name and name not in seen:
            seen.add(name)
            names.append(name)
    return names


def existing_stems() -> set[str]:
    stems: set[str] = set()
    for sub in ("skills", "support-gems", "ascendancy-notables", "ascendancies", "passive-skills"):
        d = ROOT / "raw" / "Clippings" / sub
        if d.exists():
            for f in d.glob("*.md"):
                stems.add(f.stem)
    return stems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--delay", type=float, default=1.0, help="delay after a successful fetch")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    names = read_names()
    existing = existing_stems() if not args.force else set()
    new = [n for n in names if safe_filename(n) not in existing]
    if args.limit:
        new = new[: args.limit]

    print(f"Total notables+keystones: {len(names)}")
    print(f"Already have (any folder): {len(names) - len(new)}, attempting: {len(new)}")

    if args.dry_run:
        for n in new[:30]:
            print(f"  NEW {n}")
        if len(new) > 30:
            print(f"  ... and {len(new) - 30} more")
        return 0

    counts = {"ok": 0, "skip": 0, "fail": 0, "404": 0}
    for i, name in enumerate(new, 1):
        out_path = OUT_DIR / f"{safe_filename(name)}.md"
        if out_path.exists() and not args.force:
            counts["skip"] += 1
            continue
        url = url_for(name)
        html = fetch(url)
        if html is None:
            counts["404"] += 1
            if i % 50 == 0:
                print(f"[{i}/{len(new)}] (last: {name} — 404)")
            continue
        body = extract_markdown(html)
        if body is None or len(body) < 200:
            counts["fail"] += 1
            print(f"[{i}/{len(new)}] {name} — empty")
            continue
        write_clipping(name, url, body, out_path)
        counts["ok"] += 1
        print(f"[{i}/{len(new)}] {name} — ok")
        time.sleep(args.delay)

    print("\n=== Summary ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
