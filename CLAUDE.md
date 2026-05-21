\# PoE 2 Knowledge Base — Protocol



База знаний по Path of Exile 2: механики, скиллы, крафт, предметы, билды.

Источник: Web Clipper-снапшоты официальной/фанатской вики в raw/.



\## Reading order



1\. Read `index.md` to find relevant wiki pages

2\. Read specific `wiki/{category}/\*.md` pages pointed to by index

3\. Read `raw/` ONLY if wiki page is incomplete or user asks to re-check source

4\. NEVER scan wiki/ directory blindly — always go through index.md



\## Write rules



\- `raw/`   — NEVER edit. Source material from Web Clipper. Immutable.

\- `wiki/`  — Claude writes and maintains.

\- `index.md` — update when wiki pages are added/removed.



\## Wikilinks



\- All wiki pages MUST use `\[\[wikilinks]]` to reference related concepts.

\- If a concept has no page yet — still create the `\[\[link]]`. Obsidian shows

&#x20; unresolved links on the graph as gaps to fill later.

\- When creating a new page, check existing pages for mentions of this concept

&#x20; and add `\[\[links]]` retroactively (backlink hygiene).



\## Categories



\- `mechanics/`  — game systems (damage, defenses, ailments, leveling, etc.)

\- `skills/`     — skill gems, support gems, interactions

\- `crafting/`   — crafting methods, currencies, strategies

\- `items/`      — item bases, uniques, modifiers

\- `builds/`     — build archetypes, synthesized from multiple sources

\- `glossary/`   — short definitions of terms (1-3 lines each)



\## Ingest workflow (when user adds a raw file)



1\. Read the raw file from `raw/`

2\. Identify category and key concepts

3\. Create or update wiki pages in `wiki/{category}/`

4\. Add `\[\[wikilinks]]` to related concepts (existing and not-yet-existing)

5\. Update `index.md` with new pages

6\. Update existing pages with backlinks if relevant

7\. Tell user what was added/changed



\## Query workflow



1\. Read `index.md`, find 2-5 relevant pages

2\. Read those pages

3\. Synthesize answer with `\[\[wikilink]]` citations

4\. If answer is valuable and not in wiki — offer to save as new page



\## Frontmatter for wiki pages



```yaml

\---

category: mechanics | skills | crafting | items | builds | glossary

sources: \[raw/path/file1.md, raw/path/file2.md]

patch: 0.X.X      # PoE 2 version this info is verified against

updated: YYYY-MM-DD

\---

```



\## Frontmatter for raw files (Web Clipper template)



```yaml

\---

source\_url: https://...

clipped: YYYY-MM-DD

patch: 0.X.X

status: raw

\---

```



\## Compilation rules



\- Don't create a wiki page for every term mentioned. Create when:

&#x20; - Concept appears in 2+ raw sources, OR

&#x20; - User explicitly asks for a page on it, OR

&#x20; - It's a build/strategy that synthesizes multiple mechanics

\- Short definitions (1-3 lines) go to `glossary/`, not standalone pages.

\- Always note the patch version in frontmatter — game changes frequently.

