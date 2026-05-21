---
category: skills
sources: [raw/fextralife/skills.md]
patch: 0.4.0
updated: 2026-05-21
---

# Skill Categories

Fextralife группирует активные скиллы (Skill Gems) PoE 2 в 9 тегов:
**Ammunition · Attack · Buff · Meta · Minion · Spell · Trigger · Warcry · Ascendancy**.

> ⚠️ Один скилл может попадать в несколько категорий одновременно. Например,
> *Apocalypse* у Fextralife отмечен и как **Spell**, и как **Buff**, и как
> **Trigger**, и как **Ascendancy**. Это **теги**, а не взаимоисключающие типы.

## Ammunition

Скиллы, требующие boltов/патронов/гранат (crossbow, throw weapons). Связаны с
weapon-specific ammo, обычно требуют перезарядки.

- Armour Piercing Rounds · Explosive Shot · Fragmentation Rounds
- Galvanic Shards · Glacial Bolt · High Velocity Rounds
- Ice Shards · Incendiary Shot · Molten Blast
- Permafrost Bolts · Punch · Rapid Shot
- Stormblast Bolts · Quarterstaff Strike

См. также: [[Crossbow]], [[Quarterstaff]].

## Attack

Самая большая категория — все физ./элементальные удары и выстрелы, скейлящиеся
от оружия. Активирует [[Melee Enhancement|melee enhancement]] для дефолтных атак.

### Slam/Mace (Warrior)

Armour Breaker · Boneshatter · Earthquake · Earthshatter · Furious Slam ·
Hammer of the Gods · Leap Slam · Mace Strike · Maul · Perfect Strike ·
Rolling Slam · Shockwave Totem · Stampede · Sunder · Supercharged Slam ·
Thunderous Leap · Vaulting Impact · Walking Calamity

### Spear (Huntress)

Blazing Lance · Disengage · Elemental Sundering · Explosive Spear · Falling Thunder ·
Lightning Spear · Lunar Assault · Rake · Rapid Assault · Sandstorm Swipe ·
Spearfield · Spear of Solaris · Spiral Volley · Storm Spear · Twister ·
Whirling Slash · Whirlwind Lance · Wind Serpent's Fury · Wing Blast

### Bow (Ranger)

Bow Shot · Detonating Arrow · Electrocuting Arrow · Escape Shot · Gas Arrow ·
Ice Shot · Lightning Arrow · Lightning Rod · Magnetic Salvo · Oil Barrage ·
Poisonburst Arrow · Puncture · Rain of Arrows · Shockchain Arrow · Snipe ·
Stormcaller Arrow · Tornado Shot · Vine Arrow

### Crossbow

Crossbow Shot · Plasma Blast · Shockburst Rounds · Voltaic Mark
(пересекается с Ammunition)

### Quarterstaff (Monk)

Ice Strike · Killing Palm · Tempest Bell · Tempest Flurry · Storm Wave ·
Wave of Frost · Gathering Storm · Flicker Strike · Shattering Palm ·
Siphoning Strike · Staggering Palm

### Spear/Throw mixed

Bleeding Concoction · Cluster Grenade · Explosive Grenade · Flash Grenade ·
Gas Grenade · Oil Grenade · Voltaic Grenade · Toxic Growth

### Прочее / unsorted

Ancestral Warrior Totem · Artillery Ballista · Blood Hunt · Cross Slash ·
Elemental Surge · Fangs of Frost · Flame Breath · Freezing Salvo ·
Frozen Locus · Glacial Cascade · Hailstorm Rounds · Hand of Chayula ·
Ice Spear · Impale · Magma Barrier · Parry · Pounce · Rampage ·
Resonating Shield · Ripwire Ballista · Shield Charge · Shield Wall ·
Siege Cascade · Temper Weapon · Tempest Bell · Volcanic Fissure ·
Whirling Assault · Wind Blast

(Группировка по оружию выше — эвристическая, на основе нейминга/контекста.
Подтверждать каждый скилл по индивидуальной странице.)

## Buff

Скиллы постоянного действия / ауры. Резервируют [[Spirit]]. Создаются из
**Uncut Buff Skill Gem** через [[Gemcutting]].

Известные:
- Align Fate
- Apocalypse
- Archmage

(Полный список — TODO.)

## Meta

> "Meta Gems are also Skill Gems that can be supported by Support Gems and other Skill gems."

Особый класс гемов, которые **триггерят другие скиллы** или модифицируют их
поведение на лету. Принимают и саппорты, и обычные скилл-гемы как «нагрузку».

Известные:
- Ancestral Warrior Totem · Hand of Chayula · Magma Barrier · Pounce

(Аналог PoE 1 CWDT / Cast on Crit / Spell Cascade — но как отдельная категория гемов.)

## Minion

Призывы существ. На странице явно отмечен только:
- Pounce

(Список явно неполный — стандартные миньон-скиллы PoE 2 в выдаче отсутствовали.
TODO: дотянуть.)

## Spell

Заклинания (скейл от модов на spell damage, а не от оружия).

Известные:
- Apocalypse

(Полный список — TODO.)

## Trigger

Скиллы, срабатывающие по условию (on hit, on kill, on stun и т.д.) или
триггеримые из Meta-гемов.

Известные:
- Magma Barrier · Pounce · Temper Weapon · Walking Calamity · Apocalypse

## Warcry

Кричалки [[Warrior]] (и, вероятно, [[Marauder]]).

TODO: список не извлечён из источника — нужен повторный заход.

## Ascendancy

Скиллы, открывающиеся только через прокачку конкретной [[ascendancies|ascendancy]].

Известные:
- Align Fate · Apocalypse

(TODO: распределение по конкретным ascendancy-классам — см. отдельные wiki-страницы ascendancy.)

## TODO

- Получить полные списки Warcry, Spell, Minion, Ascendancy (источник усечён в WebFetch)
- Сопоставить каждый скилл с конкретным [[classes|классом]] / оружием
- Добавить gem level / attribute requirements
- Раскрыть пересечения тегов (например, Apocalypse = Spell+Buff+Trigger+Ascendancy одновременно — что это значит механически?)

## Источники
- [Skills (Fextralife)](https://pathofexile2.wiki.fextralife.com/Skills)
- [[mechanics/skill-system|skill-system]]
