---
title: "Missing skill pages"
clipped: 2026-05-21
patch: 0.4.0
status: meta
---

# Missing on Fextralife

Скиллы есть в категорийном списке [Skills](https://pathofexile2.wiki.fextralife.com/Skills),
но отдельной wiki-страницы на Fextralife у них нет (HTTP 404):

- **Blood Boil** — встречается как Buff Skill (Pillar of the Caged God / Ascendancy notable [[Corrupted Lifeforce]]). Эффекты — см. [Skills.md](../Skills.md).
- **Ritual Sacrifice** — встречается как Buff. Эффекты — там же.
- **Snap** — Spell skill (cold-конверт). Эффекты — там же.

При создании wiki-страниц по этим скиллам использовать данные из таблиц
[raw/Clippings/Skills.md](../Skills.md) и помечать `sources` соответствующе.

Проверено: 2026-05-21. Если Fextralife добавит страницы — перезапустить
`scripts/fetch_skills.py --only "Blood Boil,Ritual Sacrifice,Snap"`.
