# ============================================================
#  DAY 16 — Object-Oriented Programming
#  PROJECT: OOP Concepts + Coffee Machine (OOP version begins)
# ============================================================
#
#  SKILLS TODAY:
#    - class ClassName:           → blueprint for objects
#    - def __init__(self, ...):   → constructor / setup
#    - self.attribute = value     → instance attribute
#    - def method(self):          → function belonging to the class
#    - object = ClassName(args)   → create an instance
#    - object.attribute           → access attribute
#    - object.method()            → call a method
#
#  KEY IDEA:
#    A class bundles DATA (attributes) and BEHAVIOUR (methods) together.
#    Every object made from the class gets its own copy of the data.
#
# ============================================================

# --------------------------------------------------
#  DEMO 1: A simple class
# --------------------------------------------------
class Dog:
    # __init__ runs automatically when you create a Dog object
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age  = age

    def bark(self):
        print(f"{self.name} says: Woof!")

    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")

# Create instances
dog1 = Dog("Rex", 3)
dog2 = Dog("Bella", 5)

dog1.bark()
dog2.birthday()
print(dog1.age)   # 3 — dog1 is unaffected by dog2's birthday


# --------------------------------------------------
#  TODO 1: Create a Car class
# --------------------------------------------------
# Attributes:  make, model, year, speed (starts at 0)
# Methods:
#   accelerate(amount) → increase speed by amount, print new speed
#   brake(amount)      → decrease speed by amount (don't go below 0)
#   describe()         → print "{year} {make} {model}"

class Car:
    def __init__(self, make, model, year):
        pass  # TODO: set up attributes

    def accelerate(self, amount):
        pass

    def brake(self, amount):
        pass

    def describe(self):
        pass

# Test your Car:
my_car = Car("Toyota", "Supra", 1998)
my_car.describe()
my_car.accelerate(30)
my_car.accelerate(20)
my_car.brake(10)


# --------------------------------------------------
#  TODO 2: Create a BankAccount class
# --------------------------------------------------
# Attributes: owner (str), balance (float, default 0)
# Methods:
#   deposit(amount)    → add to balance, print new balance
#   withdraw(amount)   → subtract if funds available, else print error
#   get_balance()      → print "Balance: ${balance}"

class BankAccount:
    def __init__(self, owner, balance=0):
        pass

# Test:
account = BankAccount("Wendy", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(200)   # should print an error
account.get_balance()


# ============================================================
#  STRETCH GOALS
# ============================================================
#  1. Add a transfer(amount, other_account) method to BankAccount
#  2. Add a __str__ method to both classes so print(obj) shows something nice
#  3. Rewrite your Day 15 coffee machine using a CoffeeMachine class
# ============================================================
