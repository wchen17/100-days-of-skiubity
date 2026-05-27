# Day 11 Concepts: Blackjack Capstone

No new syntax. This is a test of Days 1-10 in one project. The right way to do it is to attempt from the requirements and treat every "Hint Solution Walkthrough" video as an answer key you open only when stuck.

## Prerequisites (builds on)

Everything from Days 1-10: random, lists, dicts, functions, return values, while loops, conditionals. This capstone deliberately uses no new syntax.

## Practice exercises (do these before the project)

No standalone exercises. Blackjack is the exercise. The "Hint Solution Walkthrough" videos replace separate drills, so the practice is attempting each function from the requirements before opening its hint video.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 11 Goals | SKIP | Build Blackjack. |
| 002 | Requirements and Game Rules | **WATCH** | The spec. This is all you should watch first. |
| 003 | Hint 4 & 5 Walkthrough | answer key | Open only if stuck on that piece. |
| 004 | Hint 6-8 Walkthrough | answer key | |
| 005 | Hint 9 Walkthrough (refactoring) | answer key | |
| 006 | Hint 10-12 Walkthrough | answer key | |
| 007 | Hint 13 Walkthrough | answer key | |
| 008 | A Solid Foundation goes a Long Way | SKIP | Pep talk. |

## How to actually do this day

Watch 002 (requirements) only. Then build from a blank file. The hint videos are deliberately chunked so you can unstick one specific function without seeing the whole solution. If you watch them all up front, you've turned a capstone into a typing exercise and learned almost nothing. The discomfort of being stuck is the entire value of a capstone.

The principle: a capstone exists to surface what you *think* you know but can't yet produce cold. Skipping the struggle hides exactly the gaps you need to find before they show up on something graded.

## The two genuinely tricky bits (think before you code)

1. **Ace logic.** An Ace is 11, unless that busts you, then it's 1. So: if your score is over 21 and an 11 is in your hand, swap that 11 for a 1 and recompute. This conditional re-scoring is the part everyone gets wrong first.
2. **Dealer rule.** The dealer is not random; it follows a fixed rule: keep drawing while score < 17, then stop. That's a `while` loop with a clear exit, not player choice.

A common design choice the course uses: a blackjack (21 on the first two cards) is represented as score `0` so it beats a normal 21. Decide your own representation if you prefer, just be consistent.

## Build spec

Done when: both player and dealer are dealt and scored correctly including the Ace adjustment, the player can hit or stand, the dealer follows the draw-to-17 rule, and the comparison declares the right winner across all cases (bust, blackjack, higher score, tie). Test a hand that forces an Ace from 11 to 1; that's the case that breaks naive solutions.
