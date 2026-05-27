# Day 4 Concepts: Randomisation & Lists

Read this instead of watching all 7 videos. Total watch time is ~40 min; this is a 3 min read. Watch only the two flagged WATCH below.

## Prerequisites (builds on)

Day 2 (type conversion, `int()`, f-strings) and Day 3 (if/elif/else, which you'll use for the win comparison).

## Practice exercises (do these before the project)

These are the reps. Attempt each in a scratch file before Rock Paper Scissors; the project just integrates them.

- **Who will pay the bill:** put a few names in a list, then fairly pick one at random to pay. Tests picking a random index with `random.randint(0, len(names) - 1)` and indexing the list.
- **Treasure map (nested lists):** given a 3x3 grid of strings and a position like "B2", place an `"X"` at the right row and column. Tests nested-list indexing `grid[row][col]` and the offset idea.

## The videos, distilled

| # | Video | Verdict | What it actually teaches |
|---|---|---|---|
| 001 | Day 4 Goals | SKIP | "Here's what we'll build." It's Rock Paper Scissors. Now you know. |
| 002 | Random Module | READ (below) | `import random`, `random.randint(a, b)`, `random.choice(list)`. |
| 003 | Understanding the Offset and Appending | **WATCH** | List indexing. This is the one the old template assumed you knew. |
| 004 | Who will pay the bill | SKIP if 003 clicked | Applied example: pick a random person from a list to pay. Same tools as 002+003. |
| 005 | IndexErrors and Nested Lists | READ (below) | What breaks when an index doesn't exist; lists inside lists. |
| 007 | Project: Rock Paper Scissors | answer key | Don't watch first. This is your build. Watch only if stuck 15+ min. |
| 008 | Programming is like the Gym | SKIP | Pure pep talk. No content. |

## The actual content (so you can skip the videos)

**`random` module.** Python's randomness is pseudo-random: a formula seeded from the system clock, not true randomness. Enough for games, not for cryptography (that matters later for the Caesar cipher day and your security track).
- `import random` at the top of the file.
- `random.randint(0, 2)` returns an int from 0 to 2 **inclusive of both ends** (unlike most Python ranges, which exclude the top. This one does not).
- `random.choice(my_list)` returns one random item from the list.

**Offset / list indexing (the WATCH video).** A list is an ordered collection: `options = ["rock", "paper", "scissors"]`.
- Index is an **offset from the start**, so it's 0-based: `options[0]` is "rock", `options[2]` is "scissors". The offset is "how far from the front," which is why the first item is 0 away, not 1.
- Negative indexes count from the end: `options[-1]` is the last item.
- `options.append("lizard")` adds to the end.
- `len(options)` is the count (3 here), so the last valid index is always `len(list) - 1`.

**IndexError + nested lists.** `options[3]` on a 3-item list raises `IndexError: list index out of range`, because valid indexes are 0, 1, 2. This is the single most common list bug. A nested list is a list of lists: `grid = [[1,2],[3,4]]`, and `grid[0][1]` is 2 (first row, second item).

## The trap to remember (Anki this)

`random.randint(0, 2)` includes 2, but `range(0, 2)` does NOT include 2. Same-looking bounds, opposite behavior. This bites everyone on Day 5 when loops show up.

## Bugs you actually hit on this build (Anki these)

**The str vs int trap (the one that made you always lose).** `input()` always returns a string. If you write `player_choice = input(...)` without `int()`, then `player_choice == computer_choice` compares a string to an int, which is always False. So the draw check and all three win checks never fire and the game silently falls through to "you lose" every round. Fix: convert at the source, `player_choice = int(input(...))`. Rule: convert input the moment you read it, not later, so the variable holds the right type everywhere it's used.

**The IndexError (typing a number out of range).** `art` has 3 items, so the only valid indexes are 0, 1, 2. Type 5 and `art[5]` raises `IndexError: list index out of range`. Fix it with input validation: check the value is in range before using it as an index.

```python
player_choice = int(input("...(0,1,2): "))
if player_choice < 0 or player_choice > 2:
    print("That's not a valid choice.")
else:
    # the rest of the game goes in here, so it only runs on valid input
    print(art[player_choice])
    computer_choice = random.randint(0, 2)
    # ... win logic ...
```

The principle (and it matters for your security track): never trust input to be in range. A valid index is always between 0 and `len(list) - 1`; user input can be anything, so you guard it at the boundary before you index. Out-of-range and malformed input is the basis of a whole class of real vulnerabilities, so building the "validate at the edge" reflex now pays off later.

Sibling bug: type a word like "rock" instead of a number and `int("rock")` raises `ValueError`, a different error that fires before you even index. The fully robust version handles both, and the cleanest form re-asks the question in a loop, which you can write after Day 5/6 (while loops). For now the if/else guard above is enough.

## Why a concept doc beats the video here

You can read the three ideas above in under three minutes and only the offset idea genuinely benefits from seeing it animated. Recognition from watching feels like learning but fades fast; reading the rule then immediately using it in the build forces retrieval, which is what actually encodes it.
