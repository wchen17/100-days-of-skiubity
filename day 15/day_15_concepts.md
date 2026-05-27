# Day 15 Concepts: Local Setup & Coffee Machine

First intermediate day. Two parts: setting up a local environment (you've already done this in VS Codium, so most of it is redundant for you), and building the Coffee Machine, which is the procedural setup for the Day 16 OOP refactor.

## Prerequisites (builds on)

Days 1-14, especially Day 9 (nested dicts for the menu and resources) and Day 10 (functions that return).

## Practice exercises (do these before the project)

No standalone exercises. The Coffee Machine is built from a requirements brief. This is the procedural "before" version that Day 16 refactors into OOP, so the real exercise is building it cleanly enough that the Day 16 refactor is illuminating rather than a rewrite.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Introduction and Requirements for Coffee Machine | **WATCH** | The spec. |
| 002 | Solution and Walkthrough | answer key | Open when stuck. |
| 003 | Pavlov's Coding Corner | SKIP | Filler about having a dedicated workspace. |

## On the setup portion

The course walks through installing Python and PyCharm. You already code in VS Codium with a working interpreter, so skip the install hand-holding. The one thing worth confirming: you can run a `.py` file from a fresh folder and `input()`/`print()` work in your terminal. They do, given your Day 1-14 work ran.

## Why the Coffee Machine matters (the real point)

You build it **procedurally** today: dictionaries for the menu and resources, functions for each step, a main loop. It works, but it's the kind of code that gets unwieldy: shared state passed around, logic spread across loose functions. That is deliberate. Day 16 immediately refactors this exact program into OOP (classes), so today's version is the "before" picture in a before/after lesson.

This is also your trigger for the meme RPG. Per your completions log, Day 16 is when you refactor `Deluxe meme rpg.py` from procedural to OOP. The Coffee Machine is structurally the same task at small scale, so treat it as the rehearsal: feel the pain of procedural shared state here, on 100 lines, before applying the fix to your 2,400-line file.

## Concepts in play (all learned)

Nested dictionaries (menu items with their ingredient costs), functions with returns, a while loop for the main program, conditionals for "enough resources" and "enough money" checks.

## The trap to remember (Anki this)

The resource check (do we have enough water/milk/beans?) and the payment check (did the coins cover the cost?) are separate gates, and refunding on insufficient payment vs reporting insufficient resources are different outcomes. Conflating them is the common bug. Map both failure paths before coding.

## Build spec

Done when: the machine reports resources, accepts a drink order, refuses with a clear message if resources are insufficient, processes coin input and gives correct change, refunds if payment falls short, deducts resources on a successful sale, and can be turned off. Keep your working version; you'll refactor it on Day 16, so don't delete it.
