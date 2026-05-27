# Day 12 Concepts: Scope

New-concept day. Scope is invisible until it bites you, so read this before the project.

## Practice exercises (do these before the project)

- **Prime Number Checker:** write a function that returns whether a number is prime by testing divisibility in a loop. Tests scope (the loop variables are local) and returning a result. Bonus: return early as soon as you find a divisor instead of checking all the way.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 12 Goals | SKIP | Build a number guessing game. |
| 002 | Namespaces: Local vs Global | READ | Where a variable lives and who can see it. |
| 003 | Does Python Have Block Scope | READ | Short answer: no. This surprises people. |
| 005 | How to Modify a Global Variable | READ | The `global` keyword and why to avoid it. |
| 006 | Constants and Global Scope | READ | `UPPER_CASE` naming convention. |
| 008 | Number Guessing Game intro | answer key | Your build. |
| 009 | Solution Walkthrough | answer key | |
| 010 | Don't be too hard on yourself | SKIP | Pep talk. |

## The actual content

**Local vs global scope.** A variable created **inside** a function exists only inside it (local). Outside the function it doesn't exist. A variable created outside all functions is global and readable everywhere. The reason: functions get their own private workspace so their variables can't accidentally clobber each other. This is why returning a value is the clean way to get data out of a function, rather than reaching for globals.

**Python has no block scope.** This is the surprising one, especially coming to it before you hit C and Java (W&L CSCI 209/210). A variable created inside an `if` or `for` block **survives after the block ends**:
```python
if True:
    x = 5
print(x)   # works in Python. Would NOT in C/Java at block level.
```
Only **functions** create a new scope in Python, not loops or conditionals. Worth locking in now, because your W&L courses will use languages where this is the opposite, and the mismatch is a classic source of confusion.

**Modifying a global from inside a function.** Reading a global inside a function is fine. Reassigning it requires the `global` keyword, or Python makes a new local instead. But `global` is a code smell: it makes functions depend on hidden outside state, which is exactly the bug factory you'll fight when you refactor the meme RPG (its `global game_over` scattered everywhere is this anti-pattern). Prefer parameters in, return values out.

**Constants.** A variable you never intend to change, written `IN_UPPER_CASE` by convention, usually defined at the top of the file. Python won't stop you from changing it; the capitals are a message to other humans (and future you): "don't."

## The trap to remember (Anki this)

In Python, `if`/`for`/`while` blocks do NOT create scope; only functions do. A name set inside a loop is still visible after the loop. The flip side: a name set inside a function is invisible outside it. Mixing up these two rules is the source of both "why can't I see this variable" and "why did this variable leak."

## Build spec: Number Guessing Game

Done when: it picks a random 1-100 number, offers easy/hard difficulty (more/fewer turns), tells the player higher/lower after each guess, decrements turns, and ends correctly on both a correct guess and running out of turns. Keep the turn count flowing through return values rather than a global; this project is a chance to practice doing scope right.
