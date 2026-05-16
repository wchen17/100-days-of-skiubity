print("Tippy calc")

cost = input("whats the cost of the bill?\n")

tip_percent = input("how much percent you want to tip?\n 10, 12, or 15\n")

people = input("how many people to split the bill?\n")

tip_as_percent = float(tip_percent) / 100

tip_amount = float(cost) * tip_as_percent

total_bill = float(cost) + tip_amount

bill_per_person = total_bill / int(people)

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")