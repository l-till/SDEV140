# m05_assn1_LT.py
# Logan Till
# 2025-04-18
# Tie Dye Kiosk
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Tie Dye Kiosk (by Logan Till)")
print("***************************************\n")

# Import Libraries

# Input File

# Output File

# Constants
COLOR_OPTIONS = [
   'red', 'blue', 'green', 'purple', 'orange',
   'yellow', 'pink', 'lime', 'goldenrod', 'olive',
   'brown', 'lilac'
]

# Variables
welcome = ('Welcome!\nThis program will design a tie dye shirt.\n')
goodbye = ('Thank you for using this program!')
prompt = ('Please enter the number of a color or x to quit: ')

# FUNCTIONS START HERE

# This function greets the user
def greeting():
   print(welcome)
   print("Available colors:")
   # CodingAssist-AI: DeepSeek taught me the enumerate function
   for i, color in enumerate(COLOR_OPTIONS, start=1):
      print(f"{i}- {color}")

# This function will print the color options and ask for a choice
def color_choice():

   # This while loop will check if the user is inputting a number or 'x'
   while True:
      user_input = input(prompt)
      if user_input.lower() == 'x':
         return None
      
      # this will check if the user is inputting a number
      # CodingAssist-AI: DeepSeek helped with this code
         # To be fair, it made it worse and I had to fix it
      try:
         choice = int(user_input)
         if 1 <= choice <= len(COLOR_OPTIONS):
            return COLOR_OPTIONS[choice - 1]
         print(prompt)
      except ValueError:
         print("Invalid input.")

# PROGRAM STARTS HERE

# Welcome the user
greeting()

while True:
   selected_colors = []

   # This while loop will make sure the user selects at least 2 colors
   # CodingAssist-AI: Copilot debugged this code
   while selected_colors != None:
      color = color_choice()
      if color is None:
         if len(selected_colors) < 2:
            print("You must select at least two colors.")
            continue
         else:
            break
      
      # This will keep track of the selected colors
      selected_colors.append(color)
      print(f"You selected: {color}")
      print(f"Current colors: {', '.join(selected_colors)}")
   
   # this will check if the user wants to do another
   restart = input("\nWould you like to restart? (y or n): ").lower()
   if restart != 'y':
        break


# This will print the goodbye message
print(goodbye)