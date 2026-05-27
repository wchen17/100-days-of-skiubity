# ============================================================
#  DAY 83: Portfolio Project
#  PROJECT: Tic-Tac-Toe with an AI opponent
# ============================================================
#
#  SKILLS USED: OOP, 2D lists, recursion, minimax algorithm
#
#  REQUIREMENTS:
#    - Play on a 3×3 grid
#    - Human vs AI (computer plays perfectly using minimax)
#    - Display the board after each move
#    - Detect win, loss, and draw
#    - Allow the human to choose X or O
#
# ============================================================

import math

# Board: 3x3 grid, cells are " ", "X", or "O"
board = [[" " for _ in range(3)] for _ in range(3)]


def print_board(b):
    print()
    for i, row in enumerate(b):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)
    print()


def check_winner(b, player):
    # Check rows, columns, diagonals
    for row in b:
        if all(c == player for c in row):
            return True
    for col in range(3):
        if all(b[row][col] == player for row in range(3)):
            return True
    if all(b[i][i] == player for i in range(3)):
        return True
    if all(b[i][2-i] == player for i in range(3)):
        return True
    return False


def is_full(b):
    return all(cell != " " for row in b for cell in row)


# --------------------------------------------------
#  TODO 1: minimax(board, is_maximising) → int score
# --------------------------------------------------
# Base cases:
#   AI wins   → return +10
#   Human wins → return -10
#   Draw       → return 0
# Recursive case:
#   If maximising (AI's turn):
#     Try every empty cell, recurse, return the max score
#   If minimising (human's turn):
#     Try every empty cell, recurse, return the min score
#
# This lets the AI pick the move that maximises its score
# (or minimises human's score)

def minimax(b, is_maximising, ai, human):
    if check_winner(b, ai):
        return 10
    if check_winner(b, human):
        return -10
    if is_full(b):
        return 0

    if is_maximising:
        best = -math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == " ":
                    b[r][c] = ai
                    score = minimax(b, False, ai, human)
                    b[r][c] = " "
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for r in range(3):
            for c in range(3):
                if b[r][c] == " ":
                    b[r][c] = human
                    score = minimax(b, True, ai, human)
                    b[r][c] = " "
                    best = min(best, score)
        return best


# --------------------------------------------------
#  TODO 2: best_move(board, ai, human) → (row, col)
# --------------------------------------------------
# Try every empty cell, run minimax, return the move with highest score

def best_move(b, ai, human):
    best_score = -math.inf
    move       = None
    for r in range(3):
        for c in range(3):
            if b[r][c] == " ":
                b[r][c] = ai
                score   = minimax(b, False, ai, human)
                b[r][c] = " "
                if score > best_score:
                    best_score = score
                    move       = (r, c)
    return move


# --------------------------------------------------
#  TODO 3: Main game loop
# --------------------------------------------------
def play():
    human = input("Do you want to be X or O? ").upper()
    ai    = "O" if human == "X" else "X"
    print(f"You are {human}, AI is {ai}")
    print_board(board)

    turn = "X"   # X always goes first
    while True:
        if turn == human:
            try:
                row = int(input("Row (0-2): "))
                col = int(input("Col (0-2): "))
                if board[row][col] != " ":
                    print("Cell taken, try again.")
                    continue
                board[row][col] = human
            except (ValueError, IndexError):
                print("Invalid input.")
                continue
        else:
            print("AI is thinking...")
            r, c = best_move(board, ai, human)
            board[r][c] = ai
            print(f"AI played at ({r}, {c})")

        print_board(board)

        if check_winner(board, turn):
            print("You win!" if turn == human else "AI wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        turn = "O" if turn == "X" else "X"

play()
