---
category: builds
sources: [raw/poe-ninja-vaal-2026-05-24.md, raw/poe-ninja-runesofaldur-2026-06-01.md]
patch: 0.5.0
updated: 2026-06-01
---

# League Meta Snapshots

Хроника мета-замеров с [poe.ninja](https://poe.ninja/poe2/builds/). Каждый снапшот — фотография топа лиги: распределение по [[builds/ascendancies|ascendancy]], самые популярные [[items/items|items]], [[skills/skill-reference|skills]], нотейблы и анойнты на [[mechanics/passive-skill-tree|passive tree]], [[items/weapons/weapons|weapon configurations]].

Используется для:
- Сравнения patch-vs-patch: что подняли в мете, что обнулили нерфом.
- Бэйслайна перед патчем для прогноза изменений (если в текущей мете 17% — Blood Mage, и патч режет Sanguimancy, ожидаем обвал на 5-8 пунктов).
- Идентификации мест, требующих балансировочного внимания (всё что >30% использования на single-target меху ≈ TOP-tier; всё что <2% — потенциальный кандидат на бафф).

## Snapshots

| Дата | Лига | Patch | Чары в выборке | Файл |
|---|---|---|---|---|
| 2026-05-24 | Fate of the Vaal | 0.4.0 | 124 084 | [[raw/poe-ninja-vaal-2026-05-24]] |
| 2026-06-01 | Runes of Aldur | 0.5.0 | 83 589 | [[raw/poe-ninja-runesofaldur-2026-06-01]] |

## Headline Meta — Fate of the Vaal (2026-05-24)

**Топ ascendancy** (доля от всех персонажей лиги): [[builds/ascendancies/blood-mage|Blood Mage]] 17%, [[builds/ascendancies/oracle|Oracle]] 16%, [[builds/ascendancies/pathfinder|Pathfinder]] 12%, [[builds/ascendancies/shaman|Shaman]] 8%, [[builds/ascendancies/titan|Titan]] 6%.

**Топ main skills**: Comet 27% → Elemental Weakness 25% → Herald of Ice 20% → Spark 19% → Life Remnants 18% → Wind Dancer 18% → Herald of Thunder 16%.

**Топ items (не-rare/magic)**: Heart of the Well 49%, Headhunter 48%, Nascent Hope 42%, Lavianga's Spirits 38%, The Fall of the Axe 27%, The Vertex 26%, From Nothing 25%, [[items/jewellery/uniques|Kalandra's Touch]] 25%.

**Топ passives**: Mind Over Matter 20%, Sanguimancy 17%, Chaos Inoculation 17%, Grasping Wounds 16%, The Unseen Path 16%.

**Топ anoint**: Fast Metabolism 17% — единственный анойнт с двузначным процентом. Дальше Lasting Trauma 5%, Warlord Leader 4%, Overwhelming Strike 3% — длинный хвост, лиге нечего предложить большинству билдов.

**Топ weapon config**: Staff 15% (caster meta), Bow / Quiver 14%, Wand / Focus 11%, Talisman 10%. Двуручники, спирс на щите и unarmed — статистический шум.

**Топ supports / aura'ы** (All Skills): абсолютная доминанта area/duration supports — Magnified Area II 82%, Prolonged Duration II 74%, Efficiency II 53%, Cooldown Recovery II 51%, Concentrated Area 49%. Cast on Critical 37% — основной триггер. Heralds (Ice 22%, Thunder 17%, Ash 15%) — топ-вспомогательные ауры.

## Ключевые сигналы для прогноза патча

1. **Blood Mage + Sanguimancy / Mind Over Matter / Sanguis Heroum** — стек, держащий 17% мету. Любая правка этих узлов → массовый отток.
2. **Comet + Cast on Critical + Frost Bomb** — связка Stormweaver/Blood Mage, ~27% Comet ≈ верхний потолок одного скилла. Кандидат на нерф числовых модификаторов.
3. **Heart of the Well 49%** — флак, проникающий почти в каждый второй билд. Если попадёт под нерф uniques, удар поглотит почти все архетипы.
4. **Magnified Area II на 82%** — саппорт, который "обязателен". Возможный пересмотр стоимости / штрафов.
5. **Headhunter 48% + Kalandra's Touch 25%** — высокий процент юников намекает на инфляцию таргетного крафта; если выйдет orb-нерф, эти цифры просядут.

## Headline Meta — Runes of Aldur (2026-06-01) — ранний снапшот

> Лига свежая: 83k персонажей vs 124k в конце Fate of the Vaal. Максимальный уровень — 98.

**Топ ascendancy**: [[builds/ascendancies/martial-artist|Martial Artist]] 25% → [[builds/ascendancies/spirit-walker|Spirit Walker]] 17% → [[builds/ascendancies/deadeye|Deadeye]] 15% → Tactician 5% → Oracle 5%.

**Топ main skills**: Herald of Ice 27% → Ice-Tipped Arrows 20% → Barrage 17% → Freezing Mark 16% → Ice Shot 14% → Twister 14% → Snipe 14%.

**Топ items (не-rare/magic)**: Lochtonial Caress 9.5%, Wake of Destruction 7.2%, Arakaali's Gift 6.5%, Beira's Anguish 5.8%, Lavianga's Spirits 5.2%, Sanguis Heroum 5.1%, Breath of the Mountains 4.7%.

**Топ passives**: Way of the Stonefist 23%, Hollow Focus Technique 16%, Projectile Proximity Specialisation 13%, Dance with Death 13%, Point Blank 13%, Endless Munitions 13%.

**Топ anoint**: Well of Power 2.4% — всё в хвосте <1.5%. Лига слишком ранняя для массового анойнтинга.

**Топ weapon config**: Quarterstaff 18% > Bow/Quiver 15% > Crossbow 12% > Spear 10% > Staff 7%.

**Топ supports / ауры** (All Skills): Magnified Area II 69%, Prolonged Duration II 62%, Elemental Armament II 59%, Cooldown Recovery II 49%, Concentrated Area 40%. Herald of Ice 37% — главная аура лиги.

## Сравнение мет: 0.4.0 vs 0.5.0

| Метрика | Fate of the Vaal (0.4.0) | Runes of Aldur (0.5.0) | Изменение |
|---|---|---|---|
| #1 ascendancy | Blood Mage 17% | Martial Artist 25% | полная смена лидера |
| #2 ascendancy | Oracle 16% | Spirit Walker 17% | новый класс в топе |
| #3 ascendancy | Pathfinder 12% | Deadeye 15% | стабильно, рост |
| Топ main skill | Comet 27% | Herald of Ice 27% | Comet → 3% (нерф) |
| Blood Mage | 17% | 2% | обвал после нерфа |
| Стафы | Staff 15% | Staff 7% | вдвое меньше |
| Квотерстафы | нет в топ-5 | Quarterstaff 18% | новый лидер оружия |
| Cast on Critical | 37% | не в топ-20 | архетип исчез |

## Ключевые сигналы патча 0.5.0

1. **Martial Artist доминирует** — Way of the Stonefist 23%, Hollow Focus Technique 16%. Monk-физика сильна в начале лиги.
2. **Spirit Walker (Huntress) 17%** — новое ascendancy сразу в топ-3. Дикий зверь/спирит-мета.
3. **Comet упал с 27% до 3%** — прямое следствие нерфа. Stormweaver/Blood Mage больше не правят.
4. **Blood Mage 17% → 2%** — Sanguimancy/CoC связка уничтожена. Sanguis Heroum всё ещё 5.1% (переходный период).
5. **Lochtonial Caress 9.5%** — перчатки для Monk/MA-билдов. Новый флаг-предмет патча.
6. **Magnified Area II 69%** — по-прежнему обязательный саппорт.

## Notes

- "0.0%" в weapon config / ascendancy = меньше 0.05%, фактически отсутствует.
- Сырые таблицы (вкл. топ-100 чаров с life/ES/EHP/DPS) — в [[raw/poe-ninja-vaal-2026-05-24]].
- При появлении нового патча создаётся новый файл `raw/poe-ninja-<league>-<date>.md` и строка в таблице выше; этой страницей не переписывать историю.
