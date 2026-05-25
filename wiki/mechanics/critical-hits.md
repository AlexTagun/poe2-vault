---
category: mechanics
sources: [Clippings/PoE 2 Guide Critical Hits Explained.md]
patch: 0.4.0
updated: 2026-05-25
---

# Critical Hits

Critical Hit — это on-Hit эффект, который умножает урон удара на основе [[#Critical Damage Bonus]]. Бонусный урон **не является отдельным пакетом урона** — это множитель к базовому урону хита.

**DoT не может крититовать.** Но Damaging Ailments, наложенные критическим ударом, масштабируются соответственно.

---

## Critical Hit Chance

### Как проверяется крит

При использовании скилла **генерируется случайное число от 0 до 99.99** — это порог. Если твой Critical Hit Chance **превышает** этот порог — удар будет критическим.

Пример: Firestorm сгенерировал порог 17.4. Нужен крит-шанс хотя бы 17.5%, чтобы удары от этого каста были критическими.

Некоторые скиллы бросают проверку **на каждый хит отдельно** — например, Projectile-скиллы вроде Rain of Arrows. Channelling-скиллы вроде Incinerate бросают проверку на каждый интервал/стадию.

> Монстры бросают проверку только один раз на использование скилла — либо все их хиты критические, либо ни один.

### Базовый крит-шанс

- **Заклинания** — базовый крит-шанс берётся из Skill Gem. Physical Damage Spells (Bone Cage) имеют наивысший базовый крит-шанс; чистые Fire-заклинания — наименьший.
- **Атаки** — базовый крит-шанс берётся из **экипированного оружия**. Исключение: Offhand Attacks (Shield Charge) и Unarmed Attacks (Shattering Palm) — у них крит-шанс из Skill Gem, как у заклинаний.

### Масштабирование крит-шанса

**Multiplier-моды** — наиболее распространены. Умножают твой базовый крит-шанс:
- `increased Critical Hit Chance` складываются аддитивно между собой
- `more Critical Hit Chance` (например, Charge Regulation) перемножаются мультипликативно

**Flat-моды** — редкие и очень ценные. Добавляют % **до** применения multiplier-модов. Это делает их непропорционально мощными — каждый дополнительный процент основы сильнее масштабируется всеми multiplier-модами.

Пример: [[items/weapons/quarterstaves|Pillar of the Caged God]] имеет 10% базового крит-шанса. Flat +1% от Struck Through превращает его в 11%, и **весь** множитель затем применяется к 11%, а не 10%.

### Evasion и крит

[[mechanics/stats-attributes|Evasion]] даёт **дополнительную защиту от критов**: после того как крит прошёл основную проверку точности/уклонения, он должен **пройти вторую проверку**. Если вторая проверка провалена — удар становится обычным, но всё равно попадает (первая проверка была пройдена).

### Lucky / Unlucky

- **Lucky Critical Hit Chance** — порог бросается дважды, берётся **меньший** (выгоднее для тебя).
- **Unlucky Critical Hit Chance** — порог бросается дважды, берётся **больший** (невыгодно).

---

## Critical Damage Bonus

Базовый Critical Damage Bonus игрока и его миньонов — **100%**, то есть крит наносит **200% базового урона**.

> Базовый Critical Damage Bonus монстров — 30%.

### Масштабирование

**Multiplier-моды** масштабируют весь накопленный Flat Critical Damage Bonus:
- `increased Critical Damage Bonus` складываются аддитивно
- `more/less Critical Damage Bonus` (например, [[mechanics/passive-skill-tree|Pain Attunement]]) перемножаются мультипликативно

Пример: [[skills/support-gems|Supercritical Support]] даёт 100% increased Critical Damage Bonus → базовые 100% вырастают до 200% → крит наносит 300% базового урона.

**Flat-моды** добавляют % **до** применения multiplier-модов и поэтому очень ценны. Пример: Soul Core of Ticaba (`+5% Critical Damage Bonus` в Martial Weapon) поднимает базу с 100% до 105%.

---

## Защита от критов

Моды вида `Hits against you have X% reduced Critical Damage Bonus` складываются аддитивно с базовым Critical Damage Bonus монстров.

Пример: при стандартных 30% крит-бонусе монстра и Battle-hardened (−20%) монстр фактически крититует как будто у него 10% крит-бонус.

**[[items/armor/uniques|The Brass Dome]]** — полностью предотвращает весь дополнительный урон от Critical Damage Bonus входящих критов.

---

## Inevitable Critical Hits

Модификатор от нотейбла **Forced Outcome** аскендансии [[builds/ascendancies/oracle|Oracle]].

При провале проверки крита — **бросок повторяется до успеха**. Но каждый перебросок **снижает Critical Damage Bonus** результирующего крита.

---

## Особые предметы и механики

### [[items/weapons/uniques|Nebuloch]]
Уникальная булава. Attack Skills **потребляют Endurance Charge** при использовании (если он есть) → **гарантированный критический хит** на эту атаку.

### [[items/weapons/uniques|Tangletongue]]
Уникальное копьё. Модификатор **Bifurcates Critical Hits**:
- Проверка крит-шанса бросается **дважды**.
- Если хотя бы один бросок успешен → Critical Hit.
- Если **оба** броска успешны → Critical Hit с **удвоенным** Critical Damage Bonus.

### [[items/jewellery/uniques|Maligaro's Virtuosity]]
Перчатки. **Your Critical Damage Bonus is 250%** (фиксировано, без диапазона). **Your Critical Hit Chance cannot be Rerolled** — крит-шанс нельзя изменить рандомизирующими механиками.

---

## Связанные страницы

- [[mechanics/stats-attributes]] — Evasion, Accuracy
- [[mechanics/passive-skill-tree]] — Pain Attunement, Resolute Technique
- [[skills/support-gems]] — Supercritical, Pinpoint Critical, Inevitable Critical
- [[builds/ascendancies/oracle]] — Forced Outcome (Inevitable Critical Hits)
- [[items/weapons/uniques]] — Nebuloch, Tangletongue
- [[items/armor/uniques]] — The Brass Dome
- [[items/jewellery/uniques]] — Maligaro's Virtuosity
