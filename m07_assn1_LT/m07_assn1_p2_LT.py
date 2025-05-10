# m07_assn1_p2_LT.py
# Logan Till
# 2025-05-02
# Employee/Worker Classes
# This program will practice the use of classes
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Employee/Worker Classes (by Logan Till)")
print("***************************************\n")

# Import Libraries
import random

# Input File
# Output File
# Constants
WELCOME = ('Welcome!\nThis program will get employee info.\n')
GOODBYE = ('Thank you for using this program!')

# Variables


# FUNCTIONS START HERE

# Employee class
class Employee:
   def __init__(self, name, employee_number):
      self.name = name
      self.employee_number = employee_number

# ProductionWorker subclass
class ProductionWorker(Employee):
   def __init__(self, name, employee_number, pay_rate, shift_number):
      super().__init__(name, employee_number)
      self.pay_rate = pay_rate
      self.shift_number = shift_number

   # This method returns a string representation of the ProductionWorker object
   # It allows me to print the object directly
   def __str__(self):
      shift = "Day" if self.shift_number == 1 else "Night"
      return (f"Name: {self.name}\n"
               f"Employee Number: {self.employee_number}\n"
               f"Pay Rate: {self.pay_rate:.2f}/hr\n"
               f"Shift: {shift}\n")

# Create an instance of the Employee class
def employee_instance():
   name = input("Enter the employee's name: ")
   employee_number = random.randint(1000, 9999)
   pay_rate = float(input("Enter the employee's pay rate: "))

   while True:
      try:
         shift_number = int(input("Enter the employee's shift number (1 for Day, 2 for Night): "))
         if shift_number in [1, 2]:
            break
         else:
            print("Invalid input. Please enter 1 for Day or 2 for Night.")
      except ValueError:
         print("Invalid input. Please enter a number (1 or 2).")
   
   # CodeAssist-AI: ChatGPT fixed this error where I used Employee instead of ProductionWorker
   worker = ProductionWorker(name, employee_number, pay_rate, shift_number)
   return worker
    
# Main Program
print(WELCOME)
worker = employee_instance()
print("\nEmployee Information:")
print(worker)
print(GOODBYE)