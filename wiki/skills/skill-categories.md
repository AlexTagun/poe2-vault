---
category: skills
sources:
  - raw/Clippings/Skills.md
  - raw/Clippings/skills/*.md
patch: 0.4.0
updated: 2026-05-22
---

# Skill Categories

Fextralife группирует все активные скиллы (Skill Gems) и связанные ascendancy-эффекты PoE 2 в 9 категорий:
**Ammunition · Attack · Buff · Meta · Minion · Spell · Trigger · Warcry · Ascendancy**.

> ⚠️ **Категории — это теги, не взаимоисключающие типы.** Один скилл может попадать
> в несколько разделов (например, *Bone Offering* — и Minion, и Spell; *Voltaic
> Mark* — и Attack, и Spell). Это нормально: тег описывает аспект, а не класс гема.

> ⚠️ **Ascendancy "skills" — это в основном пассивные ноды/нотейблы**, многие из
> которых грантят активные скиллы из других категорий. См. соответствующий раздел.

Полные эффекты по каждому скиллу — в [raw/Clippings/Skills.md](../../raw/Clippings/Skills.md).
Таблица с T1 саппортами и требованиями по оружию — [[skills/skill-reference|skill-reference]].

## Сводка

| Категория | Кол-во | Что это |
|---|---|---|
| [Ammunition](#ammunition) | 14 | Скиллы с боеприпасами (crossbow, throw) |
| [Attack](#attack) | ~100 | Удары/выстрелы, скейл от оружия |
| [Buff](#buff) | 50 | Auras / persistent buffs / heralds, резерв [[Spirit]] |
| [Meta](#meta) | 3 | Гемы-обёртки, триггерят другие скиллы |
| [Minion](#minion) | 16 | Призывы, offerings, mounts |
| [Spell](#spell) | ~80 | Заклинания, скейл от spell damage |
| [Trigger](#trigger) | 2 | Триггер-гемы (Cast on X) |
| [Warcry](#warcry) | 4 | Кричалки [[Warrior]] |
| [Ascendancy](#ascendancy) | ~180 | Нотейблы ascendancy + грантованные скиллы |

## Ammunition

Скиллы с системой clip/reload — boltы (crossbow) или throw-патроны. Знак "+N Bolts
loaded per clip" — характерный маркер.

- [[Armour Piercing Rounds]] — knockback, anti-armour
- [[Explosive Shot]] — 30% phys→fire conversion, knockback
- [[Fragmentation Rounds]] — pierce 2, freeze consume on hit
- [[Galvanic Shards]] — phys→lightning, beam chain
- [[Glacial Bolt]] — phys→cold, ice wall
- [[High Velocity Rounds]] — pierce 6, riven armour proc
- [[Ice Shards]] — 16 shards/clip, chill amp
- [[Incendiary Shot]] — phys→fire, flammability magnitude
- [[Molten Blast]] — fire shrapnel, dual-wield bonus
- [[Permafrost Bolts]] — phys→cold, freeze buildup
- [[Punch]] — fallback melee для crossbow
- [[Rapid Shot]] — 100 bolts/clip, heat overload
- [[Stormblast Bolts]] — phys→lightning, charged bolts
- [[Quarterstaff Strike]] — fallback melee для quarterstaff

## Attack

Самая большая категория — физ./элементальные удары/выстрелы, скейл от оружия.
Группировка ниже эвристическая (по оружию/архетипу).

### Slam / Mace (Warrior)

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

### Crossbow / Ammo-Attack (overlap)

Crossbow Shot · Plasma Blast · Shockburst Rounds · Voltaic Mark ·
Explosive Shot · Hailstorm Rounds · Siege Cascade · Voltaic Grenade

### Quarterstaff (Monk)

Ice Strike · Killing Palm · Tempest Bell · Tempest Flurry · Storm Wave ·
Wave of Frost · Gathering Storm · Flicker Strike · Shattering Palm ·
Siphoning Strike · Staggering Palm

### Grenades / Throw

Bleeding Concoction · Cluster Grenade · Explosive Grenade · Flash Grenade ·
Gas Grenade · Oil Grenade · Toxic Growth

### Totems / Ballistas

Ancestral Warrior Totem · Artillery Ballista · Ripwire Ballista · Shockwave Totem

### Shield / Block

Magma Barrier · Parry · Resonating Shield · Shield Charge · Shield Wall

### Прочее / unsorted

Blood Hunt · Cross Slash · Elemental Surge (Attack) · Fangs of Frost ·
Flame Breath · Freezing Salvo · Frozen Locus · Glacial Cascade ·
Hand of Chayula · Ice Spear · Impale · Rampage · Temper Weapon ·
Volcanic Fissure · Void Illusion · Whirling Assault · Wind Blast

## Buff

Persistent buffs, auras, heralds, mark-скиллы, triggers, banners. Большинство
резервирует [[Spirit]]. Создаются из **Uncut Buff Skill Gem** через [[Gemcutting]].

### Auras / Heralds / Banners

- [[Arctic Armour]] — cold damage aura, 3 stages
- [[Berserk]] — rage effect amp
- [[Defiance Banner]] · [[Dread Banner]] · [[War Banner]] — banner auras (Glory cost)
- [[Discipline]] — share max mana → ally ES
- [[Heart of Ice]] — chill enemies in presence
- [[Herald of Ice]] · [[Herald of Plague]] · [[Herald of Thunder]] — on-kill heralds
- [[Malice]] — apply Critical Weakness
- [[Overwhelming Presence]] — ailment/stun threshold reduce in presence
- [[Plague Bearer]] — store poison damage
- [[Purity of Fire]] · [[Purity of Ice]] · [[Purity of Lightning]] — ally resistances
- [[Time of Need]] — periodic heal + cleanse
- [[Withering Presence]] — apply Wither in presence

### Cast-on Trigger Buffs (energy-based)

- [[Cast on Block]]
- [[Cast on Critical]]
- [[Cast on Death]]
- [[Cast on Elemental Ailment]]
- [[Cast on Freeze]]
- [[Cast on Ignite]]
- [[Fire Spell on Hit]]
- [[Elemental Invocation]]
- [[Barrier Invocation]]

### Charges / Resources

- [[Align Fate]] — visage timing buff (Ascendancy: Tactician)
- [[Apocalypse]] — Glory-cost meta buff (3 disasters)
- [[Archmage]] — non-channelling spells gain lightning per max mana
- [[Combat Frenzy]] — frenzy charge on ailment
- [[Trinity]] — resonance, multi-elem damage
- [[Unbound Avatar]] — Unbound Fury → unbound state

### Состояния / прочее

- [[Blink]] — teleport with cooldown
- [[Blood Boil]] — corrupted blood spread
- [[Emergency Reload]] — buff bolts after reload
- [[Grim Feast]] — Grim Remnants → ES recovery
- [[Into the Breach]] — Flames of Chayula manifestation
- [[Lingering Illusion]] — illusions with % of life
- [[Mana Remnants]] — drop mana remnants on kill
- [[Mantra of Destruction]] — empower next melee (Combo cost)
- [[Raging Spirits]] — fire spirits from fire skills
- [[Ritual Sacrifice]] — steal modifier from monster
- [[Scavenged Plating]] — stacks armour buff
- [[Sorcery Ward]] — elemental barrier

## Meta

> "Meta Gems are also Skill Gems that can be supported by Support Gems and other
> Skill gems."

Только **3 явных Meta-гема**:
- [[Cast on Melee Stun]] — energy from heavy stuns
- [[Cast on Shock]] — energy from shocks
- [[Mirage Deadeye (Meta Skill)]] — projectile mirror (ascendancy-связан)

Многие cast-on эффекты в категории Buff (см. выше) тоже фактически meta — у
Fextralife разделение нечёткое.

## Minion

Призывы, offerings, mounts.

### Offerings (бафф/деф от corpses)

- [[Bone Offering]] — shield spike, hit absorb
- [[Pain Offering]] — minion attack/cast speed aura
- [[Power Offering]] — power spike
- [[Soul Offering]] — spell damage buff
- [[Bind Spectre]] — bind enemy soul

### Summons

- [[Manifest Weapon]] — animated weapon (mace/quarterstaff/spear behaviour)
- [[Raise Zombie]] — limit 10 zombies
- [[Rhoa Mount]] — mount, +movement
- [[Skeletal Arsonist]] — fire explosive demise
- [[Skeletal Brute]] — melee shockwave
- [[Skeletal Cleric]] — revive + heal
- [[Skeletal Frost Mage]] — ice bomb
- [[Skeletal Reaver]] — life-loss demon (rage on hit)
- [[Skeletal Sniper]] — gas arrow + poison cloud
- [[Skeletal Storm Mage]] — lightning bolt + shocked ground
- [[Skeletal Warrior]] — basic melee + elem resistance
- [[Supporting Fire]] — death-from-above command

## Spell

Заклинания. Скейл от spell damage / cast speed, не от оружия.

### Lightning

Arc · Ball Lightning · Galvanic Field · Lightning Bolt · Lightning Conduit ·
Lightning Storm · Lightning Warp · Mana Tempest · Orb of Storms · Spark ·
Thunder Storm · Voltaic Mark · Sigil of Power

### Cold

Comet · Eye of Winter · Freezing Mark · Freezing Shards · Frost Bomb ·
Frost Wall · Frostbolt · Ice Nova · Lunar Blessing · Snap

### Fire

Ember Fusillade · Fireball · Firebolt · Firestorm · Flame Wall · Flameblast ·
Flammability · Incinerate · Living Bomb · Rolling Magma · Solar Orb ·
Volatile Dead · Volcano

### Physical

Bone Blast · Bone Cage · Bone Offering · Bonestorm · Detonate Dead ·
Entangle · Exsanguinate · Moment of Vulnerability · Power Siphon · Reap ·
Thrashing Vines · Tornado · Unearth · Raise Shield

### Chaos / Poison / Curses (debuffs)

Chaos Bolt · Contagion · Dark Effigy · Decompose · Despair · Essence Drain ·
Hexblast · Profane Ritual · Soulrend · Wither · Conductivity ·
Elemental Weakness · Enfeeble · Hypothermia · Inevitable Agony · Sniper's Mark ·
Temporal Chains · Vulnerability · Charged Staff · Consecrate · Summon Wolf

### Marks

[[Freezing Mark]] · [[Sniper's Mark]] · [[Voltaic Mark]] — single-target debuffs с
cap'ом 1 marked target.

## Trigger

Энергонакопительные гемы, триггерящие сокетированные spells.

- [[Cast on Melee Kill]] — 300 energy on melee kill
- [[Cast while Channelling]] — 60 energy/sec channelling

(Cast on Block/Crit/Death/Ailment/Freeze/Ignite формально в Buff, но
функционально trigger.)

## Warcry

Кричалки Warrior — все требуют enemies в радиусе и empower-ят атаки.

- [[Arctic Howl]] — cold warcry, ally cold damage buff
- [[Ferocious Roar]] — armour break empower (Strength scaling)
- [[Infernal Cry]] — fire empower + Combust corpse explosion
- [[Seismic Cry]] — slam empower + knockback

## Ascendancy

> ⚠️ В Fextralife это **смешанный раздел**: notable passives ascendancy + скиллы,
> которые они грантят. Примерно 180 записей.

### Grants Skill: ... (нотейбл даёт активный скилл)

Notables, явно начинающиеся с "Grants Skill":

- [[Against the Anvil]] → [[Temper Weapon]]
- [[Bringer of the Apocalypse]] → [[Apocalypse]]
- [[Heat of the Forge]] → [[Fire Spell on Hit]]
- [[Fateful Vision]] → [[Align Fate]]
- [[Illusory Void]] → [[Void Illusion]]
- [[Inevitability]] → [[Inevitable Agony]]
- [[Jade Heritage]] → [[Encase in Jade]]
- [[Living Weapon]] → [[Manifest Weapon]]
- [[Loyal Hellhound]] → [[Summon Infernal Hound]]
- [[Sanguimancy]] → [[Life Remnants]]
- [[Demonic Possession]] → [[Demon Form]]
- [[Converging Paths]] → [[Moment of Vulnerability]]
- [[Corrupted Lifeforce]] → [[Blood Boil]]
- [[Obsessive Rituals]] → [[Sorcery Ward]]
- [[Mirage Deadeye (Notable)|Mirage Deadeye]] → [[Mirage Deadeye (Meta Skill)]]
- [[Unleash Hell!]] → [[Supporting Fire]]
- [[Footprints in the Sand]] → [[Temporal Rift]]
- [[Faith is a Choice]] → [[Meditate]]
- [[And I Shall Rage]] → [[Unbound Avatar]]
- [[Answered Call]] → [[Ancestral Spirits]]
- [[Ultimate Command]] → [[Time Freeze]]
- [[Unbound Encore]] → [[Time Snap]]
- [[Waking Dream]] → [[Into the Breach]]
- [[As the Whispers Ask]] → [[Ritual Sacrifice]]
- [[Tempest Caller]] → [[Elemental Storm]]
- [[And Scatter them to the Winds]] → [[Elemental Expression]]
- [[Brew Concoction]] → 5 concoction skills (Bleeding/Explosive/Shattering/Fulminating/Poisonous)
- [[Bleeding Concoction (notable)|Bleeding Concoction]] → [[Bleeding Concoction]]
- [[Explosive Concoction (notable)|Explosive Concoction]] → [[Explosive Concoction]]
- [[Shattering Concoction (notable)|Shattering Concoction]] → [[Shattering Concoction]]
- [[Fulminating Concoction (notable)|Fulminating Concoction]] → [[Fulminating Concoction]]
- [[Acidic Concoction]] → [[Poisonous Concoction]]
- [[Called Shots]] → [[Called Shots (Meta Skill)]]
- [[Elemental Surge (notable)|Elemental Surge]] → [[Elemental Surge (Attack)]]
- [[Projectile Proximity Specialisation]] → [[Point Blank]] + [[Far Shot]]

### Прочие notables (без грантования скилла)

~140 пассивных нотейблов: модифицируют статы, добавляют механики, открывают
keystones. Полный список в [raw/Clippings/Skills.md](../../raw/Clippings/Skills.md)
(секция "All Ascendancy Skills"). Примеры архетипов:

- **Defensive**: Stone Skin · Stalking Panther · Heatproofing · Leather Bindings ·
  Tantalum Alloy · Support Straps · Spiked Plates · Crimson Power · Beidat's Gaze/Hand/Will
- **Offensive scaling**: Critical Strike · Forced Outcome · Crushing Impacts ·
  Predatory Instinct · No Mercy · Penetrate · Judge Jury and Executioner
- **Ailment ramp**: Shaper of Storms · Shaper of Winter · Bringer of Flame ·
  Strike Twice · Heavy Snows
- **Charge synergy**: Avidity · Thrilling Chase · Price of Power ·
  Advanced Thaumaturgy · Surging Avatar
- **Skill/build keystones**: Pyromantic Pact · Embrace the Darkness ·
  Sanguine Tides · Weapon Master · The Unseen Path · Soulless Form
- **Curse/banner amp**: Incessant Cacophony · Whoever Pays Best · Warcaller's Bellow
- **Totem/minion**: Cannons Ready! · Unnamed Heartwood · Strategic Embankments ·
  Wooden Wall
- **Flask/charm**: Connected Chemistry · Enduring Elixirs · Azmeri Brew ·
  Intricate Sigils · Mind Phylacteries · Sacred Flow
- **Body Armour-зависимые**: Kitavan Engraving · Kitavan Imprint · Tribute to Utula ·
  Internal Layer · Heatproofing · Spiked Plates · Smith's Masterwork ·
  Molten Symbol · Flowing Metal · Dedication to Kitava

(Распределение по конкретным ascendancy — см. [[builds/ascendancies|ascendancies]];
здесь только перечисление.)

## Связанные ссылки

- [[mechanics/skill-system|skill-system]] — механика гемов и сокетов
- [[builds/ascendancies|ascendancies]] — ascendancy-классы и их notable trees
- [[Spirit]] — резервация под persistent buffs
- Полный raw с эффектами по каждому скиллу: [raw/Clippings/Skills.md](../../raw/Clippings/Skills.md)
