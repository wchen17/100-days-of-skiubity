# ============================================================
#  DAY 8 — Function Parameters & Caesar Cipher
#  PROJECT: Caesar Cipher Encoder/Decoder
# ============================================================
#
#  SKILLS TODAY:
#    - def func(param):         → function with a parameter
#    - def func(p1, p2, p3):    → multiple parameters
#    - Positional arguments     → order matters when calling
#    - Keyword arguments        → func(name="Alice") — order doesn't matter
#    - string.lower()           → normalise case
#    - chr() and ord()          → convert between char and ASCII number
#    - % (modulo)               → wrap numbers around (e.g. 26 % 26 == 0)
#
#  HOW CAESAR CIPHER WORKS:
#    Shift every letter by a fixed number of positions in the alphabet.
#    "abc" shifted by 3 → "def"
#    "xyz" shifted by 3 → "abc"  ← wraps around using modulo
#
# ============================================================

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

# --------------------------------------------------
#  TODO 1: Write the caesar() function
# --------------------------------------------------
# Parameters:
#   start_text  → the message to encode/decode
#   shift_amount → how many positions to shift
#   direction   → "encode" or "decode"
#
# Logic:
#   - If direction == "decode", flip the shift: shift_amount = -shift_amount
#   - Loop through each letter in start_text
#   - If the letter is in the alphabet:
#       find its index, add the shift, wrap with % 26
#       look up that index in alphabet → new letter
#   - If the letter is NOT in alphabet (space, punctuation, number):
#       keep it unchanged
#   - Print the final encoded/decoded string

def caesar(start_text, shift_amount, direction):
    pass  # TODO: implement the cipher logic


# --------------------------------------------------
#  TODO 2: Build the game loop
# --------------------------------------------------
# Ask: "Type 'encode' to encrypt, 'decode' to decrypt: "
# Ask: "Type your message: "   (lower-case it)
# Ask: "Type the shift number: "  (int)
# Call caesar() with those three values
# Ask: "Go again? yes or no: "
# Loop while they say yes

should_continue = True
while should_continue:
    direction  = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text       = input("Type your message:\n").lower()
    shift      = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, direction=direction)

    restart = input("Type 'yes' if you want to go again, 'no' to quit:\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Make the cipher work with UPPER-CASE letters too
#  2. Support numbers in the cipher (shift 0-9 by shift_amount % 10)
#  3. Add a "brute force" mode: try all 26 shifts and print them all
#     so the user can spot which one looks like real text
# ============================================================
