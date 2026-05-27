# Day 10 Concepts: Functions with Outputs (return)

~25 min of video, ~3 min here. One distinction here matters more than anything since Day 6.

## Prerequisites (builds on)

Day 8 (functions with inputs), Day 9 (dicts). Today the functions hand a value back instead of just printing.

## Practice exercises (do these before the project)

- **Leap Year (as a function):** write `is_leap(year)` that **returns** True/False using the rule: divisible by 4, except not by 100, unless also by 400. The point is to return the boolean, not print it, so the caller can use it. This is the exact return-vs-print lesson in practice.
- **Days in a month:** use your `is_leap` function to return the correct number of days for a given month and year (February depends on the leap result). Tests calling one function from another.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 10 Goals | SKIP | Build a calculator. |
| 002 | Functions with Outputs | READ | `return` sends a value back. |
| 003 | Multiple return values | READ | Return more than one thing at once. |
| 005 | Docstrings | READ | The `"""..."""` that documents a function. |
| 007 | The Calculator Project | answer key | Your build. |
| 008 | How to Get a Good Night's Sleep | SKIP | Pep talk. |

## The actual content

**return vs print (the key distinction).** This trips up almost everyone.
- `print(x)` shows something on screen and is gone. The function gives nothing back.
- `return x` hands a value back to whoever called the function, so you can store and reuse it: `result = add(2, 3)`.
- A function that prints but doesn't return cannot be chained or reused. `total = add(2, 3)` where `add` only prints would make `total` equal `None`. This is the single most common beginner confusion and it's the root of the "why is my variable None" bug.

**Multiple return values.** `return a, b` actually returns a tuple, and you can unpack it: `x, y = get_point()`. Convenient, used constantly.

**Docstrings.** A string on the first line inside a function, in triple quotes, that explains what it does. Tools and editors read it. Light habit to build now; it's expected in professional code and on your GitHub.

## The trap to remember (Anki this)

If a function "isn't working" and a variable holding its result is `None`, check whether the function actually `return`s or just `print`s. Print is for humans; return is for the rest of your program. They are not interchangeable.

## Bonus concept (used in the project)

Functions are values. You can store them in a dict: `operations = {"+": add, "-": subtract}`. Then `operations["+"]` *is* the add function, and `operations["+"](2, 3)` calls it. This "dispatch table" pattern replaces a long if/elif chain and is genuinely elegant. Note `add` (no parentheses) is the function itself; `add()` calls it.

## Build spec: Calculator

Done when: the four operations each `return` (not print) their result, the operation is picked from the dict by symbol, and the calculator can continue with the previous result as the new first number. Handle divide by zero so it doesn't crash. Verify a function returns by storing its result in a variable and printing that, not by printing inside the function.
