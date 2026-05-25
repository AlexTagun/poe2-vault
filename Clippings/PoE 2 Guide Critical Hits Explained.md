---
title: "PoE 2 Guide: Critical Hits Explained"
source: "https://mobalytics.gg/poe-2/guides/critical-hits"
author:
  - "[[Dreamcore]]"
published: 2025-05-20
created: 2026-05-25
description: "Check out this guide on Critical Hits in Path of Exile 2 for information on Critical Hit Chance, Critical Damage Bonus and more!"
tags:
  - "clippings"
---
![Mobalytics](https://cdn.mobalytics.gg/assets/common/icons/mobalytics-logo/logo-mobalytics-collapsed-fixed.svg) Use your favourite features in-game with our Desktop App

**Critical Hits** are on-Hit effects in Path of Exile 2.

![](https://cdn.mobalytics.gg/cdn-cgi/image/format=auto,width=1000/uploads/images/poe-2/crit_icon.png)

### What are Critical Hits?

Critical Hits are on-Hit effects that **make the Damage of the Hit gain a Damage multiplier based on Critical Damage Bonus**. The bonus Damage of a Critical Hit is **not dealt separately** in its own packet of Damage, and is instead a **multiplier to the base Damage** of the original Hit.

**Note: Damage over time cannot Critically Hit. However, Damaging Ailments inflicted by Critical Hits will have their Damage scaled accordingly.**

### Critical Hit Chance

The **chance** to deal a Critical Hit is **rolled when a Skill is first used**. A **random number is rolled between 0 and 99.99**, and this number is used as a **threshold that must be exceeded** to confirm that the Hit will be a Critical Hit.

For example you use Firestorm and randomly roll the Critical Hit threshold, resulting in a threshold of 17.4. You must have a Critical Hit Chance of at least 17.5% to deal Critical Hits with this Skill usage. If your Critical Hit Chance is lower than 17.5%, then any Hits resulting from that Skill usage will be normal, non-Critical Hits.

**Note: Buffs and Debuffs can still cause a Hit to change its behaviour in terms of being a Critical Hit or not, such as a Monster with the Critical Weakness Debuff.**

**Note: modifiers that prevent you from dealing Critical Hits such as** Resolute Technique **always override modifiers that guarantee Critical Hits, for example** Sunder**.**

To prevent awkward gameplay, some Skills will **roll their Critical Hit threshold on a per-Hit basis**, or in the case of **Channelling Skills** like Incinerate, they'll **roll a new Critical Hit threshold per interval or stage**. An example of **Skills that roll this check on a per-Hit basis are Projectile abilities that fire multiple Projectiles**, such as Rain of Arrows.

**Note: Monsters do not roll this check on a per-Hit basis like players. Instead, Skills they use that fire multiple Projectiles will only check once at Skill usage, resulting in either all Hits dealing Critical Hits, or none.**

#### Spells and Critical Hit Chance

**Spell Skills** have their **base Critical Hit Chance derived from the Skill Gem** itself, which will specify a base Critical Hit Chance. Pure Physical Damage Spells such as Bone Cage are amongst the highest base Critical Hit Chance Spells in the game, whilst pure Fire Damage Spells typically have the lowest.

**Tip: check out our guide on** [**Damage Types**](https://mobalytics.gg/poe-2/guides/damage-types) **for more information!**

#### Attacks and Critical Hit Chance

Unlike Spells, **Attack Skills** have their **base Critical Hit Chance derived from the equipped weapon** that's used to perform the Attack instead. The **exception to this is Offhand Attacks** such as Shield Charge, **and Unarmed Attacks**, for example Shattering Palm. **Offhand and Unarmed Attacks have a base Critical Hit Chance derived from the Skill Gem** itself, similar to Spells.

#### Scaling Critical Hit Chance

There are two types of modifiers to scale your Critical Hit Chance; **multipliers** and **flat additions**.

**Multiplier modifiers** are much more common, for example Heartstopping. These modifiers **directly multiply your base Critical Hit Chance**. For example if you have a total of 75% increased Critical Hit Chance and you use Fireball which has a base Critical Hit Chance of 7%, your final Critical Hit Chance would be 12.25% (7 \* 1.75). Whilst **increases and reductions are additive**, note that **more multipliers to Critical Hit Chance also exist**, such as Charge Regulation, which are **multiplicative with each other**.

**Flat Critical Hit Chance modifiers** are much rarer because they **add their percentage to your base Critical Hit Chance before any multiplier modifiers are calculated**. For example the Struck Through Passive Skill Tree notable adds 1% to the Critical Hit Chance for Attacks. If you were using the Pillar of the Caged God Unique Quarterstaff to Attack, your base Critical Hit Chance would be improved from 10% to 11%, and this percentage would then be multiplied by any multiplier modifiers you have. As a result, flat Critical Hit Chance modifiers are extremely powerful as they can make multiplier modifiers much more efficient in terms of how much Critical Hit Chance they provide.

#### Evasion and Critical Hit Chance

The [**Evasion**](https://mobalytics.gg/poe-2/guides/evasion) **mechanic has a special interaction** that **provides an additional layer of defence against Critical Hits**. When a Critical Hit succeeds the [Accuracy](https://mobalytics.gg/poe-2/guides/accuracy) and Evasion Hit check calculation, **it must succeed a secondary check to confirm the Critical Hit**. If the second check fails, the Critical Hit is downgraded to a normal non-Critical Hit, but **notably it still Hits the target because the first check passed**.

#### Lucky and Unlucky

If you have **Lucky Critical Hit Chance**, the **random Critical Hit threshold number will be rolled twice** and the **lower number is used**. Conversely, if you have **Unlucky Critical Hit Chance**, it will be **rolled twice** with the **higher number used**.

### Critical Damage Bonus

The **extra Damage dealt by a Critical Hit** is **determined by Critical Damage Bonus**. By default, Critical Damage Bonus for both player characters and their minions is **100%**, for an effective **200% of base Damage dealt**.

**Note: the default Critical Damage Bonus for Monsters is 30%.**

#### Scaling Critical Damage Bonus

Similar to Critical Hit Chance, there are two types of modifiers to scale your Critical Damage Bonus; **multipliers** and **flat additions**.

**Multipliers** are common modifiers that **scale your total flat Critical Damage Bonus**. For example the Supercritical Support Gem grants *'* **100% increased Critical Damage Bonus** *'*. This alone would largely scale your Critical Damage Bonus for the supported Skill, from the default 100% to 200%, or an effective 300% of base Damage dealt on a Critical Hit. **Increases and reductions to Critical Damage Bonus are additive** before being applied, but rarer **more and less modifiers also exist**, for example Pain Attunement, which are **multiplicative with each other**.

**Flat Critical Damage Bonus modifiers** also exist and are typically quite rare because they **add their total to your default base Critical Damage Bonus before any multiplier modifiers are calculated**. For example a Soul Core of Ticaba socketed into a Martial Weapon provides *'* **+5% to Critical Damage Bonus** *'*. This alone would bring your Critical Damage Bonus up to 105% prior to any scaling from multiplier modifiers.

**Note: the Critical Damage Bonus provided by** Soul Core of Ticaba **is local to the Martial Weapon it's socketed into.**

### Inevitable Critical Hits

**Inevitable Critical Hits** is a modifier granted by the Oracle's Forced Outcome Ascendancy Notable. This modifier will **cause Hits that** **can Critically Hit** to **reroll their Critical Chance upon failing until they ultimately succeed** the Critical Chance check and deal a Critical Hit. However, **every time the reroll occurs, the resulting Critical Damage Bonus will be diminished**.

### Defence Against Critical Hits

You can invest into modifiers that help to **mitigate the extra Damage from incoming Critical Hits**. For example Battle-hardened provides *'* **Hits against you have 20% reduced Critical Damage Bonus** *'*. These modifiers [**stack additively**](https://discord.com/channels/174993814845521922/1118165205025828884/1425208902319869972) **with Monster Critical Damage Bonus**, and therefore if you were Critically Hit by a Monster with the **default 30% Critical Damage Bonus whilst you had** Battle-hardened **allocated**, the **Hit would deal Damage to you as though the Monster had 10% Critical Damage Bonus**.

The Brass Dome has the modifier *'* **Take no Extra Damage from Critical Hits** *'*, **fully preventing any extra Damage resulting from Critical Damage Bonus on any incoming Critical Hits**.

### Nebuloch

The Nebuloch Unique Mace **forces Attack Skills** to **consume an Endurance Charge on use** if you have one **to guarantee a Critical Hit** on that Attack.

### Tangletongue

Tangletongue is a Unique Spear that has the special modifier *'* **Bifurcates Critical Hits** *'*. This modifier **causes the Critical Hit Chance check to be rolled twice**, and checks both outcomes. **If one roll succeeds, the Hit will be a Critical Hit**. However, **if both rolls succeed, the Hit will be a Critical Hit with** **double** **your normal Critical Damage Bonus**.

PoE 0.5 Campaign Checklist - Stats, rewards, skillpoints and more

Beginner

Beginner

PoE 2 Essence Guide - How to Use them Efficiently

Beginner

Currency

Crafting

Beginner

Currency

Crafting

\[REMOVED\] Expedition Crafting Guide with Tips and Tricks

Beginner

Crafting

Currency

Beginner

Crafting

Currency

0.5 - Return of the Ancients: Free Weekend

News

News