---
category: crafting
sources: [raw/fextralife/crafting.md]
patch: 0.4.0
updated: 2026-05-22
---

# Crafting Overview

Крафтинг в Path of Exile 2 — система модификации предметов через [[currency|валюту]]. Ключевое отличие от PoE 1: нет **Orb of Scouring**, поэтому нельзя сбросить [[items/armor|броню]] или [[items/weapons|оружие]] обратно в Normal. Белые (Normal) предметы ценны как чистые основы.

## Редкость предметов

| Редкость | Аффиксы |
|----------|---------|
| Normal (белый) | 0 — чистая основа для крафта |
| Magic (синий) | 1–2 аффикса |
| Rare (жёлтый) | до 6 аффиксов |
| Unique (оранжевый) | фиксированные модификаторы |

## Базовый путь прокачки предмета

```
Normal
  └─ Orb of Transmutation → Magic (1 афф.)
       └─ Orb of Augmentation → Magic (2 афф.)
            └─ Regal Orb → Rare (+1 афф.)
                 └─ Exalted Orb → Rare (до +1 афф., макс. 6)
```

Альтернатива: **Orb of Alchemy** переводит Normal сразу в Rare с 4 аффиксами.

## Валюта крафта

### Основные орбы

| Валюта | Действие |
|--------|---------|
| [[orb-of-transmutation\|Orb of Transmutation]] | Normal → Magic (1 афф.) |
| [[orb-of-augmentation\|Orb of Augmentation]] | добавляет афф. Magic-предмету (если только 1) |
| [[regal-orb\|Regal Orb]] | Magic → Rare (+1 афф., сохраняет существующие) |
| [[orb-of-alchemy\|Orb of Alchemy]] | Normal → Rare (4 афф.) |
| [[exalted-orb\|Exalted Orb]] | добавляет случайный афф. Rare-предмету |
| [[chaos-orb\|Chaos Orb]] | удаляет и заменяет 1 случайный модификатор |
| [[divine-orb\|Divine Orb]] | перерандомизирует числовые значения модификаторов |
| [[orb-of-annulment\|Orb of Annulment]] | удаляет 1 случайный модификатор |
| [[orb-of-chance\|Orb of Chance]] | случайно улучшает Normal-предмет |
| [[artificers-orb\|Artificer's Orb]] | добавляет сокет к предмету |
| [[scroll-of-wisdom\|Scroll of Wisdom]] | идентифицирует предмет |
| [[vaal-orb\|Vaal Orb]] | порча — непредсказуемый результат (см. ниже) |

### Удалённые валюты (нет в PoE 2)

- Orb of Alteration
- Orb of Scouring
- Orb of Fusing
- Chromatic Orb

Линкинг заменён системой [[uncut-gems|Uncut Gems]].

## Качество (Quality)

Качество даёт до +20% к базовым характеристикам. Материалы различаются по типу снаряжения:

| Тип | Материал | Бонус |
|-----|---------|-------|
| Боевое оружие | [[blacksmiths-whetstone\|Blacksmith's Whetstone]] | физ. урон |
| Кастерское оружие | [[arcanists-etcher\|Arcanist's Etcher]] | жезлы, посохи, скиптры |
| Броня | [[armourers-scrap\|Armourer's Scrap]] | броня / уклонение / ES |
| Аксессуары | [[flesh-catalyst\|Flesh Catalyst]] | модификаторы; дроп из [[breach\|Breach]] |

## Сокеты и руны

Тело и двуручное оружие имеют **2 сокета**, остальные слоты — **1 сокет**. В сокеты вставляются [[ezomyte-runes|Ezomyte Runes]] (сопротивления, элем. урон).

[[soul-cores|Soul Cores]] — продвинутый вариант рун с уникальными модификаторами. После установки **нельзя снять или заменить**.

## Эссенции

[[essences|Essences]] (обновлены в The Third Edict):

- **Обычные эссенции**: Normal → Magic с гарантированным модификатором.
- **Greater Essences**: Magic → Rare с конкретным модификатором (аналог Regal Orb).
- **Perfect Essences**: убирают и заменяют модификатор гарантированным (аналог Chaos Orb).

## Омены

[[omens|Omens]] — особые предметы из [[mechanics/atlas-endgame#ritual|Ритуалов]]. Меняют поведение следующей использованной орбы. Применяется только 1 омен за крафт.

Пример: *Omen of Dextral Annulment* — следующий Orb of Annulment снимет только суффикс.

## Порча (Vaal Orb)

[[vaal-orb|Vaal Orb]] — финальный шаг, применяется **после всего крафта**, т.к. после порчи дальнейшие модификации невозможны. Возможные результаты:

- Добавление энчанта поверх implicit.
- Перерандомизация модификаторов.
- Добавление дополнительного сокета.
- Превращение предмета в непригодный.

## Desecrated Modifiers (The Third Edict)

Новая механика из обновления. Через **Well of Souls** (Акт 2) и Ancient Bones из [[abyss|Abyss]] можно выбрать 1 из 3 случайных модификаторов для добавления на предмет — без риска потерять существующие.

## Tiered Currencies (The Third Edict)

Для основных орб появились варианты **Normal / Greater / Perfect**, гарантирующие минимальный тир аффикса (нет риска получить слабый афф.).

## Разборка (Salvaging)

- Разобрать Magic-предмет → фрагменты для [[orb-of-transmutation|Orb of Transmutation]].
- Разобрать Rare-предмет → фрагменты для [[regal-orb|Regal Orb]].
- Качественный предмет → [[armourers-scrap|Armourer's Scrap]] / [[blacksmiths-whetstone|Whetstone]].

## Экономика и Gold

Предметы продаются за **Gold** (не торгуемый между игроками). Gold используется для:

- Покупки у торговцев.
- Гемблинга (случайные предметы).
- Респека пассивных навыков.
- Обмена валюты игрок-игрок (с комиссией в Gold).

## Стратегия раннего старта

- **Normal-база** — лучший старт для крафта (чистый лист).
- **Magic-база** — есть полезные аффиксы, но меньше контроля.
- **Rare-база** — максимальная сила, но дороже модифицировать.

Крафт ориентирован на улучшение найденных в игре предметов, а не крафт с нуля.
