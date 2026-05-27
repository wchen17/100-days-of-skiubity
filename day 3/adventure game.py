# ============================================================
#  DAY 3 ASSIGNMENT: If / Elif / Else  (Adventure Game)
# ============================================================
#
#  WHAT YOU'RE LEARNING TODAY:
#    if   → "only do this when the condition is True"
#    elif → "otherwise, check THIS condition next"
#    else → "if nothing above matched, do this instead"
#
#  NESTING: you can put an if/else INSIDE another if/else block.
#  Indentation (spaces) is what tells Python "this belongs inside that".
#
#  WHY AN ADVENTURE GAME?
#    Every choice the player makes is just an if/elif/else chain.
#    Your meme RPG is built on thousands of these: this is that concept
#    stripped down so you can *see* the skeleton before the muscle goes on.
#
#  GOAL: finish the TODOs so the game has at least 2 full story branches,
#        each with a nested choice that leads to different outcomes.
#
# ============================================================

print("You wake up in a dark dungeon. Typical.")
print("Ahead you see two paths:")
print("  1 - A glowing blue door")
print("  2 - A suspiciously normal-looking door")

first_choice = input("\nWhich door do you choose? (1 or 2): ")

# --------------------------------------------------
#  BRANCH A : the blue door
# --------------------------------------------------
if first_choice == "1":
    print("\nYou push open the glowing blue door.")
    print("Inside is a weird-looking merchant.")
    print("He says: 'Trade me your shoe and I'll give you a sword.'")
    print("  y - Trade the shoe")
    print("  n - Keep the shoe and back away slowly")

    trade_choice = input("\nWhat do you do? (y or n): ")
    if trade_choice == "y":
        print("The sword is yours")
    else:
        print("oh well, maybe next time")
    # TODO: write the if/else for the trade choice
    # ----------
    # if trade_choice == "y":
    #     print out what happens when you trade: do you get the sword?
    #     does something go wrong? You decide the outcome.
    # else:
    #     print out what happens when you refuse:
    #     does the merchant get mad? Do you find another item?
    # ----------


# --------------------------------------------------
#  BRANCH B : the normal-looking door
# --------------------------------------------------
elif first_choice == "2":
    print("\nYou open the suspiciously normal door.")
    print("It leads outside. There's a goblin sitting on a rock eating lunch.")
    print("He looks up at you.")
    print("  1 - Try to sneak past him")
    print("  2 - Challenge him to a battle")
    print("  3 - Ask if you can have some of his lunch")

    goblin_choice = input("\nWhat do you do? (1, 2, or 3): ")
    if goblin_choice == "1":
        print("The goblin didnt see you at all!")
    elif goblin_choice == "2":
        print("The gayblin is mad now...")
        weapon = input("do you take out your weapon? (y/n)")
        if weapon == "y":
            print("the gayblin respectfully makes way for you")
        else:
            print("the goblin smashes with his rock smashing sword, you lose")
    elif goblin_choice == "3":
        print("No problem polite human!")

    # TODO: write the if / elif / else for the goblin choice
    # ----------
    # Handle all 3 options (1, 2, 3) with if / elif / elif.
    # Add an else at the end for any other input (invalid choice).
    # At least one of the branches should have a NESTED if/else inside it.
    # Example: if they fight (choice 2), ask "do you have a weapon?" (y/n)
    #          and print different results based on that answer.
    # ----------


# --------------------------------------------------
#  CATCH-ALL : player typed something unexpected
# --------------------------------------------------
else:
    print("uhhh, you cant do that.")
    # TODO: handle invalid input for the first choice
    # ----------
    # print a message telling the player the input wasn't valid.
    # ----------
  # delete this 'pass' once you fill in the block above


# ============================================================
#  STRETCH GOALS (optional, do these if you finish early)
# ============================================================
#
#  1. Add a third door / branch entirely.
#
#  2. Give the player a "health" variable that starts at 100.
#     Subtract HP on bad choices, add HP on good ones.
#     Print their health at the end.
#     Use an if/else at the very end:
#       if hp > 0:  → "You survived!"
#       else:       → "You died. Skill issue."
#
#  3. Add at least one check using "and" or "or":
#       if choice == "2" and has_weapon:
#
# ============================================================
