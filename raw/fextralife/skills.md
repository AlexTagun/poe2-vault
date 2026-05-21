---
source_url: https://pathofexile2.wiki.fextralife.com/Skills
clipped: 2026-05-21
patch: 0.4.0
status: raw
note: |
  Clipped через WebFetch несколькими проходами — модель агрессивно резюмирует
  Fextralife, поэтому полный текст недоступен. Получены: общая структура страницы,
  список категорий скиллов, полный список Ammunition и Attack skills, частичные
  списки Buff/Meta/Minion/Spell/Trigger; механика uncut gems, gemcutting, socket
  colors, weapon swap. Списки Warcry и Ascendancy в выдаче отсутствовали —
  нужен повторный заход (см. TODO ниже).
---

# Path of Exile 2 Skills — Fextralife (nav + lists)

## Обзор страницы

Skills в PoE 2 делятся на 2 главные категории:

1. **Skill Gems** — активные скиллы в бою
2. **Passive Skills** — улучшения с пассивного дерева

Персонаж может иметь до **9 активных скиллов**, каждый модифицируется до **5 саппортами**.

Ключевые цитаты:
- "Any class can use any Skill Gem"
- Support gems "provide utility effects rather than direct offensive stats such as damage itself"
- "Skills scale based on character level progression"
- "Each skill has independent advanced settings for targeting and minion control"

## Skill Gems System

### Uncut Gems

> "Uncut Skill Gems must be engraved into a Gem to become usable in the Gemcutting Menu,
> they can be used to create a Skill Gem or to Level an existing gem up to a certain level."

Игрок находит **uncut gems** в локациях, а не готовые скилл-гемы.

Три типа uncut gems:
- **Uncut Skill Gems** — создаёт новый скилл или повышает уровень существующего
- **Uncut Buff Skill Gems** — создаёт buff-скиллы (persistent buffs / резерв Spirit)
- **Uncut Support Gems** — создаёт саппорты

### Gemcutting

> "Gemcutting has its own interface menu where you will be able to craft Gems to get
> new Skills, and then enhance these skills using Support Gems, also crafted in the
> Gemcutting menu, and placed in the Skill Gem Sockets to further modify the effects
> of the skills."

### Skill Gem Sockets

> "Skill Gems can contain up to 5 sockets, but at the moment you first obtain them
> they usually have only 2 or 3, you can upgrade the amount of sockets with Jeweller's Orbs."

Цвета сокетов привязаны к атрибуту:
- **Red** = Strength
- **Blue** = Intelligence
- **Green** = Dexterity

## Weapon Swapping для скиллов

> "In Path of Exile 2, swapping between two weapon sets is quick and effortless."

Скиллы можно прикрепить к конкретному weapon set через "extended description menu"
в Skill Gem tab — при использовании скилла без подходящего оружия игра автоматически
переключит набор.

## Категории скиллов

Страница организует скиллы по категориям:
Ammunition, Attack, Buff, Meta, Minion, Spell, Trigger, Warcry, Ascendancy.

### Ammunition Skills

- Armour Piercing Rounds
- Explosive Shot
- Fragmentation Rounds
- Galvanic Shards
- Glacial Bolt
- High Velocity Rounds
- Ice Shards
- Incendiary Shot
- Molten Blast
- Permafrost Bolts
- Punch
- Rapid Shot
- Stormblast Bolts
- Quarterstaff Strike

### Attack Skills

- Ancestral Warrior Totem
- Armour Breaker
- Artillery Ballista
- Blazing Lance
- Bleeding Concoction
- Blood Hunt
- Boneshatter
- Bow Shot
- Cluster Grenade
- Cross Slash
- Crossbow Shot
- Detonating Arrow
- Disengage
- Elemental Sundering
- Earthquake
- Earthshatter
- Electrocuting Arrow
- Escape Shot
- Explosive Grenade
- Explosive Spear
- Falling Thunder
- Fangs of Frost
- Flame Breath
- Flash Grenade
- Flicker Strike
- Freezing Salvo
- Frozen Locus
- Furious Slam
- Gas Arrow
- Gas Grenade
- Gathering Storm
- Glacial Cascade
- Hailstorm Rounds
- Hammer of the Gods
- Hand of Chayula
- Ice Shot
- Ice Spear
- Ice Strike
- Impale
- Elemental Surge (Attack)
- Killing Palm
- Leap Slam
- Lightning Arrow
- Lightning Rod
- Lightning Spear
- Lunar Assault
- Mace Strike
- Magma Barrier
- Magnetic Salvo
- Maul
- Oil Barrage
- Oil Grenade
- Parry
- Perfect Strike
- Plasma Blast
- Poisonburst Arrow
- Pounce
- Puncture
- Rain of Arrows
- Rake
- Rampage
- Rapid Assault
- Resonating Shield
- Ripwire Ballista
- Rolling Slam
- Sandstorm Swipe
- Shattering Palm
- Shield Charge
- Shield Wall
- Shockburst Rounds
- Shockchain Arrow
- Shockwave Totem
- Siege Cascade
- Siphoning Strike
- Snipe
- Spearfield
- Spear of Solaris
- Spiral Volley
- Staggering Palm
- Stampede
- Storm Spear
- Storm Wave
- Stormcaller Arrow
- Sunder
- Supercharged Slam
- Temper Weapon
- Tempest Bell
- Tempest Flurry
- Thunderous Leap
- Tornado Shot
- Toxic Growth
- Twister
- Vaulting Impact
- Vine Arrow
- Void Illusion
- Volcanic Fissure
- Voltaic Grenade
- Voltaic Mark
- Walking Calamity
- Wave of Frost
- Whirling Assault
- Whirling Slash
- Whirlwind Lance
- Wind Blast
- Wind Serpent's Fury
- Wing Blast

### Buff Skills (partial)

- Align Fate
- Apocalypse
- Archmage

> Замечание Fextralife: Support Gems предоставляют utility-эффекты, а не прямой
> damage stat. Buff-скиллы похожи на постоянные баффы/ауры (резерв [[Spirit]]).

### Meta Skills (partial)

> "Meta Gems are also Skill Gems that can be supported by Support Gems and other Skill gems."

- Ancestral Warrior Totem
- Hand of Chayula
- Magma Barrier
- Pounce

(Список явно неполный — несколько скиллов перекрываются с Attack/Trigger.)

### Minion Skills (partial)

- Pounce

### Spell Skills (partial)

- Apocalypse

### Trigger Skills (partial)

- Magma Barrier
- Pounce
- Temper Weapon
- Walking Calamity
- Apocalypse

### Warcry Skills

TODO: не получен список — нужно повторное извлечение через WebFetch с
прицельным запросом по Warcry.

### Ascendancy Skills (partial)

- Align Fate
- Apocalypse

TODO: полный список Ascendancy-only скиллов.

## TODO для следующего прохода

- Полные списки Warcry, Meta, Minion, Spell, Trigger, Ascendancy
- Описания отдельных категорий (что именно отличает Meta от Trigger)
- Конкретные требования к уровню/атрибутам для гемов
- Механика **gem quality** (упоминалась в hub, но не раскрыта здесь)
- Связь Spirit Skills с Buff Skills — это синонимы или разные категории?
- Источник: [Skills](https://pathofexile2.wiki.fextralife.com/Skills)
