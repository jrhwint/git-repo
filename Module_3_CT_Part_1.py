# Module 3 Part 1

# ask for user to input food_cost
food_charge = float(input("Enter the food charge: "))

# print food charge
print(f"The food charge is: ${food_charge}.")

tip = round(food_charge * 0.18, 2)
# round to 2 decimals
print(f"The tip is: ${tip}.")

tax = round(food_charge * 0.07, 2)
# round to 2 decimals
print(f"The tax is: ${tax}.")

meal_total = round(food_charge + tip + tax, 2)
# round to 2 decimals

# print meal_total
print(f"The total amount of the meal is: ${meal_total}.")




