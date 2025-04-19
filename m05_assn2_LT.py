# m05_assn2_LT.py
# Logan Till
# 2025-04-18
# Lottery Ticket Generator
# This program will generate a lottery ticket
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Lottery Ticket Generator (by Logan Till)")
print("***************************************\n")

# Import Libraries
import random

# Input File

# Output File

# Constants
WELCOME = ('Welcome!\nThis program will generate lottery tickets.\n')
GOODBYE = ('Thank you, {}, for using this program!')
EMAIL_PROMPT = ('Please enter your email address: ')
NAME_PROMPT = ('Please enter your name: ')
HOW_MANY_PROMPT = ('How many tickets would you like to generate, {}?: ')
SUPER_PROMPT = ('Would you like to play Super Lotto for $1? (y or n): ')
CONTINUE_PROMPT = ('Would you like more tickets? (y or n): ')
REGULAR_PRICE = 2
SUPER_PRICE = 3

# Variables
email = ''
name = ''
total_tickets = 0
super_lotto = False
total_cost = 0

# FUNCTIONS START HERE

# This function greets the user
def greeting():
   print(WELCOME)

# This function will get the user's name
def get_name():
   name = input(NAME_PROMPT).strip()
   return name

# This function will get the user's email
def get_email():
   email = input(EMAIL_PROMPT).strip()
   return email

# This function will get the number of tickets
def get_ticket_count(name):
   while True:
      count = input(HOW_MANY_PROMPT.format(name))
      try:
         if int(count) > 0:
            return int(count)
      except ValueError:
         print("Invalid input. Please enter a positive number.")

# This function will ask the user if they want to play Super Lotto
def play_super_lotto():
   while True:
      play_super = input(SUPER_PROMPT).lower()
      if play_super == 'y':
         return True
      elif play_super == 'n':
         return False
      else:
         print("Invalid input. Please enter 'y' or 'n'.")

# This function will gather ticket information from the user
# CodeAssistAI: ChatGPT debugged this function
def generate_tickets(play_super):
   numbers = sorted(random.sample(range(1, 60), 6))
   ticket = "\t" + " ".join(f"{num:2d}" for num in numbers)
   price = SUPER_PRICE if play_super else REGULAR_PRICE
   return f"{ticket}\t${price}" + (" (Super Lotto)" if play_super else "")

# This function will calculate the total cost of the tickets
def calculate_total_cost(ticket_count, play_super):
   global total_cost
   if play_super:
      total_cost += int(ticket_count) * SUPER_PRICE
   else:
      total_cost += int(ticket_count) * REGULAR_PRICE      


# PROGRAM STARTS HERE

# Welcome the user
greeting()

email = get_email()
name = get_name()

while True:
   ticket_count = get_ticket_count(name)
   super_lotto = play_super_lotto()

   for _ in range(ticket_count):
      print(generate_tickets(super_lotto))
      total_tickets += 1
   calculate_total_cost(ticket_count, super_lotto)
   
   # this will check if the user wants to do another ticket
   if input(CONTINUE_PROMPT) != 'y':
      break

#This will print the totals
print(f"Total tickets: {total_tickets}")
print(f"Total cost: ${total_cost:.2f}")

# This will print the goodbye message
print(GOODBYE.format(name))
