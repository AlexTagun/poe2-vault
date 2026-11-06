---
category: mechanics
sources: [Clippings/PoE 2 Guide Resistances Explained.md]
patch: 0.4.0
updated: 2026-05-26
---

# Resistances

Резисты — базовые защитные статы, снижающие входящий урон соответствующего типа. Доступны всем персонажам через суффиксные моды на экипировке и другие источники.

Связанные темы: [[mechanics/stats-attributes|Stats & Attributes]], [[exposure]], [[curses]], [[mechanics/combat|Combat]], [[items/charms|Charms]]

## Типы резистов

Резист существует для **каждого типа урона кроме Physical**. Physical Damage Reduction — отдельная механика, реализованная через [[armour|Armour]].

| Тип | Сокращение |
|---|---|
| [[fire-resistance\|Fire Resistance]] | Fire Res |
| [[cold-resistance\|Cold Resistance]] | Cold Res |
| [[lightning-resistance\|Lightning Resistance]] | Lightning Res |
| [[chaos-resistance\|Chaos Resistance]] | Chaos Res |

## Cap и расчёт

- **Default cap: 75%** — максимальное снижение урона при стандартных условиях
- **Hard cap: 90%** — абсолютный потолок, поднимается редкими модами на Maximum Resistance (например, Crystalline Resistance)
- Формула простая: при 75% Fire Res и 1000 Fire Damage → получаешь 250 урона

Таблица: урон после вычета резиста из 1000 Fire Damage

| Fire Resistance | Урон получен |
|---|---|
| 75% | 250 |
| 80% | 200 |
| 85% | 150 |
| 90% | 100 |

Каждый дополнительный % Maximum Resistance тем **ценнее**, чем ближе к 90% — переход с 89% на 90% даёт эффективно ~9% less Damage taken.

## Чтение Character Sheet

В панели персонажа резист отображается двумя числами:

- **Первое** — эффективный резист (используется для снижения урона, ограничен cap'ом)
- **Второе (в скобках)** — суммарный некапированный резист

Пример: `75% (114%)` — персонаж имеет эффективную защиту 75%, но 114% суммарного резиста.

Некапированный резист важен при расчёте эффектов, снижающих резист (Exposure, Curses) — он даёт запас прочности.

## Campaign Resistance Penalty

По мере завершения актов кампании **перманентно накапливается штраф** на все элементальные резисты:

- **−10% ко всем Elemental Resistances за каждый завершённый акт**
- Итого после 6 актов: **−60% ко всем Elemental Resistances**
- **Chaos Resistance penalty НЕ получает** — только Fire, Cold, Lightning

Штраф нельзя избежать или снять.

## Campaign Resistance Bonuses

За убийство определённых боссов в кампании выпадают одноразовые предметы, дающие **перманентные бонусы к Elemental Resistances**:

- Суммарно: **+20% ко всем Elemental Resistances** (по +10% к каждому отдельно)
- В Акте 6 есть опциональный бонус к **Chaos Resistance**

Эти бонусы частично компенсируют penalty от прохождения актов.

## Отрицательные резисты (Exposure и Curses)

Эффекты, снижающие резисты, применяются к **некапированному** суммарному значению.

### Exposure

- Дебафф, снижающий конкретный резист на **−20% по умолчанию**
- Можно усилить через модификаторы Exposure Effect (например, Overexposure)

### Curses

- Отдельные [[curses|Curses]] также снижают резисты, например Elemental Weakness
- Величина снижения зависит от уровня Curse Skill Gem и модов на Magnitude of Curses (например, Master of Hexes)

**Пример расчёта**: персонаж с `75% (114%)` Lightning Res → Exposure (−20%) → `75% (94%)` → Elemental Weakness lv1 (−23%) → `54% (54%)`. Эффективная защита упала ниже cap'а.

### Резист ниже 0%

Когда резист уходит в минус — урон **увеличивается** вместо снижения. Монстр с −17% Fire Res берёт 17% **дополнительного** Fire Damage.

Используй некапированный резист с запасом, чтобы Exposure + Curses не пробили cap.

## Resistance Penetration

Penetration позволяет хитам обходить резист цели на указанный процент.

- Пример: 15% Fire Penetration → хиты с Fire Damage обрабатываются так, будто у цели на 15% меньше Fire Res
- **Не может пробить резист ниже 0%** — излишек отбрасывается
- **Применяется только к Hits** — DoT не взаимодействует с Penetration
- Порядок: сначала применяются Exposure/Curses, затем считается Penetration от полученного значения

## Ignoring Resistances

Некоторые механики **полностью игнорируют** значение резиста — урон рассчитывается как если бы резист был **0%**.

Пример: Invoker ascendancy нода «Sunder my Enemies...» — крит-хиты игнорируют Monster Elemental Resistances, если те не были в минусе.

## Honour Resistance

В [[mechanics/bosses|Trial of the Sekhemas]] резисты работают аналогично для **Honour** (особый ресурс испытания). Honour Resistance предоставляется [[items/relics|Relics]] в Relic Altar.

## Взаимодействие с аскендансями

### [[builds/ascendancies/smith-of-kitava|Smith of Kitava]] (Warrior)

- **Coal Stoker**: бонусы к Fire Resistance применяются также к Cold и Lightning Resistance в **половинном размере**. Работает и для негативных резистов!
- **Forged in Flame**: бонусы к **Maximum** Fire Resistance применяются к Maximum Cold и Lightning Resistance. Позволяет скейлить все Maximum Elemental Res через инвестиции только в Fire.

### [[builds/ascendancies/gemling-legionnaire|Gemling Legionnaire]] (Mercenary)

- **Thaumaturgical Infusion**: получает большой бонус к Maximum Elemental Resistances в зависимости от цветов Support Gems в скиллах.

### [[builds/ascendancies/acolyte-of-chayula|Acolyte of Chayula]] (Monk)

- **Chayula's Gift**: огромный бонус к Maximum Chaos Resistance + **удвоение Chaos Resistance** (динамически).
- Удвоение работает **динамически** — Curses вроде Despair (−Chaos Res) применяются до удвоения, что делает их особенно опасными.
- Пример: 43% base Chaos Res → 85% после удвоения. Despair −18% → 25% → 50% после удвоения.

---

## Связанные страницы

- [[damage-calculation]] — где резисты/пенетрация/инверсия стоят в порядке расчёта урона (шаг Mitigation)
