# m03_assn3_LT.py
# Logan Till
# 2025-04-07
# Debug Code
# No coding assistance was used in this program

# Issue0: Corrected the header
# Date: 1-1-05
# Name: Frank Sinatra
# IDE:  VS Code

# Pseudo-code:
# 1. Take a user order for flowers

# Issue1: Capitalization of the constant name END_VALUE
# Define constants
DISCOUNT = .05
PROMPT0 = "Enter your items one at a time, enter 'done' to check out."
# Issue5: Changed the prompt to be more user-friendly
PROMPT1 = "Please enter an item or 'done' to check out: "
PROMPT2 = "Please enter the price: "
END_VALUE = "done"

# Issue2: The variable item_name was moved to varables and corrected
# Issue7: initialized variable price
# Initialize variables
item_name = ""
item_count = 0
price = 0
total_price = 0
discount_price = 0
final_price = 0

# Issue3: Adjusted the print statement to use f-string formatting and use 1 line
# banner and first prompt
print(f"\n{PROMPT0}\n");

# Issue4: corrected Variable names and added spaces for readability
# Issue8: adjusted end value check to be case insensitive
# Issue9: added item count
# Take input until user is finished
while item_name.lower() != END_VALUE:
    item_name = input(PROMPT1)
    if (item_name != END_VALUE):
        str_price = input(PROMPT2)
        if (str_price > ""):
            price = float(str_price)
            total_price += price
            item_count += 1
            print (f"last item: {item_name} {price:.2f}")

# Issue10: print item count
print (f"Your total order: {item_count} items");

# Total
print (f"Total price: {total_price:.2f}");

# Discount_price
# Issue11: added the discount calculation
discount_price = total_price * DISCOUNT

# Issue12: Print the discount amount
# Discount amt
print (f"Discount price: {discount_price:.2f}");

# Issue13: added the final price calculation
# Final price
final_price = total_price - discount_price

# Issue14: Print the final price amount
# Final price amount
print (f"Final price: {final_price:.2f}");

# Issue6: Removed random lines of code from previous assignment