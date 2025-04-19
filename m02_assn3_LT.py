# m02_assn3_LT.py
# Logan Till
# 2025-03-29
# Calculate Loan Payments
# Coding assistance was used in this program


# this will print the title of the program
print("***************************************")
print("Calculate Loan Payments (by Logan Till)")
print("***************************************")
print("")

# this will print the welcome message
print("Welcome!")
print("This program will Calculate Your Loan Payments.")

# Constants
DOWN_PAYMENT_PCT = 0.10
ANNUAL_INTEREST_RATE = 0.12
PAYMENT_RATE = 0.05

# Variables
months = 0
balance_owed = 0
total_payments = 0
total_interest = 0
prompt = "Please enter a loan amount (xxxxx.xx): "

# this will ask the user for a loan amount
loan_amount = float(input(prompt))

# calculate starting values
down_payment = loan_amount * DOWN_PAYMENT_PCT
starting_balance = loan_amount - down_payment
balance_owed = starting_balance
payment_amount = starting_balance * PAYMENT_RATE
monthly_interest_rate = (ANNUAL_INTEREST_RATE / 12)
interest = balance_owed * monthly_interest_rate

# this will print the amounts overview
print(f"Loan Amount: {loan_amount:.2f}")
print(f"Down Payment: {down_payment:.2f}")
print(f"Starting Balance: {starting_balance:.2f}")
print(f"Monthly Payment: {payment_amount:.2f}")
print(f"Monthly Interest Rate: {monthly_interest_rate:.2f}")

# this will print the header for the payment schedule
print(f"{'Month':<6} {'Payment':>10} {'Interest':>10} {'Principal':>10} {'Balance':>10}")

# this will check if the balance owed is greater than 0
# CodingAssist-AI: ChatGPT helped fix an issue where my final payment was not being calculated correctly.
while balance_owed > 0:
    interest = balance_owed * monthly_interest_rate
    principle = payment_amount - interest
    
    # this will handle the the final payment
    if balance_owed < payment_amount:
       payment_amount = balance_owed + interest
       principle = balance_owed

    # this will update the totals
    balance_owed -= principle
    total_interest += interest
    months += 1
   
    # this will print the payment schedule
    print(f"{months:<6} {payment_amount:>10.2f} {interest:>10.2f} {principle:>10.2f} {balance_owed:>10.2f}")
    
# this will calculate the total payments
total_payments = loan_amount + total_interest

# this will print the number of payments, total payments, and total interest
print(f"Number of Payments: {months}")
print(f"Total Interest: {total_interest:.2f}")
print(f"Total Payments: {total_payments:.2f}")


# this will print the goodbye message
print("")
print("Thank you for using this program.")