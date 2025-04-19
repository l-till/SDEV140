# m02_assn1_LT.py
# Logan Till
# 2025-03-28
# Tax and Tip Calculator
# assistance was used in this program


# this will print the title of the program
print("***************************************")
print("Tax and Tip Calculator (by Logan Till)")
print("***************************************")
print("")

# this will print the welcome message
print("Welcome!")
print("This program will calculate your tax and tip on a meal.")

# this will ask the user for the meal cost
cost = input("Please enter the cost of your meal (xxx.xx): ")


# this section decalres the constants
tip_pct = 0.18
tax_rate = 0.07

# this will convert the cost to a float
meal_cost = float(cost)
tip = meal_cost * tip_pct
tax = meal_cost * tax_rate
total = meal_cost + tip + tax

# this will print the amounts
# CodeAssist-AI: ChatpGPT showed me to use the .2f format to round the numbers to 2 decimal places
print(f'Meal cost: {cost}')
print(f'...Tip: {tip:.2f}')
print(f'...Tax: {tax:.2f}')
print(f'Total: {total:.2f}')

# this will print the goodbye message
print("")
print("Thank you for using this program.")