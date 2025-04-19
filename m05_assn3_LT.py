# m05_assn3_LT.py
# Logan Till
# 2025-04-19
# Monthly tax calculator
# This program will generate a lottery ticket
# No coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Monthly Tax Calculator (by Logan Till)")
print("***************************************\n")

# Import Libraries

# Input File

# Output File

# Constants
WELCOME = ('Welcome!\nThis program will Calcualte Monthly Tax.\n')
GOODBYE = ('Thank you for using this program!')
SALES_PROMPT = ('Please enter the monthly sales: ')
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Variables
total_sales = 0
state_tax = 0
county_tax = 0
total_tax = 0

# FUNCTIONS START HERE

# This function greets the user
def greeting():
   print(WELCOME)

# This function gets the monthly sales
def get_monthly_sales():
   while True:
       try:
           monthly_sales = input('Please enter the monthly sales: ')
           if float(monthly_sales) < 0:
               print("Sales cannot be negative. Please try again.")
               continue
           break
       except ValueError:
           print("Invalid input. Please enter a numeric value.")
   global total_sales
   total_sales = float(monthly_sales)
   return total_sales

# This function calculates the tax
def calculate_taxes(total_sales):
   global state_tax
   global county_tax
   global total_tax
   state_tax = total_sales * STATE_TAX_RATE
   county_tax = total_sales * COUNTY_TAX_RATE
   total_tax = state_tax + county_tax

# This function displays the results
def display_results(total_sales, state_tax, county_tax, total_tax):
   print('The total sales are: $', format(total_sales, '.2f'))
   print('The state tax is: $', format(state_tax, '.2f'))
   print('The county tax is: $', format(county_tax, '.2f'))
   print('The total tax is: $', format(total_tax, '.2f'))

# This runs the program
greeting()
get_monthly_sales()
calculate_taxes(total_sales)
display_results(total_sales, state_tax, county_tax, total_tax)

# This will print the goodbye message
print(GOODBYE)
