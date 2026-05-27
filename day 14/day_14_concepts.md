# Day 14 Concepts: Higher Lower Game (Beginner Capstone)

No new syntax. Final beginner-phase capstone, integrating Days 1-13. Like Day 11, watch the requirements only and build from blank.

## Prerequisites (builds on)

Days 1-13, especially Day 9 (list of dicts), Day 10 (functions that return), and the Day 5 score-tracking pattern.

## Practice exercises (do these before the project)

No standalone exercises. The Higher Lower game is the exercise, built from the requirements video with a walkthrough as the answer key. Attempt from blank before opening the solution.

## The videos, distilled

| # | Video | Verdict | What it teaches |
|---|---|---|---|
| 001 | Introduction and Program Requirements | **WATCH** | The spec. All you watch first. |
| 002 | Solution and Walkthrough | answer key | Open only when stuck. |
| 003 | Study Tip: Calendar Reminders | SKIP | Filler (the tip: spaced review, which you already do in Anki). |

## How to do this day

Watch 001, then build cold. This is your second capstone, so it should feel less brutal than Blackjack if Days 1-13 stuck. If it feels impossible, that's a signal about which earlier concept didn't land, and that's useful information, not failure. Note which piece blocked you and review that day.

## The concepts in play (all already learned)

- A **list of dictionaries** for the account data (Day 9 nesting): `[{"name": ..., "follower_count": ...}, ...]`.
- `random.choice` to pick accounts (Day 4).
- A **function that returns** whether the guess was right (Day 10 return, not print).
- A **while loop** for the game continuing while correct (Day 6).
- A running **score** variable (Day 5 tracking pattern).

## The one design subtlety (think before coding)

After a correct guess, the account the player chose becomes the new "A" to compare against, and a fresh random "B" is drawn. So it's not two fresh accounts each round; the winner carries forward. Getting this wrong makes the game trivially easy or impossible. Also make sure the new B is never the same as the current A.

## The trap to remember (Anki this)

When B becomes the new A for the next round, you must reassign `account_a = account_b` *before* drawing a new B. Drawing B first and then reassigning loses the carry-forward. Small ordering bug, completely changes the game.

## Build spec

Done when: two accounts show with descriptions (counts hidden), the player guesses A or B, a correct guess increments score and carries the winner forward, a wrong guess ends the game and prints the final score, and the screen clears between rounds. Verify the carry-forward by winning several rounds in a row and checking that one account persists while the other refreshes.
