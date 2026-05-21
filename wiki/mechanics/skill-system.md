---
category: mechanics
sources:
  - raw/fextralife/path-of-exile-2-wiki-hub.md
  - raw/fextralife/skills.md
patch: 0.4.0
updated: 2026-05-21
---

# Skill System

Принципиально переработанная относительно PoE 1 система гемов и пассивок.

## Skill Gems

- Гемы — отдельные item'ы, не вставляются в сокеты экипировки
- 9 стартовых сокетов гемов у персонажа (расширяются прокачкой/предметами)
- К каждому Skill Gem прикрепляется до **5 [[Support Gem|Support Gems]]**
- Цвет сокета меняется **детерминированно** — без RNG-чрома

В PoE 1 саппорты ставились через цветные сокеты в экипировке и линки. В PoE 2 этот слой убран — линковка происходит на уровне самого скилл-гема.

### Любой класс — любой скилл

> "Any class can use any Skill Gem"

Нет привязки гема к классу. Различия между классами идут через стартовый набор, ascendancy, weapon proficiency и пассивы.

## Uncut Gems и [[Gemcutting]]

Гемы как готовые item'ы **не дропаются**. Игрок собирает **uncut gems** в локациях и преобразует их через Gemcutting Menu.

Три типа сырых гемов:
- **Uncut Skill Gem** — создаёт новый активный скилл или повышает уровень существующего
- **Uncut Buff Skill Gem** — создаёт buff-скиллы (резервирующие [[Spirit]])
- **Uncut Support Gem** — создаёт [[Support Gem|саппорт]]

> "Uncut Skill Gems must be engraved into a Gem to become usable in the Gemcutting Menu,
> they can be used to create a Skill Gem or to Level an existing gem up to a certain level."

## Sockets внутри гема

> "Skill Gems can contain up to 5 sockets, but at the moment you first obtain them
> they usually have only 2 or 3, you can upgrade the amount of sockets with Jeweller's Orbs."

Цвет сокета привязан к [[stats-attributes|атрибуту]]:
- 🔴 Red — Strength
- 🔵 Blue — Intelligence
- 🟢 Green — Dexterity

Расширение сокетов: [[Jeweller's Orb|Jeweller's Orbs]] (как в PoE 1, но действуют на сам гем, а не на экипировку).

## Support Gems

- До 5 саппортов на скилл
- 100+ Support Gems в 0.2.0, +30+ в 0.4.0
- Система Support Gem перестроена в 0.3.0 («Support Gem system rebuild»)
- Цитата Fextralife: саппорты *"provide utility effects rather than direct offensive stats"* — намёк, что чистых +damage саппортов в PoE 2 меньше, чем в PoE 1.

## Persistent Buff Gems

Отдельная категория — постоянные баффы (auras, persistent buffs), резервирующие [[Spirit]] вместо маны. Создаются из **Uncut Buff Skill Gem**.

## Recommended combinations

В UI есть рекомендации сборок гемов для новичков (видимо, что-то вроде стартеров: рекомендованные саппорты для конкретного скилла).

## Weapon Swap и скиллы

В PoE 2 [[Weapon Set Swap|свап оружия]] интегрирован со скиллами:
- Скилл можно прикрепить к конкретному weapon set через extended description в Skill Gem tab
- При активации скилла без подходящего оружия игра **автоматически свапнет** набор

Полезно для гибридных билдов (например, [[Huntress]] со spear + thrown spear) и комбо-ротации.

## Категории скиллов

Fextralife делит активные скиллы на:
**Ammunition, Attack, Buff, Meta, Minion, Spell, Trigger, Warcry, Ascendancy**.

Подробные списки и пометки — [[skills/skill-categories|skill-categories]].

## Passive Tree

[[Passive Tree]] поддерживает **дуал-специализацию**: можно прокачивать 2 разных стиля боя в одном дереве. Точные правила переключения — TODO (проверить отдельный источник).

QoL: с 0.2.1 есть кнопка **Refund All Passives**.

## Gemcutting

[[Gemcutting]] — отдельная подсистема. Здесь — только базовые механики; подробности (стоимость, ограничения по уровню гемов, способы получения uncut gems) — TODO.

## Связанные ссылки
- [[combat|Combat basics]] — про Melee Enhancement (default attacks бесплатно усиливаются гемами)
- [[Spirit]] — резервация под persistent buffs
- [[classes|Классы]] — у каждого класса свой набор стартовых гемов
- [[skills/skill-categories|skill-categories]] — категоризация активных скиллов
