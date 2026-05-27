# Prerequisites Map: 100 Days of Python

What each day depends on. Use it two ways: before a day, confirm the upstream concepts are solid; when a day fights you, this tells you which earlier day to review instead of grinding.

Concepts compound here. A wobble on Day 5 loops shows up as confusion on Day 7 Hangman, not as a "loop problem," so trace difficulty back up the chain.

## Beginner phase (Days 1-15)

| Day | Topic | Builds on | If this day is hard, review |
|---|---|---|---|
| 1 | Variables, print, input | (start) | nothing |
| 2 | Data types, type conversion, f-strings | Day 1 | Day 1 input/print |
| 3 | if/elif/else, logical operators, nesting | Day 2 | Day 2 (comparing typed values) |
| 4 | Randomisation, lists, indexing | Day 2 (type conversion), Day 3 (conditionals for win logic) | Day 2 `int()`, Day 3 if/elif |
| 5 | Loops (for, while, range) | Day 4 (lists), Day 3 (conditionals) | Day 4 lists |
| 6 | Functions, indentation, while loops | Day 5 (loops), Day 3 (conditionals) | Day 5 loops |
| 7 | Hangman (decomposition) | Days 4-6 (lists, loops, functions, random.choice) | whichever of 4-6 is shaky |
| 8 | Function parameters, Caesar cipher | Day 6 (functions), Day 5 (loops), Day 3 (conditionals) | Day 6 def/call |
| 9 | Dictionaries, nesting | Day 4 (lists), Day 5 (loops), Day 8 (functions w/ inputs) | Day 4 lists, Day 8 params |
| 10 | Functions with return | Day 8 (functions w/ inputs), Day 9 (dicts) | Day 8 (return vs the inputs you already learned) |
| 11 | Blackjack capstone | Days 1-10 (all of it) | any beginner day; this is the audit |
| 12 | Scope | Day 6 (functions), Day 10 (return) | Day 10 return vs global |
| 13 | Debugging | all prior | none; this fixes the others |
| 14 | Higher Lower capstone | Days 1-13, esp Day 9 (list of dicts), Day 10 (return), Day 5 (score tracking) | Day 9 nested data, Day 10 return |
| 15 | Local setup, Coffee Machine | Days 1-14, esp Day 9 (nested dicts), Day 10 (functions/return) | Day 9 dicts |

## The load-bearing concepts

Three things carry most of the weight downstream. If any is shaky, fix it before moving on, because everything after leans on it:

- **Lists and indexing (Day 4).** Every collection, every loop body, every data structure after this assumes it.
- **Functions: define, call, parameters, return (Days 6, 8, 10).** The whole intermediate phase is functions and classes. The return-vs-print distinction (Day 10) is the single most common silent bug.
- **Dictionaries and nesting (Day 9).** API data (Day 32+) is nested dicts and lists. This is the most load-bearing concept for the entire second half of the course.

## Later phases

Will be added here as each phase's concept docs are built (16-31 next). The dependency chain gets simpler past Day 31: the course shifts to single multi-step projects, so "builds on" becomes "the previous part of this project" plus the one new library introduced that day.
