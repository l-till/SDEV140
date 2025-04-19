# m02_assn2_LT.py
# Logan Till
# 2025-03-28
# Add Up User Numbers
# No assistance was used in this program


# this will print the title of the program
print("***************************************")
print("Add Up User Numbers (by Logan Till)")
print("***************************************")
print("")

# this will print the welcome message
print("Welcome!")
print("This program will add inputs to give the total and average.")

# Variables
total = 0
entry_count = 0
prompt = "Please enter a number (or 'x' to finish): "

# this will ask the user for a number 
user_entry = input(prompt)

# this will check if the user entered 'x' to exit the loop
while user_entry != 'x':
    # this will add the number to the total
    total += float(user_entry)
    # this will increase the entry count
    entry_count += 1
    # this will ask the user for another number
    user_entry = input(prompt)
print("The sum is: ", total)
print("The average is: ", total / entry_count)

# this will print the goodbye message
print("")
print("Thank you for using this program.")