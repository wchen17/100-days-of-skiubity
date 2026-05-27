# Day 7 Concepts: Hangman (Decomposition)

This day teaches almost no new syntax. Its real lesson is **how to break a big problem into steps**, which is the skill the whole course is secretly about.

## Practice exercises (do these before the project)

No standalone exercises today. Hangman is built in 5 guided steps (videos 003-007). Treat each step as a mini-exercise: read what the step should do, attempt it yourself, then watch that step's video only to check or unstick. That keeps the step-by-step format from turning into pure transcription.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 7 Goals | SKIP | Build Hangman. |
| 002 | Break a Problem into a Flow Chart | **WATCH** | The actual lesson. Decomposition. |
| 003 | Step 1: Random word + checking | answer key | Build steps, attempt first. |
| 004 | Step 2: Replacing blanks | answer key | |
| 005 | Step 3: Checking for a win | answer key | |
| 006 | Step 4: Tracking lives | answer key | |
| 007 | Step 5: Improving UX | answer key | |
| 008 | Benefits of Daily Practice | SKIP | Pep talk. |

## Why video 002 is the one to watch

Hangman uses only things you already know: lists, loops, conditionals, `random.choice`. Nothing new. So the difficulty is entirely in **decomposition**: turning "build Hangman" into an ordered list of small solvable pieces. That translation is the exact muscle that the old fill-in-the-TODO templates did for you. This video shows you doing it yourself with a flow chart. That is the transferable skill; the syntax is not.

The principle: every program you'll ever write past this point is a decomposition problem first and a syntax problem second. Interviews test decomposition. Get reps on it now, on an easy problem, so it's automatic on hard ones.

## The decomposition (try it before reading)

Hangman breaks into: pick a word, show it as blanks, take a guess, reveal matching letters, lose a life on a miss, check win (no blanks left) and loss (no lives left), loop until one happens. Draw that as boxes and arrows before you write a line. If you can draw the flow chart, the code is just translation.

## Concepts you'll reuse

- `["_"] * 5` makes `["_", "_", "_", "_", "_"]`. List times integer repeats it.
- `letter in word` checks membership and returns True/False.
- `display[i] = letter` updates a list item in place by index.
- `" ".join(display)` turns `["_", "a", "_"]` into `"_ a _"` for display.

## Build spec

Done when: a random word is hidden as blanks, correct guesses fill the right positions (all of them, if the letter repeats), wrong guesses cost a life, and the game ends correctly on both win (word complete) and loss (lives gone). Test a word with a repeated letter; that's where most Hangman bugs hide.
