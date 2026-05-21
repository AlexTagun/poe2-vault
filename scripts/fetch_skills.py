"""
Mass-fetch Fextralife PoE 2 skill pages and save as markdown clippings.

- Reads skill names from raw/Clippings/Skills.md (lines starting with `| #### `)
- Fetches each https://pathofexile2.wiki.fextralife.com/<Name+with+pluses>
- Strips junk (scripts, iframes, ads), converts main content to markdown
- Writes raw/Clippings/skills/<Name>.md with frontmatter
- Idempotent: skips already-downloaded files (use --force to override)
- Rate-limited; retries 502/503/timeouts

Usage:
    python scripts/fetch_skills.py              # download all missing
    python scripts/fetch_skills.py --force      # re-download everything
    python scripts/fetch_skills.py --limit 5    # only first 5 (smoke test)
    python scripts/fetch_skills.py --only "Stormblast Bolts,Apocalypse"
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
INDEX_FILE = ROOT / "raw" / "Clippings" / "Skills.md"
OUT_DIR = ROOT / "raw" / "Clippings" / "skills"
BASE_URL = "https://pathofexile2.wiki.fextralife.com"
PATCH = "0.4.0"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
}

SKILL_LINE_RE = re.compile(r"^\| #### (.+?) \|")


def read_skill_names(index_path: Path) -> list[str]:
    names: list[str] = []
    seen: set[str] = set()
    for line in index_path.read_text(encoding="utf-8").splitlines():
        m = SKILL_LINE_RE.match(line)
        if not m:
            continue
        name = m.group(1).strip()
        if name in seen:
            continue
        seen.add(name)
        names.append(name)
    return names


def safe_filename(name: str) -> str:
    # Keep human-readable, just remove path-unsafe chars
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def url_for(name: str) -> str:
    return f"{BASE_URL}/{name.replace(' ', '+')}"


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
    # remove junk
    for tag in content.select(
        "script, style, iframe, noscript, .ad-container, .ads, "
        ".advertisement, .fex-leaderboard, .fex-mpu"
    ):
        tag.decompose()
    text = md(str(content), heading_style="ATX")
    # collapse 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    return text


def write_clipping(name: str, url: str, body: str, out_path: Path) -> None:
    today = date.today().isoformat()
    frontmatter = (
        "---\n"
        f"title: \"{name}\"\n"
        f"source_url: {url}\n"
        f"clipped: {today}\n"
        f"patch: {PATCH}\n"
        "status: raw\n"
        "tags:\n  - clippings\n  - skill\n"
        "---\n\n"
    )
    out_path.write_text(frontmatter + body, encoding="utf-8")


def process(name: str, *, force: bool) -> str:
    """Returns one of: 'skip', 'ok', 'fail', '404'."""
    out_path = OUT_DIR / f"{safe_filename(name)}.md"
    if out_path.exists() and not force:
        return "skip"
    url = url_for(name)
    html = fetch(url)
    if html is None:
        return "404"
    body = extract_markdown(html)
    if body is None or len(body) < 200:
        print(f"  ! empty/too-short content for {name}")
        return "fail"
    write_clipping(name, url, body, out_path)
    return "ok"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-download even if file exists")
    ap.add_argument("--limit", type=int, default=0, help="process only first N skills")
    ap.add_argument(
        "--only",
        type=str,
        default="",
        help="comma-separated list of skill names (overrides --limit)",
    )
    ap.add_argument("--delay", type=float, default=1.0, help="seconds between requests")
    args = ap.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.only:
        names = [n.strip() for n in args.only.split(",") if n.strip()]
    else:
        names = read_skill_names(INDEX_FILE)
        if args.limit:
            names = names[: args.limit]

    print(f"Total skills to process: {len(names)}")
    counts = {"ok": 0, "skip": 0, "fail": 0, "404": 0}
    for i, name in enumerate(names, 1):
        print(f"[{i}/{len(names)}] {name}")
        result = process(name, force=args.force)
        counts[result] += 1
        if result == "ok":
            time.sleep(args.delay)

    print("\n=== Summary ===")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    return 0 if counts["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
