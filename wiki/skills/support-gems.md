---
category: skills
sources: [raw/Clippings/Support Gems.md, raw/Clippings/support-gems/*.md]
patch: 0.4.0
updated: 2026-05-22
---

# Support Gems

Support Gems модифицируют [[skill-gems|Skill Gems]], усиливая или изменяя их поведение. Они не дают активных способностей сами по себе — только усиливают другие скиллы.

## Система поддержки

- Support Gem вставляется в **Support Gem Socket** (синий кружок) рядом с целевым Skill Gem
- Каждый Support Gem требует **+5 STR**, **+5 DEX** или **+5 INT** для установки
- Support Gems не имеют своего уровня — их эффективность задаётся **тиром** (для обычных) или фиксирована (для Lineage)
- Большинство Support Gems имеют **Cost Multiplier**, увеличивающий стоимость поддерживаемого скилла

## Два типа Support Gems

### Обычные (Standard) Support Gems

- Тиры **1–5**: более высокий тир = более высокие значения характеристик
- Высокие тиры могут добавлять **дополнительные эффекты**, недоступные на низких
- Крафтятся через **Engraving an Uncut Support Skill Gem** нужного тира
- Организованы по атрибуту (STR/DEX/INT) и уровню (1/2/3)

### Lineage Support Gems

- Названы в честь персонажей лора PoE
- Требуют **Level 65** (за исключением нескольких: Amanamu's Tithe, Kulemak's Dominion, Kurgal's Leash — требуют Level 25)
- Уникальные взаимодействия, которых нет у обычных гемов
- Большинство **выпадают только из контента эндгейма** (Pinnacle Bosses, Breach, etc.)
- Исключение: **[[Cirel's Cultivation]]** — крафтится из Uncut Support Skill Gem
- Имеют тэг **Lineage** и часто дополнительный тэг категории

## Патч 0.3.0 — The Third Edict (Ключевые изменения)

- Удалено ограничение «один гем на персонажа» для всех Support Gems (включая Lineage)
- Введена **тир-система** для обычных гемов (ранее были просто уровни)
- Добавлены Lineage Gems — первая группа: Breachlord-семейство (Uul-Netol's Embrace, Esh's Radiance, Tul's Stillness, Xoph's Pyre) и другие
- Смержены некоторые дублирующиеся гемы

## Патч 0.4.0 — Last of the Druids

Добавлены 10 новых Lineage Gems:
- Cirel's Cultivation, Morgana's Tempest, Dreamer's Knell, Oisin's Oath, Tasalio's Rhythm, Xibaqua's Rending, Helbrym's Hide, Ailith's Chimes, Arjun's Medal, Khatal's Rejuvenation

---

## Lineage Support Gems (полный список)

| Гем | Кат. | Тэги | Req | Support Req | Эффект |
|-----|------|------|-----|-------------|--------|
| Ahn's Citadel | Fortress | Lineage | 65 | +5 INT | Стены из скилла создаются вдоль Fissure; −30% AoE, −30% Hit damage |
| Ailith's Chimes | — | Lineage | 65 | +5 DEX | 10% шанс получить Power Charge за каждую единицу Combo при трате Combo |
| Amanamu's Tithe | — | Lineage, Minion, Persistent | **25** | +5 STR | 50% шанс получить Abyssal Monster Modifier при гибели миньона (макс. 3) |
| Arakaali's Lust | — | Lineage | 65 | +5 DEX | +6% more Hit Damage за каждый Poison на цели, до 30% |
| Arbiter's Ignition | — | Lineage, Spell, Fire | 65 | +5 INT | 20% шанс получить Flame Archon при поджоге врага |
| Arjun's Medal | Ammo Conservation | Lineage, Ammunition, Projectile | 65 | +5 DEX | 35% шанс зарядить болт во все Crossbow Ammo при убийстве |
| Atalui's Bloodletting | Lifetap | Lineage, Physical | 65 | +5 STR | Стоимость маны → стоимость жизни; +2% урона как Physical за каждые 10 Life cost |
| Atziri's Allure | — | Lineage, Curse | 65 | +5 INT | Проклятия игнорируют лимит, но отражаются на вас; −25% Curse Effect |
| Atziri's Call | — | Lineage, Spell, AoE, Trigger | 65 | +5 INT | Крит по поддерживаемому Spell → Trigger Atziri's Storm у ближайшего врага |
| Brutus' Brain | Meat Shield | Lineage, Minion | 65 | +5 STR | Миньоны не получают и не наносят урон |
| Cirel's Cultivation | Totemic Control | Lineage, Totem | 65 | +5 STR | 1 активный Totem; +5% AoE и +10% damage за каждый союзный Totem в 4м; реген 1% Life/сек за Totem; до 5 Totem *(крафтится!)* |
| Daresso's Passion | — | Banner, Lineage | 65 | +5 STR | −50% Glory для использования Banner Skills |
| Dialla's Desire | — | Lineage | 65 | +5 INT | +1 к уровню поддерживаемых Skill Gems; +10% Quality |
| Doedre's Undoing | Cursed Ground | Lineage, Spell, AoE, Chaos, Curse, Hazard | 65 | +5 INT | Cursed Ground как Hazard, взрывается при входе врага; макс. 2 зоны |
| Dreamer's Knell | — | Lineage, Attack, AoE, Melee, Trigger, Duration | 65 | +5 DEX | Создаёт Bell за каждые 2 Combo при трате Combo; 40% Attack Damage |
| Einhar's Beastrite | Behead | Lineage, Attack, Melee, Strike | 65 | +5 STR | Уничтожает только Low Life врагов; убийство Rare → 2 их модификатора на 40 сек |
| Esh's Radiance | Breachlord | Lineage | 65 | +5 INT | +20% Lightning Damage as Extra Chaos; Chaos Hits также учитываются для Shock |
| Garukhan's Resolve | Hit and Run | Lineage, Attack, Conditional | 65 | +5 DEX | Активен только после перемещения на 20м; Bifurcate [[mechanics/critical-hits|Critical Hit Chance]] |
| Helbrym's Hide | — | Lineage, Shapeshift, Buff | 65 | +5 STR | Shapeshift → бафф, накапливающий полученный урон → Guard + Rage при истечении |
| Ixchel's Torment | Fluke | Lineage, Trigger | 65 | +5 INT | Триггерные скиллы получают случайный ±40–60% Damage, ±40–50% AoE/ProjSpeed, 0–20% Refund cost |
| Kalisa's Crescendo | — | Lineage | 65 | +5 INT | Враги Pacified в последние 30% длительности проклятия; повторная Pacify через 8 сек |
| Kaom's Madness | Fissures | Lineage, Attack, Melee | 65 | +5 STR | +3 дополнительных Fissure; −20% Attack Speed; −40% Damage; −30% AoE |
| Khatal's Rejuvenation | — | Lineage, Remnant | 65 | +5 INT | Подбор Remnants из поддерживаемых скиллов даёт Khatal's Rejuvenation |
| Kulemak's Dominion | — | Lineage | **25** | +5 INT | Спеллы, затрагивающие область вокруг вас, также работают у Offerings; −50% Damage в зонах Offering |
| Kurgal's Leash | Blackblood | Lineage | **25** | +5 INT | Command Minion → и вы и миньон получают Unholy Might на 5 сек |
| Morgana's Tempest | Advancing Storm | Lineage, Spell, Storm | 65 | +5 INT | Storm Skills: +1 к лимиту, +60% скорость движения Storm, −25% AoE, −35% Damage; Storm исходит от игрока |
| Oisin's Oath | Mana Leech | Lineage, Spell | 65 | +5 INT | Mana Leech восстанавливается по Elemental Damage вместо Physical |
| Paquate's Pact | Corrupting Cry | Lineage, Warcry, Physical, Duration | 65 | +5 STR | Warcry → 5 стаков Corrupted Blood (25% STR как Physical DPS, 5 сек); −2% Max Life за каждый стак |
| Piety's Mercy | — | Lineage | 65 | +5 DEX | Поддерживаемые Hits не убивают врагов |
| Rakiata's Flow | — | Lineage | 65 | +5 DEX | Hits инвертируют Elemental Resistance врагов |
| Ratha's Assault | Double Barrel | Lineage, Ammunition, Projectile | 65 | +5 DEX | Нельзя перезаряжаться обычно; +3 болта при Dodge; +3 дополнительных болта |
| Rigwald's Ferocity | — | Lineage, Attack | 65 | +5 DEX | Set I: +20% Attack Speed, −15% Damage; Set II: −10% Attack Speed, +30% Damage |
| Romira's Requital | Loyalty | Lineage, Minion | 65 | +5 INT | 10% Hit Damage переходит на Companion вместо вас; вы Recoup 200% этого урона как Life; −30% Max Life миньонов |
| Sione's Temper | — | Lineage, Spell, Projectile | 65 | +5 INT | Накапливает Wildshards (1 за каст); 20% × Wildshards шанс выпустить 8 доп. Projectile по кругу (теряет все заряды) |
| Tacati's Ire | — | Lineage, Chaos | 65 | +5 DEX | Poisons наносят урон на 1% быстрее за каждую единицу Rage |
| Tasalio's Rhythm | Perfection | Lineage | 65 | +5 DEX | Perfect Timing → стак (макс. 5): +10% Damage и −30% окно Perfect Timing за стак; любой промах сбрасывает все стаки |
| Tawhoa's Tending | Hardy Totems | Lineage, Totem, AoE, Physical | 65 | +5 STR | Totems +50% Max Life; при гибели — Physical Damage взрыв (Tawhoa's Vengeance) |
| Tecrod's Revenge | Last Gasp | Lineage, Minion, Persistent, Duration | 65 | +5 INT | При смерти миньон живёт ещё 10 сек с Soul Eater и +20% Attack/Cast Speed |
| Tul's Stillness | Breachlord | Lineage | 65 | +5 DEX | +20% Cold Damage as Extra Chaos; Chaos Hits также учитываются для Freeze Buildup |
| Uhtred's Augury | Uhtred of Kalguur | Lineage | 65 | +5 STR | +3 к уровню поддерживаемых скиллов, если ровно 2 других Support |
| Uhtred's Exodus | Uhtred of Kalguur | Lineage | 65 | +5 STR | +3 к уровню поддерживаемых скиллов, если нет других Support |
| Uhtred's Omen | Uhtred of Kalguur | Lineage | 65 | +5 STR | +3 к уровню поддерживаемых скиллов, если ровно 1 другой Support |
| Uruk's Smelting | Armour Demolisher | Lineage, Spell | 65 | +5 STR | Break 70% more Armour; Fully Break → +2% Physical Damage taken permanently (до 20%) |
| Uul-Netol's Embrace | Breachlord | Lineage | 65 | +5 STR | +20% Physical Damage as Extra Chaos; Break Armour = 20% Chaos Damage dealt |
| Varashta's Blessing | — | Lineage | 65 | +5 INT | +10% more Damage за каждый разный Command Skill за последние 8 сек |
| Vilenta's Propulsion | — | Lineage, Spell, Projectile | 65 | +5 INT | 50% изменений Cast Speed также применяются к Projectile Speed |
| Xibaqua's Rending | — | Lineage, AoE, Trigger, Fire | 65 | +5 INT | При приземлении скилла — трупы в зоне взрываются (Fiery Reclamation) |
| Xoph's Pyre | Breachlord | Lineage | 65 | +5 STR | +20% Fire Damage as Extra Chaos; Chaos Hits также учитываются для Ignite/Flammability |
| Zarokh's Refrain | Spell Echo | Lineage, Spell, AoE | 65 | +5 INT | Spell Echo 2 раза (с коротким Cooldown); не поддерживает Channelling, Remote, Triggered, с CD |

---

## Обычные Support Gems по атрибуту

### STR — Level 1

Added Fire Damage, Armour Explosion, Bleed Chance, Bloodlust, Break Endurance, Brutality, Corrupting Cry, Double Barrel, Empowered Damage, Enduring Stuns, Eternal Flame, Execute, Far Reach, Fast Forward, Fire Infusion, Fist of War, Ignition, Impact Shockwave, Increased Armour Break, Inspiration, Iron Grip, Jagged Ground, Lacerate, Less Duration, Lifetap, Lockdown, Meat Shield, More Duration, Overpower, Persistence, Premeditation, Pulverise, Rage, Ruthless, Stomping Ground, Unbreakable, Vitality

### STR — Level 2

Aftershock, Ancestral Urgency, Auto Reload, Bludgeon, Demolisher, Devastate, Exploit Weakness, Fire Penetration, Font of Blood, Fresh Clip, Herbalism, Holy Descent, Infernal Legion, Ironwood, Knockback, Life Leech, Life Thief, Melee Physical Damage, Primal Armament, Raging Cry, Splinter, Weapon Elemental Damage

### STR — Level 3

Behead, Cannibalism, Dazing Cry, Deep Cuts, Despoiler, Enraged Warcry, Fire Exposure, Font of Rage, Ground Effect Duration, Heft, Immolate, Long Fuse, Rageforged, Rupture, Searing Flame, Tremors, Upheaval

---

### DEX — Level 1

Acceleration, Added Lightning Damage, Ammo Conservation, Biting Cold, Bursting Plague, Chain, Combo Finisher, Comorbidity, Conduction, Corrosion, Crescendo, Deceleration, Empowered Cull, Encumbrance, Envenom, Extended Combo, Faster Attacks, Faster Projectiles, Increase Limit, Innervate, Lasting Shock, Leverage, Life Drain, Lightning Infusion, Lockdown, Martial Tempo, Multiple Charge, Multiple Poison, Multiple Projectiles, Multiple Trap, Murderous Intent, Overabundance, Perpetual Charge, Pierce, Pin, Poison Chance, Precision, Profusion, Scattershot, Second Wind, Slower Projectiles, Swift Affliction, Wind Wave, Window of Opportunity

### DEX — Level 2

Additional Accuracy, Blind, Bullseye, Close Combat, Electrocute, Ferocity, Ingenuity, Lightning Penetration, Maim, Mana Leech, Momentum, Practiced Combo, Ranged Combat, Reduced Cooldown, Ricochet

### DEX — Level 3

Culling Strike, Culmination, Dazing, Deadly Poison, Discombobulate, Enduring Life, Enduring Mana, Life Bounty, Lightning Exposure, Mana Bounty, Mobility, Neural Overload, Nimble Reload, Overcharge, Payload, Soul Drain

---

### INT — Level 1

Added Cold Damage, Ambush, Arcane Tempo, Arcane Surge, Area of Effect, Clarity, Cold Infusion, Concentrated Effect, Controlled Destruction, Decaying Hex, Deep Freeze, Elemental Army, Energy Barrier, Enervation, Essence Harvest, Expanse, Faster Casting, Fortress, Frost Nexus, Frozen Vortex, Glaciation, Heightened Curse, Hourglass, Ice Bite, Ignite Proliferation, Impending Doom, Last Gasp, Magnified Effect, Minion Instability, Minion Pact, Spell Cascade, Unleash, Withering Touch

### INT — Level 2

Bidding, Cold Penetration, Considered Casting, Corpse Conservation, Coursing Current, Excise, Feeding Frenzy, Fiery Death, Focused Curse, Font of Mana, Fragility, Glacier, Hinder, Icicle, Inevitable Critical, Intense Agony, Impetus, Mana Flare, Potential, Rising Tempest, Ritualistic Curse, Shock Siphon, Soul Thief, Spell Echo, Strip Away, Tempestuous Tempo, Wildfire

### INT — Level 3

Ablation, Added Chaos Damage, Astral Projection, Biting Frost, Burning Inscription, Capacitor, Chaos Infusion, Chaos Mastery, Chaotic Freeze, Cold Exposure, Cold Mastery, Critical Damage, Cursed Ground, Danse Macabre, Drain Ailments, Elemental Discharge, Elemental Focus, Energy Retention, Execrate, Extraction, Fire Mastery, Frostfire, Hex Bloom, Lightning Mastery, Minion Mastery, Physical Mastery, Stormfire, Supercritical, Wildshards

---

## Крафт

- Обычные Support Gems: **Engrave an Uncut Support Skill Gem** → выбор гема и тира
- Lineage Gems: **выпадают из контента эндгейма** (Breach, Pinnacle и т.д.) — за исключением [[Cirel's Cultivation]], которая крафтится
- Уровень Support Gems не повышается XP — только через крафт нового тира

## Связанные концепции

- [[skill-gems]] — Skill Gems, которые поддерживаются Support Gems
- [[skill-categories]] — категории скиллов (Attack, Spell, Warcry, Minion и т.д.)
- [[skill-reference]] — полный справочник по скиллам
- [[mechanics/skill-system|skill-system]] — система гемов и сокетов
- [[mechanics/stats-attributes|stats-attributes]] — STR/DEX/INT требования
