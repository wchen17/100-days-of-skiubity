# Day 6 Concepts: Functions & While Loops (Karel/Reeborg)

~35 min of video, ~3 min here. One WATCH flagged.

## Prerequisites (builds on)

Day 5 (loops) and Day 3 (conditionals).

## Practice exercises (do these before the project)

All in Reeborg's World (reeborg.ca/reeborg.html). Each is a rep on function reuse and loops:

- Build `turn_right()` out of three `turn_left()` calls (function reuse, since Reeborg only has turn_left).
- Define a `jump()` function and call it to clear a single hurdle.
- Clear a whole row of hurdles with a `while` loop instead of repeating jump calls.
- Variable-height hurdles: combine a `while` loop with conditionals so the robot climbs any height.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 6 Goals | SKIP | Solve mazes with functions. |
| 002 | Defining and Calling Functions | READ | `def name():` then `name()` to run it. |
| 003 | The Hurdles Loop Challenge | WATCH | Reeborg is visual; seeing the robot move helps. |
| 004 | Indentation in Python | READ | Whitespace defines code blocks. No braces. |
| 006 | While Loops | READ | `while condition:` repeats until condition is False. |
| 007 | Hurdles with While Loops | optional | Applied version of 006 in Reeborg. |
| 008 | Jumping over Variable Heights | optional | Combines while + conditionals. |
| 009 | Final Project: Escaping the Maze | answer key | Your build. Attempt first. |
| 010 | Why is this so Hard | SKIP | Pep talk. No content. |

## The actual content

**Defining and calling functions.** `def greet():` defines a reusable block; `greet()` runs it. Defining does not run it, calling does. This is the single biggest leap of the day: code you write once and trigger many times.

**Indentation IS syntax.** Most languages use `{ }` to mark what's inside a function or loop. Python uses indentation. The spaces are not cosmetic; they are how Python knows what belongs to the block. Mixing tabs and spaces, or being off by one level, is a real error (`IndentationError`). The principle: the language forces the visual structure to match the logical structure, so badly-indented code literally cannot run.

**While loops.** `while x < 10:` repeats the block as long as the condition is True, rechecking each pass. Use it when you don't know how many iterations you need in advance (for is for known counts; while is for "until something happens").
- **Infinite loop danger:** if nothing inside the loop ever makes the condition False, it runs forever. Always make sure something changes toward the exit.

## for vs while (the decision)

- Known count or iterating a collection: `for`.
- "Keep going until X happens": `while`.

## The trap to remember (Anki this)

A `while` loop whose condition never becomes False hangs forever. Before writing one, name the line inside that moves you toward the exit. If you can't, you have a bug before you've run it.

## Build spec: Escaping the Maze

Use Reeborg's World (reeborg.ca/reeborg.html) for the visual version. Done when: the robot navigates from start to exit using your own functions (`turn_right`, etc.) and a while loop that follows the wall, not a hardcoded sequence of moves. If your solution only works on one specific maze, you've hardcoded it; the point is a loop that reacts to walls.
