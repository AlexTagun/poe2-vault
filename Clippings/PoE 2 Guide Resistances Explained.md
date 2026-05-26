---
title: "PoE 2 Guide: Resistances Explained"
source: "https://mobalytics.gg/poe-2/guides/resistances"
author:
  - "[[Dreamcore]]"
published: 2025-04-28
created: 2026-05-26
description: "Check out this detailed guide for information on Resistances, Exposure, Penetration and more in Path of Exile 2!"
tags:
  - "clippings"
---
![Mobalytics](https://cdn.mobalytics.gg/assets/common/icons/mobalytics-logo/logo-mobalytics-collapsed-fixed.svg) Use your favourite features in-game with our Desktop App

**Resistances** are core defensive stats in Path of Exile 2 and are specific to a type of Damage. You can find Resistance-related stats on Suffix modifiers on gear.

![](https://cdn.mobalytics.gg/cdn-cgi/image/format=auto,width=1000/uploads/images/poe-2/res.jpg)

*Lightning Resistance icon as seen in the Character Sheet*

### What is Resistance?

**Resistance is a core Damage type defensive stat that any character can access** by default. Resistance is applied to **reduce incoming Damage of the relevant type by the stated percentage**. For example if you take 1000 Fire Damage and you have 75% Fire Resistance, you'll take 250 Fire Damage after Fire Resistance has been applied.

Resistance exists for each type of Damage **except for Physical Damage**, and therefore you can obtain modifiers to **Fire****,** **Cold****,** **Lightning** and **Chaos** **Resistance**.

**Note: Physical Damage does not have associated Resistance, and is instead referred to as Physical Damage Reduction, typically provided by** [**Armour**](https://mobalytics.gg/poe-2/guides/armour) **and Additional Physical Damage Reduction.**

![](https://cdn.mobalytics.gg/cdn-cgi/image/format=auto,width=1000/uploads/images/poe-2/resistancesheet.jpg)

*Resistances section in the Character Sheet*

You can **view an overview of your Resistances in your character sheet (default: Press C)**, with a more detailed view listed below the main section at the top. See the below section for more information on reading Resistances from your character sheet.

### Resistance Cap

**Resistances are** **capped at 75% by default**. This is the effective cap on Damage reduction provided by the relevant Damage Resistance and **does not include** other methods of mitigating Damage, for example the Less Damage taken from Bulwark. Other methods used to mitigate Damage are calculated on a separate layer, [see the full order of operations guide here](https://mobalytics.gg/poe-2/guides/damage-defence-calc-order) for more details.

The cap on Resistances **can be increased with rare modifiers to Maximum Resistances**, for example Crystalline Resistance. **Maximum Resistances are hard-capped at 90%**.

**Note: you must still have enough Resistance to reach the cap to obtain that amount of mitigation.**

### Understanding Resistance Numbers in the Character Sheet

Resistance is typically listed as two numbers at the top section in your character sheet. The **first number indicates your effective Resistance**, or the number that is used to mitigate incoming Damage of that type. The **second number in brackets indicates your total uncapped Resistance** - this is the sum of all modifiers to that type of Resistance.

![](https://cdn.mobalytics.gg/cdn-cgi/image/format=auto,width=1000/uploads/images/poe-2/resistance12.jpg)

*Capped and Uncapped Resistance in the Character Sheet*

Whilst uncapped Resistance may not be important to the actual mitigation that's provided by this stat, it's important for **any modifiers that impose negative Resistances** on you, for example [Exposure](https://mobalytics.gg/poe-2/guides/exposure) or a Curse such as Elemental Weakness. Knowing how much reduction to a Resistance an effect will impose on you means you're able to overcap your Resistance(s) by enough to ensure that those negative Resistances will not bring you below your Resistance cap. See the section below on Negative Resistances for more information.

### Value of Maximum Resistances

Obtaining modifiers that improve your Maximum Resistances is an effective way to boost your mitigation against the relevant Damage type. However, it's important to understand how valuable Maximum Resistances are as you get closer and closer to the 90% hard cap.

**Each percentage of Resistance will mitigate the same amount of Damage**. For example at 75% Fire Resistance you'll mitigate 750 Fire Damage from a Hit of 1000 Fire Damage. Each percentage is mitigating 10 Fire Damage. If you increase your Maximum Fire Resistance by 1% to 76%, you're now mitigating 760 Fire Damage from the same Hit, an increase in Damage mitigated of 10 Damage. However, **the more Maximum Resistance you obtain, the more valuable modifiers to Maximum Resistance become as the mitigation provided relative to the Damage taken becomes more and more**.

| Fire Resistance | Damage taken from 1000 Fire Damage |
| --- | --- |
| 75% | **250** |
| 80% | **200** |
| 85% | **150** |
| 90% | **100** |

*Example table showing Damage taken after Resistance mitigation*

At 75% Fire Resistance you'll take 250 Fire Damage from a Hit of 1000 Fire Damage. If you obtain modifiers for an additional 5% Maximum Fire Resistance, you'd have 80% Fire Resistance and you'd take 200 Fire Damage from the same Hit. You've gone from taking 250 Damage to 200 Damage, or an effective 20% less Damage taken. If you then obtain a further 5% Maximum Fire Resistance, you'd now have 85% Fire Resistance and you'd take 150 Fire Damage from the Hit. You've gone from taking 200 Damage to 150 Damage, or an effective 25% less Damage taken. Going from 85% to 90% Maximum Fire Resistance would mean you'd take 100 Fire Damage from the Hit, or an effective 33.3% less Damage taken compared to having 85% Fire Resistance.

**For this reason, modifiers to Maximum Resistances are rare and extremely valuable, especially the more of them you're able to obtain.**

**Tip: every percent counts! Going from 89% to 90% Resistance is an effective ~9% less Damage taken!**

### Modifiers to Negative Resistances (Exposure, Curses etc.)

There are effects that will **impose negative Resistances on an entity**. The most common of these effects is **Exposure and Curses**.

Exposure is a Debuff that **lowers a specific Resistance by 20% by default**, and can be improved with modifiers to Exposure Effect, for example Overexposure.

There are also some **Curses that also lower a specific Resistance** such as Elemental Weakness. The amount of negative Resistance imposed by a Curse is derived from the level of the Curse Skill gem and any modifiers to the Magnitude of Curses, such as Master of Hexes.

**Negative Resistances from these effects are always applied to the total uncapped Resistance** that an entity has. For example if a character has 75% (114%) Lightning Resistance, this means they have an effective 75% Lightning Resistance for the purpose of Resistance mitigation and 114% uncapped Lightning Resistance. If the character had Exposure inflicted on them, their Lightning Resistance would now be 75% (94%) following the -20% Resistance from a default Exposure. If they were also Cursed with a Level 1 Elemental Weakness, their Lightning Resistance would be lowered by a further 23%, bringing it down to 54% (54%). This means that the character's effective Lightning Resistance for mitigation has been lowered below their cap of 75%, so they're now effectively mitigating less Lightning Damage, and taking a lot more Damage as a result.

### Resistance Penetration

**Penetration is a modifier that allows the Damage of a Hit to bypass Resistance by the stated amount**. For example Breath of Fire will grant a character 15% Fire Penetration, which will allow their Hits that deal Fire Damage to Monsters to bypass 15% of Monster Fire Resistance, effectively treating the Monster's Fire Resistance as being 15% lower. However, **Resistance Penetration cannot Penetrate Resistances beyond 0%**. Any Resistance Penetration in excess that would go beyond 0% is discarded.

When Resistance Penetration exists alongside a modifier that lowers Resistance such as Exposure, the effect that lowers Resistance is applied first and Resistance Penetration is calculated from the resulting Resistance value.

**Note: Penetration only applies to Hits and does not interact with Damage over time in any way.**

### Resistance Below 0

When Resistances are brought below 0% with effects such as Exposure and Curses, the **normal mitigation provided by that Resistance is reversed to instead make the entity take more Damage** from that type. For example a Boss Monster that has -17% Fire Resistance after being inflicted with a combination of Exposure and Curses will effectively take 17% more Damage from Fire Damage.

**Note: Penetration does not apply below 0% Resistance, even if the current Resistance is negative.**

### Ignoring Resistances

Some mechanics **allow the Damage of a Hit to fully ignore the Resistance value** on an entity. For example the Invoker's Sunder my Enemies... makes the Damage from your Critical Hits ignore Monster Elemental Resistances as long as they weren't currently in the negatives.

**When Damage ignores Resistance, the Resistance value is always treated as 0%**.

### Campaign Resistance Penalty

As you progress through the Path of Exile 2 story campaign, you'll slowly increment negative Elemental Resistances which apply permanently to your character. You **cannot avoid** these negative Resistances and they are applied upon completing each story Act.

**When completing an Act, you'll have -10% to all Elemental Resistances imposed on your character, up to -60% in total upon completing all six Acts.**

**Note: Campaign negative Resistance is not applied to Chaos Resistance.**

### Campaign Resistance Bonuses

**Slaying specific Boss Monsters in Campaign areas will award you with single-use items that permanently grant specific Elemental Resistance bonuses** when used. [See our guide on Campaign Bonuses in Normal](https://mobalytics.gg/poe-2/guides/campaign-loot-normal) and [Cruel areas](https://mobalytics.gg/poe-2/guides/campaign-loot-cruel) for more details. Obtaining all of the available Campaign Bonuses will grant **+20% to all Elemental Resistances** in increments of 10% to each specific Elemental Resistance, helping to somewhat negate the Resistance penalty imposed from Campaign Act completion.

**Note: there is also an optional Chaos Resistance Bonus found in Act 6.**

### Honour Resistance

In the **Trial of the Sekhemas**, you can obtain **Relics** which improve your **Honour Resistance** when placed in the Relic Altar. Honour Resistance is calculated using the same method as basic Resistances, mitigating any Damage that would impact your Honour.

### Smith of Kitava

The **Smith of Kitava** Warrior ascendancy has access to Coal Stoker and Forged in Flame.

Coal Stoker makes any modifiers you have to your Fire Resistance also be applied to both your Cold and Lightning Resistance at half of their value. For example a Suffix modifier that grants 26% to Fire Resistance would also grant 13% to Cold and Lightning Resistance. Be aware that this also applies to negative Resistances from effects that would lower your Fire Resistance.

Forged in Flame provides a way to scale all of your Maximum Elemental Resistances by only investing into Maximum Fire Resistance such as Unnatural Resilience. Increases to your Maximum Fire Resistance will also apply to both your Cold and Lightning Resistances, but as with the previous node, be aware that negative Maximum Fire Resistance modifiers will also affect your Cold and Lightning Resistances.

### Gemling Legionnaire

The **Gemling Legionnaire** Mercenary ascendancy can utilise Thaumaturgical Infusion to gain a large amount of Maximum Elemental Resistances based on the colours of the Support Gems used in their Skills.

### Acolyte of Chayula

The **Acolyte of Chayula** Monk ascendancy can use the Chayula's Gift notable to gain a very large amount of Maximum Chaos Resistance in addition to doubling their Chaos Resistance. Chaos Resistance is doubled **dynamically**, thus modifiers to negative Chaos Resistance such as Despair can be especially dangerous if you're only relying on a somewhat small amount of base Chaos Resistance.

For example an Acolyte of Chayula with the Chayula's Gift notable allocated only needs a total of 43% Chaos Resistance to cap their Chaos Resistance at 85% after it's doubled. If they were to be Cursed with Despair lowering their Chaos Resistance by 18%, they'd have 25% prior to doubling, and therefore their Chaos Resistance would be lowered from 85% to 50% following the Curse.

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