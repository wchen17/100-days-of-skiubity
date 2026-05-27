# Day 8 Concepts: Function Parameters & Caesar Cipher

New-syntax day. Concept gate at the bottom: don't start the cipher until parameters click.

## Practice exercises (do these before the project)

- **Life in Weeks:** given an age, print how many days, weeks, and months remain assuming a 90-year life. Tests writing a function that takes an input and computes from it.
- **Love Calculator:** given two names, count how many times the letters in TRUE and LOVE appear across both, and combine into a score. Tests counting with inputs and returning a result.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Day 8 Goals | SKIP | Build a Caesar cipher. |
| 002 | Functions with Inputs | READ | `def f(x):` parameters let a function take data. |
| 004 | Positional vs Keyword Arguments | READ | Order vs naming when you call. |
| 006 | Caesar Part 1: Encryption | answer key | Build, attempt first. |
| 007 | Caesar Part 2: Decryption | answer key | |
| 008 | Caesar Part 3: Reorganising | answer key | Refactor into one reusable function. |
| 009 | How You Can Stay Motivated | SKIP | Pep talk. |

## The actual content

**Parameters (inputs).** A parameter is a named slot in a function definition: `def greet(name):`. When you call `greet("Bob")`, `name` becomes `"Bob"` inside the function. This is how functions become general instead of doing the same fixed thing every time. The difference from Day 6: those functions took no input and always did the identical thing.

**Positional vs keyword arguments.**
- Positional: `caesar(text, 3, "encode")` matches parameters by **order**. Get the order wrong and you pass the wrong value to the wrong slot, silently.
- Keyword: `caesar(start_text=text, shift_amount=3, direction="encode")` matches by **name**, so order doesn't matter and the call is self-documenting. Prefer keyword args when a function takes more than two inputs; it prevents the silent order-mix bug.

**How the Caesar cipher works (this course's approach).** Shift each letter forward by a fixed amount in the alphabet. This version uses a hardcoded `alphabet` list, not chr/ord:
- Find the letter's index in the list, add the shift, then look up the new letter.
- **Wrap with modulo:** `new_index = (index + shift) % 26`. Modulo gives the remainder, so when the index runs past 25 (z), it wraps back to the start. `27 % 26 == 1`. That is the whole trick to handling "x shifted by 3 = a".
- To decode, shift the other way (negative shift). Refactoring (Part 3) merges encode and decode into one function with a direction parameter, which is the day's real point: one function, two behaviors, chosen by an argument.

**Security-track note.** The Caesar cipher is the canonical "broken" cipher: only 25 possible keys, trivially brute-forced. It's the historical starting point for understanding why modern crypto needs huge keyspaces. Worth internalizing the *why it's weak*, since that intuition carries into your federal cyber track.

## The trap to remember (Anki this)

Modulo is what makes wrap-around work. `(24 + 3) % 26 == 1`, not 27. If your cipher crashes or produces garbage at the end of the alphabet, you forgot the `% 26`. Also: non-letters (spaces, punctuation) aren't in the alphabet list, so handle them by passing them through unchanged instead of trying to shift them.

## Concept gate (do before coding)

Watch 002 and 004. Then answer: in `caesar(start_text=text, shift_amount=5, direction="decode")`, which value lands in which parameter, and would it still work if you reordered the three keyword arguments? If you can't answer, the cipher will fight you. Reread first.

## Build spec

Done when: encode then decode the same message with the same shift returns the original text exactly, the alphabet wraps correctly past z, and spaces/punctuation survive unchanged. Test the wrap explicitly: encode "z" with shift 1 should give "a".
