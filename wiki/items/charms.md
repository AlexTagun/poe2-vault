---
category: items
sources: [raw/fextralife/items/charms.md, raw/poe2db/uniques/*.md]
patch: 0.4.0
updated: 2026-05-25
---

# Charms

Charms — экипируемые предметы, дающие автоматические защитные бонусы или иммунитеты при наступлении определённых условий. Экипируются в слоты пояса.

Связанные темы: [[flasks]], [[items/jewellery/belts|jewellery-belts]], [[mechanics/combat|combat]]

## Механика

- **Триггерные**: каждый чарм активируется при выполнении условия (например, при получении урона огнём)
- **Заряды**: ограниченный запас зарядов (обычно 80 макс.), расходуется при активации; пополняется убийством монстров
- **Длительность**: эффект длится 2–4 секунды в зависимости от типа
- **Редкость**: доступны в Normal → Rare, можно крафтить моды

## Слоты чармов

Базово доступен 1 слот чарма. Идол **Maxarius** добавляет +1 Charm Slot. Пояса с модом "Charm Slot" также расширяют количество.

## Полный список чармов

| Название | Эффект | Триггер | Стоимость | Треб. ур. |
|---|---|---|---|---|
| Ruby Charm | +25% Fire Resistance | Получение fire damage от хита | 40/80 | 5 |
| Sapphire Charm | +25% Cold Resistance | Получение cold damage от хита | 40/80 | 5 |
| Topaz Charm | +25% Lightning Resistance | Получение lightning damage от хита | 40/80 | 5 |
| Stone Charm | Нельзя оглушить | Оглушение | 40/80 | 8 |
| Silver Charm | Скорость не замедляется | Попадание под slow | 40/80 | 10 |
| Thawing Charm | Иммунитет к Freeze | Заморозка | 80/80 | 12 |
| Staunching Charm | Иммунитет к Bleeding | Начало кровотечения | 60/80 | 18 |
| Antidote Charm | Иммунитет к Poison | Отравление | 40/80 | 24 |
| Dousing Charm | Иммунитет к Ignite | Поджигание | 60/80 | 32 |
| Grounding Charm | Иммунитет к Shock | Шок | 50/80 | 32 |
| Amethyst Charm | +18% Chaos Resistance | Получение chaos damage от хита | 60/80 | 40 |
| Golden Charm | +20% Item Rarity | Убийство rare/unique врага | 80/80 | 50 |

## Восстановление зарядов

Заряды восполняются убийством монстров. [[omens|Omen of Refreshment]] мгновенно восстанавливает заряды фласков и чармов при достижении Low Life.

## Soul Core взаимодействие

[[items/soul-cores|Soul Core of Opiloti]] (armour slot) даёт +10% Charm Charges gained.

## Уникальные чармы (patch 0.4.0)

Уникальные чармы имеют фиксированные мощные эффекты вместо стандартных иммунитетов. Базовый тип чарма (слот) соответствует обычным чармам.

| Название | База | Треб. уровень | Триггер | Эффект |
|---|---|---|---|---|
| Rite of Passage | Golden Charm | 50 | Убийство Rare/Unique | Персонаж становится Possessed by Azmeri Spirit на 10–20 сек |
| Forsaken Bangle | Amethyst Charm | 40 | Получение Chaos damage | 50% полученного Chaos урона предотвращается и конвертируется в регенерацию Life и Mana |
| Valako's Roar | Topaz Charm | 5 | Получение Lightning damage | Получить Frenzy Charge |
| Breath of the Mountains | Sapphire Charm | 5 | Получение Cold damage | Получить Power Charge |
| Ngamahu's Chosen | Ruby Charm | 5 | Получение Fire damage | Заполнить Rage до максимума |
| The Fall of the Axe | Silver Charm | 10 | Попадание под Slow | Получить [[mechanics/combat|Onslaught]] на 3 сек |
| For Utopia | Stone Charm | 8 | Оглушение | Защищаться с 200% Armour во время оглушения |
| The Black Cat | Grounding Charm | 32 | Шок (Shocked) | Следующий шок на персонаже становится Lightning Unlucky |
| Beira's Anguish | Dousing Charm | 32 | Поджигание (Ignited) | Создаёт Ignited Ground под персонажем, поглощающий 500% Maximum Life |
| Arakaali's Gift | Antidote Charm | 24 | Отравление (Poisoned) | 15–20% Recovery от Mana Flask применяется к Life; 15–20% Recovery от Life Flask применяется к Mana |
| Sanguis Heroum | Staunching Charm | 18 | Кровотечение (Bleeding) | Создаёт [[mechanics/combat|Consecrated Ground]] под персонажем |
| Nascent Hope | Thawing Charm | 12 | Заморозка (Frozen) | Перезарядка [[mechanics/combat|Energy Shield]] начинается немедленно |
