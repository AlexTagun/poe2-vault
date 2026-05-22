"""
Mass-fetch Fextralife PoE 2 unique item pages and save as markdown clippings.

- Fetches the index page https://pathofexile2.wiki.fextralife.com/Unique+Equipment
  and saves it to raw/Clippings/Unique Equipment.md
- Parses all unique item links from the index table
- Fetches each item page and saves to raw/Clippings/uniques/<Name>.md
- Idempotent: skips already-downloaded files (use --force to override)
- Rate-limited; retries 502/503/timeouts

Usage:
    python scripts/fetch_uniques.py              # download all missing
    python scripts/fetch_uniques.py --force      # re-download everything
    python scripts/fetch_uniques.py --limit 5    # only first 5 (smoke test)
    python scripts/fetch_uniques.py --only "Shavronne's Wrappings,Kaom's Heart"
    python scripts/fetch_uniques.py --index-only # only save/refresh the index
"""

from __future__ import annotations
import argparse
import re
import sys
import time
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = Path(__file__).resolve().parent.parent
INDEX_URL = "https://pathofexile2.wiki.fextralife.com/Unique+Equipment"
INDEX_FILE = ROOT / "raw" / "Clippings" / "Unique Equipment.md"
OUT_DIR = ROOT / "raw" / "Clippings" / "uniques"
BASE_URL = "https://pathofexile2.wiki.fextralife.com"
PATCH = "0.2.0"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}


def safe_filename(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def fetch(url: str, max_retries: int = 4) -> str | None:
    for attempt in range(1, max_retries + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=30)
        except requests.RequestException as e:
            print(f"  ! request error {e!r} (attempt {attempt})")
            time.sleep(2 * attempt)
            continue
        if r.status_code == 200:
            r.encoding = "utf-8"
            return r.text
        if r.status_code in (404, 410):
            print(f"  ! {r.status_code} — page does not exist")
            return None
        print(f"  ! status {r.status_code} (attempt {attempt})")
        time.sleep(2 * attempt)
    return None


def extract_markdown(html: str) -> str | None:
    soup = BeautifulSoup(html, "lxml")
    content = soup.select_one("#wiki-content-block")
    if content is None:
        return None
    for tag in content.select(
        "script, style, iframe, noscript, .ad-container, .ads, "
        ".advertisement, .fex-leaderboard, .fex-mpu"
    ):
        tag.decompose()
    text = md(str(content), heading_style="ATX")
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def write_clipping(name: str, url: str, body: str, out_path: Path, tag: str) -> None:
    today = date.today().isoformat()
    frontmatter = (
        "---\n"
        f"title: \"{name}\"\n"
        f"source_url: {url}\n"
        f"clipped: {today}\n"
        f"patch: {PATCH}\n"
        "status: raw\n"
        f"tags:\n  - clippings\n  - {tag}\n"
        "---\n\n"
    )
    out_path.write_text(frontmatter + body, encoding="utf-8")


def save_index(force: bool = False) -> str | None:
    """Fetch the index page and save to raw/Clippings/Unique Equipment.md.
    Returns the HTML text for further parsing."""
    if INDEX_FILE.exists() and not force:
        print(f"[index] already exists, skipping (use --force to refresh)")
        return INDEX_FILE.read_text(encoding="utf-8")

    print(f"[index] fetching {INDEX_URL} ...")
    html = fetch(INDEX_URL)
    if html is None:
        print("[index] FAILED to fetch index page")
        return None

    body = extract_markdown(html)
    if body is None:
        print("[index] could not extract content")
        return None

    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    write_clipping("Unique Equipment", INDEX_URL, body, INDEX_FILE, "unique-index")
    print(f"[index] saved to {INDEX_FILE.relative_to(ROOT)}")
    return html


def parse_unique_links(html: str) -> list[tuple[str, str]]:
    """Parse unique item (name, url) pairs from the index page HTML.
    Returns list of (display_name, full_url)."""
    soup = BeautifulSoup(html, "lxml")
    content = soup.select_one("#wiki-content-block")
    if content is None:
        return []

    results: list[tuple[str, str]] = []
    seen: set[str] = set()

    # Unique items are in table rows; first <td> contains the link to the item page
    for row in content.select("table tr"):
        cells = row.select("td")
        if not cells:
            continue
        first_cell = cells[0]
        link = first_cell.select_one("a[href]")
        if link is None:
            continue
        href = link.get("href", "")
        # Only keep wiki-internal item links (relative paths or same-domain)
        if not href:
            continue
        if href.startswith("http") and BASE_URL not in href:
            continue
        # Normalise to full URL
        if href.startswith("/"):
            full_url = BASE_URL + href
        elif href.startswith(BASE_URL):
            full_url = href
        else:
            continue

        # Extract only the unique name — the cell has "UniqueName<br>BaseType"
        # inside the <a>, so we take only the first non-empty text node.
        raw_parts = [t.strip() for t in link.strings if t.strip()]
        name = raw_parts[0] if raw_parts else link.get_text(strip=True)
        if not name or name in seen:
            continue
        if len(name) < 2:
            continue

        seen.add(name)
        results.append((name, full_url))

    return results


def process(name: str, url: str, *, force: bool) -> str:
    """Returns one of: 'skip', 'ok', 'fail', '404'."""
    out_path = OUT_DIR / f"{safe_filename(name)}.md"
    if out_path.exists() and not force:
        return "skip"
    html = fetch(url)
    if html is None:
        return "404"
    body = extract_markdown(html)
    if body is None or len(body) < 200:
        print(f"  ! empty/too-short content for {name}")
        return "fail"
    write_clipping(name, url, body, out_path, "unique")
    return "ok"


def main() -> int:
    # Force UTF-8 output on Windows consoles that default to cp1251/cp1252
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-download even if file exists")
    ap.add_argument("--limit", type=int, default=0, help="process only first N items")
    ap.add_argument(
        "--only",
        type=str,
        default="",
        help="comma-separated list of unique names (overrides --limit)",
    )
    ap.add_argument("--delay", type=float, default=1.2, help="seconds between requests")
    ap.add_argument("--index-only", action="store_true", help="only save/refresh the index page")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # Always fetch the live HTML for link parsing; save index file too
    print(f"Fetching index page ...")
    index_html = fetch(INDEX_URL)
    if index_html is None:
        print("ERROR: could not fetch index page")
        return 1

    # Save index markdown (skip if exists and not --force)
    if not INDEX_FILE.exists() or args.force:
        body = extract_markdown(index_html)
        if body:
            INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
            write_clipping("Unique Equipment", INDEX_URL, body, INDEX_FILE, "unique-index")
            print(f"Saved index -> {INDEX_FILE.relative_to(ROOT)}")
    else:
        print(f"Index already exists at {INDEX_FILE.relative_to(ROOT)}")

    if args.index_only:
        return 0

    # Parse item links from live HTML
    items = parse_unique_links(index_html)
    if not items:
        print("ERROR: could not parse any unique item links from index page")
        return 1
    print(f"Found {len(items)} unique items in index")

    if args.only:
        only_names = {n.strip().lower() for n in args.only.split(",") if n.strip()}
        items = [(n, u) for n, u in items if n.lower() in only_names]
    elif args.limit:
        items = items[: args.limit]

    print(f"Processing {len(items)} items ...")
    counts = {"ok": 0, "skip": 0, "fail": 0, "404": 0}
    for i, (name, url) in enumerate(items, 1):
        print(f"[{i}/{len(items)}] {name}")
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
