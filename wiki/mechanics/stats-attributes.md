---
category: mechanics
sources: [raw/fextralife/stats-attributes.md]
patch: 0.4.0
updated: 2026-05-21
---

# Stats & Attributes

Числовые основы персонажа: три ядерных атрибута, защитные и наступательные статы, резисты, бонусы по актам.

## Ядерные атрибуты

Три первичных атрибута. **Сами по себе урон не дают** — только статы и доступ к экипировке/скиллам.

| Атрибут          | Бонус за 1 очко       | Открывает                                                     |
|------------------|-----------------------|---------------------------------------------------------------|
| **Strength**     | +2 [[Life]]           | [[Armour]]-экипировку, melee-оружие и скиллы                  |
| **Dexterity**    | +5 [[Accuracy Rating]] | [[Evasion Rating|Evasion]]-экипировку, дальнобойное оружие/скиллы |
| **Intelligence** | +2 [[Mana]]           | [[Energy Shield]]-экипировку, спелл-оружие и скиллы           |

> Damage от атрибутов **не идёт автоматически**. Если скилл/passive скейлится от STR/DEX/INT — это указано явно.

### Hybrid-классы

Гибридные классы используют комбинации (см. [[classes|Список классов]] и таблицу ниже). Гибридная экипировка (STR-DEX, STR-INT, DEX-INT) даёт обе соответствующие защиты.

## Защитные статы

- **[[Life]]** — здоровье. Смерть при 0.
- **[[Energy Shield]]** (ES) — поглощает урон до Life. Быстро восстанавливается, если давно не били. **Chaos** снимает ES в **2× объёме**. [[Bleeding]] и [[Poison]] игнорируют ES и бьют прямо по Life.
- **[[Mana]]** — ресурс большинства скиллов. Медленно регенерирует.
- **[[Spirit]]** — резервируется persistent-скиллами (auras, buffs, миньоны). Подробнее: [[combat#Spirit (ресурс)|Spirit в combat]].
- **[[Armour]]** — снижает **физический** урон от attacks и spells. Cap снижения — **90%**. Против других типов урона не работает.
- **[[Evasion Rating|Evasion]]** — шанс полностью увернуться от strikes и projectiles. Проверка: Accuracy атакующего против Evasion жертвы.
- **[[Block]]** — шанс заблокировать strike/projectile. Часть «крупных» вражеских атак заблокировать нельзя.

## Резисты

Четыре резиста. **Cap по умолчанию — 75%**, поднимается до **90%**. Отрицательные значения **увеличивают** получаемый урон. По мере прогресса кампании резисты режутся (penalty).

- **[[Fire Resistance]]**
- **[[Cold Resistance]]**
- **[[Lightning Resistance]]**
- **[[Chaos Resistance]]**

## Базовые атрибуты классов

Источник перечисляет 8 из заявленных 12 классов. См. полный список в [[classes]].

| Класс         | STR | INT | DEX | Профиль                |
|---------------|-----|-----|-----|------------------------|
| [[Warrior]]   | ✔   |     |     | чистый STR             |
| [[Ranger]]    |     |     | ✔   | чистый DEX             |
| [[Huntress]]  |     |     | ✔   | чистый DEX             |
| [[Sorceress]] |     | ✔   |     | чистый INT             |
| [[Witch]]     |     | ✔   |     | чистый INT             |
| [[Mercenary]] | ✔   |     | ✔   | STR-DEX                |
| [[Monk]]      |     | ✔   | ✔   | INT-DEX                |
| [[Druid]]     | ✔   | ✔   |     | STR-INT                |

## Permanent upgrades (кампания)

Награды актов кампании — **перманентные** бонусы, остаются после респека.

### Act 1
- +4 Passive Skill points
- +10% [[Cold Resistance]]
- +30 max [[Spirit]]
- +20 max [[Life]]
- Доступ к Salvaging Bench (см. [[crafting]])

### Act 2
- +4 Passive Skill points
- +10% [[Lightning Resistance]]
- Выбор: **+30% Charm charges** ИЛИ **+15% Mana Recovery from Flasks**

## Экипировка по типу атрибута

| База экипировки    | Даёт                       |
|--------------------|----------------------------|
| Strength           | [[Armour]]                 |
| Dexterity          | [[Evasion Rating|Evasion]] |
| Intelligence       | [[Energy Shield]]          |
| STR-DEX (hybrid)   | Armour + Evasion           |
| STR-INT (hybrid)   | Armour + ES                |
| DEX-INT (hybrid)   | Evasion + ES               |

Предмет нельзя надеть, если не хватает соответствующих атрибутов.

## Бижутерия с атрибутами

Перечислены амулеты и кольца, которые конкретно скейлят атрибуты.

| Предмет             | Бонус                                            | Lvl |
|---------------------|--------------------------------------------------|-----|
| Amber Amulet        | +(10-15) STR                                     | 8   |
| Jade Amulet         | +(10-15) DEX                                     | 8   |
| Lapis Amulet        | +(10-15) INT                                     | 8   |
| Golden Hoop         | +(8-12) all attributes                           | 12  |
| Stellar Amulet      | +(5-7) all attributes                            | 25  |
| **Astramentis** (U) | +(5-7) all + flat +(80-100) all                  | 24  |
| **Eye of Chayula** (U) | +(10-15) all attributes                       | 35  |
| **Serpent's Egg** (U)  | +(10-20) all attributes                       | 35  |

(U = unique. См. [[unique-jewellery]] — TODO.)

## Skill tags

Метки на скиллах и саппортах, определяющие, как они взаимодействуют. Полный список — [[skill-tags]] (TODO, пока живёт в этом raw'е).

Краткая выжимка тэгов из источника:

- **Ailment**, **Buff**, **Curse**, **Mark** — статусные эффекты (свои/чужие)
- **AoE**, **Projectile**, **Chaining** (6м projectiles / 4м прочее), **Slam**, **Strike** — геометрия
- **Channeling**, **Duration**, **Trigger** — тайминг
- **Ammunition** — патроны для арбалета
- **Totem** — стационарные миньоны
- **Life Leech** — leech-механика (см. [[leech]])
- **Physical** — урон-тэг

## Терминология (общая)

Краткие сокращения, используемые в гайдах. См. [[glossary]] для расширенного списка.

- **AoE** — Area of Effect
- **Buff / Debuff** — позитивный / негативный эффект
- **CC** — Crowd Control
- **CD** — Cooldown
- **Crit** — критический удар
- **DoT** — Damage over Time
- **DPS** — Damage Per Second
- **Proc** — срабатывание условного триггера

## Связанные страницы

- [[character|Character hub]]
- [[combat|Combat basics]]
- [[classes|Классы]]
- [[skill-system|Skill System]]
- [[ailments]]
- [[defenses]] (TODO)
