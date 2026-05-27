# Day 5 Concepts: Loops

~30 min of video, ~3 min here. Watch nothing unless a section below says so.

## Prerequisites (builds on)

Day 4 (lists) and Day 3 (conditionals).

## Practice exercises (do these before the project)

- **Highest Score:** given a list of scores, loop through and print the largest. Tests the running-max pattern (a tracking variable updated inside the loop).
- **FizzBuzz:** print 1 to 100, but "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for both. The classic loop + modulo + conditional drill, and a real interview screening question, so get it clean.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 5 Goals | SKIP | You're building a password generator. |
| 002 | for loop with Lists | READ | `for item in my_list:` walks every item. |
| 003 | Highest Score | READ | Applied: loop a list, track the max in a variable. |
| 004 | for loops and range() | READ | `range(start, stop, step)` generates numbers to loop over. |
| 006 | Project: Password Generator | answer key | Your build. Don't watch first. |
| 007 | Hard Work beats Raw Talent | SKIP | Pep talk. No content. |

## The actual content

**`for` loop over a list.** `for letter in ["a", "b", "c"]:` runs the indented block once per item, with `letter` holding the current one. This is the readable way to touch every element. No manual index needed.

**Tracking a value across a loop.** The "highest score" pattern: set `highest = 0` before the loop, then inside, `if score > highest: highest = score`. After the loop, `highest` holds the answer. This running-variable pattern is everywhere (max, min, sum, count).

**`range()`.** `range(0, 5)` yields 0, 1, 2, 3, 4. **The top is excluded.** This is the exact opposite of `random.randint(0, 5)` from Day 4, which includes 5. Same-looking bounds, opposite rule. `range(0, 10, 2)` adds a step: 0, 2, 4, 6, 8.
- `for i in range(n):` is how you do something exactly n times.

## The trap to remember (Anki this)

`range(a, b)` stops **before** b. `randint(a, b)` stops **on** b. If you ever loop one short or one long, this is why. The technical reason: `range` is built for indexing, and a list of length n has valid indexes 0 to n-1, so `range(n)` deliberately stops at n-1.

## For the password generator

You'll loop to add N random characters. The hard version builds a list, shuffles it, then joins it back to a string. Building a string by repeated `+=` vs building a list then `"".join()` is the same idea you'll see again in real code, where join is the efficient one.
