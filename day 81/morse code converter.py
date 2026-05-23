# ============================================================
#  DAY 81 — Portfolio Project
#  PROJECT: Text to Morse Code Converter (CLI tool)
# ============================================================
#
#  SKILLS USED: dicts, string manipulation, file I/O, CLI args
#
#  REQUIREMENTS:
#    - Convert plain text to Morse code (dots and dashes)
#    - Convert Morse code back to plain text
#    - Accept input from command line args OR interactive prompt
#    - Save output to a file optionally
#    - Support letters A-Z, digits 0-9, and common punctuation
#
# ============================================================

import sys

MORSE_CODE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',  'J': '.---',
    'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',  'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...', 'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-','Y': '-.--',
    'Z': '--..',
    '0': '-----','1': '.----','2': '..---','3': '...--','4': '....-',
    '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', ' ': '/',
}

# Reverse the dictionary for decoding
REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}


# --------------------------------------------------
#  TODO 1: encode(text) → Morse string
# --------------------------------------------------
# Convert each character to its Morse code (skip unknown chars)
# Separate letters with a space, words with " / "

def encode(text):
    pass   # TODO


# --------------------------------------------------
#  TODO 2: decode(morse) → plain text
# --------------------------------------------------
# Split on " / " to get words
# Split each word on " " to get letter codes
# Look up each code in REVERSE_MORSE

def decode(morse):
    pass   # TODO


# --------------------------------------------------
#  TODO 3: CLI interface
# --------------------------------------------------
# If called with args: python morse.py encode "Hello World"
#                  or: python morse.py decode ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
# If no args: show interactive menu

def main():
    if len(sys.argv) == 3:
        mode  = sys.argv[1].lower()
        text  = sys.argv[2]
        if mode == "encode":
            print(encode(text))
        elif mode == "decode":
            print(decode(text))
    else:
        print("Morse Code Converter")
        print("1. Encode text to Morse")
        print("2. Decode Morse to text")
        choice = input("Choose (1/2): ")
        if choice == "1":
            text = input("Enter text: ")
            result = encode(text)
            print(f"Morse: {result}")
        elif choice == "2":
            morse = input("Enter Morse (separate letters with space, words with /): ")
            result = decode(morse)
            print(f"Text: {result}")

main()
