# ============================================================
#  DAY 15: Local Dev Environment & Procedural Programming
#  PROJECT: Coffee Machine (procedural version)
# ============================================================
#
#  SKILLS TODAY:
#    - Running Python locally (not in a browser REPL)
#    - Breaking a big problem into small functions
#    - Nested dictionaries as a data store
#    - while True / break pattern for a menu loop
#
#  MACHINE RESOURCES:
#    water (ml), milk (ml), coffee (g), money ($)
#
#  DRINKS MENU:
#    espresso  → 50ml water, 0ml milk, 18g coffee  → $1.50
#    latte     → 200ml water, 150ml milk, 24g coffee → $2.50
#    cappuccino→ 250ml water, 100ml milk, 24g coffee → $3.00
#
# ============================================================

MENU = {
    "espresso": {"ingredients": {"water": 50,  "milk": 0,   "coffee": 18}, "cost": 1.50},
    "latte":    {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.50},
    "cappuccino":{"ingredients":{"water": 250, "milk": 100, "coffee": 24}, "cost": 3.00},
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}


# --------------------------------------------------
#  TODO 1: is_resource_sufficient(order_ingredients)
# --------------------------------------------------
# Loop through each ingredient in order_ingredients
# If resources[ingredient] < order_ingredients[ingredient]:
#   print "Sorry there is not enough {ingredient}."
#   return False
# return True

def is_resource_sufficient(order_ingredients):
    pass


# --------------------------------------------------
#  TODO 2: process_coins() → returns total value inserted
# --------------------------------------------------
# Ask how many quarters (0.25), dimes (0.10), nickles (0.05), pennies (0.01)
# Return total as a float

def process_coins():
    print("Please insert coins.")
    pass


# --------------------------------------------------
#  TODO 3: is_transaction_successful(money_received, drink_cost)
# --------------------------------------------------
# If money_received >= drink_cost:
#   add profit to resources["money"]
#   calculate change and print it
#   return True
# Else:
#   print "Sorry that's not enough money. Money refunded."
#   return False

def is_transaction_successful(money_received, drink_cost):
    pass


# --------------------------------------------------
#  TODO 4: make_coffee(drink_name, order_ingredients)
# --------------------------------------------------
# Deduct each ingredient from resources
# Print "Here is your {drink_name} ☕. Enjoy!"

def make_coffee(drink_name, order_ingredients):
    pass


# --------------------------------------------------
#  TODO 5: Main loop
# --------------------------------------------------
# Print "What would you like? (espresso/latte/cappuccino): "
# If "report" → print current resources
# If "off"    → break (turn off the machine)
# Otherwise:
#   get drink from MENU
#   check resources → if not sufficient, loop again
#   process coins
#   check transaction → if not enough, loop again
#   make the coffee

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    pass  # TODO: handle choice


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Rewrite this tomorrow as a CoffeeMachine class (Day 16!)
#  2. Save the money total to a file so it persists between runs
#  3. Add a maintenance mode that refills resources
# ============================================================
