"""
Mass-fetch Fextralife PoE 2 Support Gem pages.

Parses raw/Clippings/Support Gems.md for #### links and downloads each.
URL is taken verbatim from the source markdown (handles disambiguation suffixes
like "Ixchel's+Torment+(Support+Gem)" correctly).

Usage:
    python scripts/fetch_support_gems.py [--force] [--limit N]
"""

from __future__ import annotations
import argparse
import re
import sys
import time
import urllib.parse
from pathlib import Path

# Reuse helpers from sibling script
sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_skills import fetch, extract_markdown, write_clipping, safe_filename, BASE_URL

ROOT = Path(__file__).resolve().parent.parent
INDEX_FILE = ROOT / "raw" / "Clippings" / "Support Gems.md"
OUT_DIR = ROOT / "raw" / "Clippings" / "support-gems"

# Matches:  #### [... Name](/Url+Path "Path of Exile 2 ...")
LINK_RE = re.compile(r'^####\s+\[[^\]]+\]\((/[^)"\s]+)\s+"')


def url_to_name(url_path: str) -> str:
    # /Ixchel%27s+Torment+(Support+Gem)  →  Ixchel's Torment (Support Gem)
    decoded = urllib.parse.unquote(url_path.lstrip("/"))
    return decoded.replace("+", " ")


def read_targets(index_path: Path) -> list[tuple[str, str]]:
    targets: list[tuple[str, str]] = []
    seen: set[str] = set()
    for line in index_path.read_text(encoding="utf-8").splitlines():
        m = LINK_RE.match(line)
        if not m:
            continue
        path = m.group(1)
        url = BASE_URL + path
        name = url_to_name(path)
        if name in seen:
            continue
        seen.add(name)
        targets.append((name, url))
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
        print(f"  ! empty content for {name}")
        return "fail"
    write_clipping(name, url, body, out_path)
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--delay", type=float, default=1.0)
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    targets = read_targets(INDEX_FILE)
    if args.limit:
        targets = targets[: args.limit]

    print(f"Total support gems to process: {len(targets)}")
    counts = {"ok": 0, "skip": 0, "fail": 0, "404": 0}
    for i, (name, url) in enumerate(targets, 1):
        print(f"[{i}/{len(targets)}] {name}")
        result = process(name, url, force=args.force)
        counts[result] += 1
        if result == "ok":
            time.sleep(args.delay)

    print("\n=== Summary ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
