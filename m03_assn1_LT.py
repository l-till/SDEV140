# m03_assn1_LT.py
# Logan Till
# 2025-04-06
# Write Random Numbers to a File
# Coding assistance was used in this program


# this will print the title of the program
print("***************************************")
print("Print Random Numbers (by Logan Till)")
print("***************************************")
print("")

# this will print the welcome message
print("Welcome!")
print("This program will print random numbers to a file.")

# Import Libraries
import random

# Output File
FILE_NAME = "LT_random_numbers.rtf"

# Constants

# Variables
numbers = []
total = 0
average = 0
num = 0
num_count = 0


# Write 100-200 random 3-digit numbers to file
# CodingAssist-AI: AI helped me understand how to generate random numbers and write them to a file.
# Ai explained the use of with open() and that the file will be closed automatically.
num_count = random.randint(100, 200)
with open(FILE_NAME, 'w') as file:
    for _ in range(num_count):
        num = random.randint(100, 999)
        file.write(f"{num}\n")

# Read and analyze the numbers
with open(FILE_NAME, 'r') as file:
    for line in file:
        numbers.append(int(line.strip()))

# Calculate statistics
total = sum(numbers)
average = total / num_count

# Display results
print("Output File: ", FILE_NAME)
print(f"Total lines input: {len(numbers)}")
print(f"Total of all numbers: {total}")
print(f"Highest value: {max(numbers)}")
print(f"Lowest value: {min(numbers)}")
print(f"Average value: {average:.2f}")

# this will print the goodbye message
print("")
print("Thank you for using this program.")