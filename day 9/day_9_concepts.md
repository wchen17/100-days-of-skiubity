# Day 9 Concepts: Dictionaries & Nesting

~25 min of video, ~3 min here.

## Prerequisites (builds on)

Day 4 (lists), Day 5 (loops), Day 8 (functions with inputs).

## Practice exercises (do these before the project)

- **Grading Program:** given a dict of student names to numeric scores, build a new dict mapping each name to a letter grade using score ranges. Tests looping a dict with `.items()`, conditionals for the ranges, and building a second dict from the first.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 9 Goals | SKIP | Build a secret auction. |
| 002 | Dictionary Deep Dive | READ | `{key: value}` storage and lookup. |
| 004 | Nesting Lists and Dictionaries | READ | Dicts inside dicts, lists inside dicts. |
| 006 | Auction Instructions and Flow Chart | answer key | Your build. |
| 007 | Motivation and the Accountability Trick | SKIP | Pep talk. |

## The actual content

**Dictionaries.** A dict stores **key to value** pairs: `bids = {"Alice": 50, "Bob": 70}`. Unlike a list (accessed by position), a dict is accessed by key: `bids["Bob"]` gives 70. Use a dict when each item has a meaningful label, not just an order.
- Add or update: `bids["Carol"] = 90`. Same syntax for both; if the key exists it overwrites, if not it creates.
- Loop the pairs: `for name, amount in bids.items():` gives you both at once.
- Looking up a missing key raises `KeyError`. (Day 30 will teach the safe way to handle that.)

**Nesting.** Values can themselves be lists or dicts: `users = {"Alice": {"age": 30, "pets": ["cat"]}}`. Access drills in: `users["Alice"]["pets"][0]` is `"cat"`. This is how real data is shaped (JSON from APIs is exactly nested dicts and lists), so this is the most load-bearing concept of the early course for everything past Day 32.

## list vs dict (the decision)

- Ordered sequence, position matters, you'll loop it: **list**.
- Labeled lookups, "find the value for this key": **dict**.

## The trap to remember (Anki this)

`dict[key]` on a missing key crashes with `KeyError`, it does not return blank or None. Lists raise `IndexError` for the same mistake. Knowing which collection you have tells you which error to expect, which is half of debugging.

## Build spec: Secret Auction

Done when: it collects any number of name+bid pairs in a loop, clears the screen between bidders (`print("\n" * 20)`) so bids stay secret, and correctly names the highest bidder at the end. Test with three bidders where the highest is not the last one entered; a common bug is accidentally reporting the final entry instead of the max.
