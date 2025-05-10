# m07_assn1_p2_LT.py
# Logan Till
# 2025-05-02
# Person/Customer Classes
# This program will practice the use of classes
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Person/Customer Classes (by Logan Till)")
print("***************************************\n")

# Import Libraries
import random

# Input File
# Output File
# Constants
WELCOME = ('Welcome!\nThis program will get a customers info.\n')
GOODBYE = ('Thank you for using this program!')

# Variables


# FUNCTIONS START HERE

# Part 1: person class
class Person:
   def __init__(self, name, address, phone):
      self.name = name
      self.address = address
      self.phone = phone

# Part 2: customer subclass
class Customer(Person):
   def __init__(self, name, address, phone, customer_number, mailing_list):
      super().__init__(name, address, phone)
      self.customer_number = customer_number
      self.mailing_list = mailing_list

   # CodeAssist-AI: I was missing this part. ChatGPT fixed it.
   # This method returns a string representation of the Customer object
   # It allows me to print the object directly
   def __str__(self):
      return (f"Name: {self.name}\n"
               f"Address: {self.address}\n"
               f"Phone: {self.phone}\n"
               f"Customer Number: {self.customer_number}\n"
               f"Mailing List: {'Yes' if self.mailing_list else 'No'}")

# Create an instance of the Customer class
def customer_instance():
   name = input("Enter the customer's name: ")
   address = input("Enter the customer's address: ")
   phone = input("Enter the customer's phone number: ")
   customer_number = random.randint(1000, 9999)
   mailing_list_ask = input("Subscribe to the mailing list? (y/n): ")
   mailing_list = True if mailing_list_ask.lower() == 'y' else False
   customer = Customer(name, address, phone, customer_number, mailing_list)
   return customer
    
# Main Program
print(WELCOME)
customer = customer_instance()
print("\nCustomer Information:")
print(customer)
print(GOODBYE)