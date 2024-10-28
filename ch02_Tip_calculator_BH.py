# Brian Herrera
# Tip Calculator
# 08/23/2024
# Calculates and displays total after tip from a meal at a restaurant.

cost_of_meal = float(input("Enter Cost of Meal: "))
tip_percent = int(input("Enter Tip Percent: "))
tip = cost_of_meal *(tip_percent /100)
total = tip + cost_of_meal

print("Tip amount: ", round(tip,2))
print("Total amount: ", round(total,2))
