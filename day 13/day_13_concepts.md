# Day 13 Concepts: Debugging

No project, no new syntax. This is a method day, and it's one of the most useful in the whole course. Your Day 4 always-lose bug is exactly what this day prevents. WATCH the debugger video; the rest reads fine here.

## Practice exercises (do these instead of a project)

The whole day is exercises. Fix intentionally broken versions of earlier programs (Odd/Even, Leap Year, FizzBuzz, an average function) using the six-step process below. No new code, just repair. Force yourself to predict the bug before running, then confirm with the debugger.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Describe the Problem | READ | Say out loud what should happen vs what does. |
| 002 | Reproduce the Bug | READ | Find the smallest input that triggers it. |
| 003 | Play Computer, Evaluate Each Line | READ | Trace execution by hand. |
| 004 | Fixing Errors, Red Underlines | READ | Read the editor's warnings before running. |
| 005 | Squash Bugs with print() | READ | Print variables to see actual values. |
| 006 | Using a Debugger | **WATCH** | Breakpoints and stepping. Hard to learn from text. |
| 007 | Final Debugging Tips | READ | Wrap-up. |
| 011 | Building Confidence | SKIP | Pep talk. |

## The actual method (the whole point of the day)

A repeatable debugging process, in order:

1. **Describe it precisely.** "It always says you lose, even on a tie." Vague descriptions ("it's broken") hide the bug; precise ones often reveal it. Stating the expected vs actual is half the fix.
2. **Reproduce it reliably.** Find the exact input that triggers it every time. A bug you can't reproduce, you can't fix.
3. **Play computer.** Read your code line by line as if you were Python, writing down each variable's value. This is how you'd have caught Day 4: `player_choice` is `"0"` (a string), `computer_choice` is `0` (an int), so `"0" == 0` is False. Tracing by hand exposes it instantly.
4. **`print()` the variables.** When tracing in your head is too hard, print the actual values and types: `print(player_choice, type(player_choice))`. The values rarely match what you assumed; that gap is the bug.
5. **Use the debugger.** Set a breakpoint, run, and step line by line watching variables update live. It's print-debugging without editing code. Worth learning the keys in VS Codium now.
6. **Read the red underlines first.** The editor flags many errors before you even run. Don't ignore them.

The principle: bugs feel random but almost never are. Your code does exactly what you wrote; debugging is the disciplined process of finding where what-you-wrote diverges from what-you-meant. The process replaces guessing-and-rerunning, which is slow and teaches nothing.

## The single most useful habit (Anki this)

When something's wrong, `print(variable, type(variable))` before guessing. Most beginner bugs are a value or a type that isn't what you assumed (string vs int, None from a function that should return, an off-by-one index). Seeing the real value ends the guessing.

## No build today

Run the debugging drills in the day folder. Better: go fix the Day 4 type bug using the "play computer" method, then set a breakpoint there in VS Codium and watch `player_choice` to feel the debugger work on a bug you understand.
