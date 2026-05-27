# ============================================================
#  DAY 9: Dictionaries & Nesting
#  PROJECT: Secret Auction
# ============================================================
#
#  SKILLS TODAY:
#    - {key: value}             → create a dictionary
#    - dict[key]                → access a value
#    - dict[key] = value        → add or update an entry
#    - dict.items()             → loop through key-value pairs
#    - Nesting: dict inside dict, list inside dict
#    - for key, value in dict.items():
#
# ============================================================

print("Welcome to the secret auction program.")

bids = {}   # will store  { "Name": bid_amount, ... }

bidding_finished = False

# --------------------------------------------------
#  TODO 1: Collect bids in a loop
# --------------------------------------------------
# Ask: "What is your name?: "
# Ask: "What is your bid?: $"  (convert to int/float)
# Store in bids dict as  bids[name] = bid
# Ask: "Are there any other bidders? Type 'yes' or 'no': "
# If "no" → set bidding_finished = True to exit the loop
# If "yes" → clear the screen so bids stay secret
#   hint: print("\n" * 20)

while not bidding_finished:
    pass  # TODO: replace with your bid-collection logic


# --------------------------------------------------
#  TODO 2: Find the winner
# --------------------------------------------------
# Write a function find_highest_bidder(bidding_record)
# It should:
#   - Loop through bidding_record.items()
#   - Track the highest bid and who made it
#   - Print "The winner is {name} with a bid of ${amount}"

def find_highest_bidder(bidding_record):
    pass  # TODO: implement

find_highest_bidder(bids)


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Store each bid as a dict itself:
#       bids[name] = {"bid": amount, "email": email}
#  2. Handle ties: what if two people bid the same highest amount?
#  3. Show a sorted leaderboard of all bids after the winner
# ============================================================
