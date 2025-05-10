# m07_assn1_LT.py
# Logan Till
# 2025-04-19
# Fahrenheit/Celsius Converter
# This program will convert Fahrenheit to Celsius and vice versa
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Fahrenheit/Celsius Converter (by Logan Till)")
print("***************************************\n")

# Import Libraries
import tkinter as tk
from tkinter import ttk

# Input File
# Output File
# Constants

# Variables
celcius = 0
fahrenheit = 0

# FUNCTIONS START HERE
# This function converts Fahrenheit to Celsius
def convert_to_fahrenheit():
   celsius = float(entry_temp.get())
   fahrenheit = (celsius * 9/5) + 32
   result.config(text=f"{celsius}° Celsius is {fahrenheit:.2f}° Fahrenheit")

# Function to convert Fahrenheit to Celsius
def convert_to_celsius():
   fahrenheit = float(entry_temp.get())
   celsius = (fahrenheit - 32) * 5/9
   result.config(text=f"{fahrenheit}° Fahrenheit is {celsius:.2f}° Celsius")

# CodingAssist-AI: GPT helped to create the Tkinter GUI
# Tkinter starts here
# This creates the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="lightblue")

# This will style the widgets
style = ttk.Style()
font_style = ('Arial', 12)
style.configure("TButton", font=font_style, padding=10)
style.configure("TLabel", font=font_style)
style.configure("TEntry", font=font_style, padding=5)

# This creates the main frame
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# This creates the temperature entry messasge
enter_msg = ttk.Label(main_frame, text="Enter temperature:")
enter_msg.grid(row=1, column=0, columnspan=3, pady=10)

# This takes the temperature input
entry_temp = ttk.Entry(main_frame, width=20)
entry_temp.grid(row=2, column=0, columnspan=3, pady=5)

# This creates the convert messsage
convert_msg = ttk.Label(main_frame, text="Convert to:")
convert_msg.grid(row=3, column=0, columnspan=3, pady=(20, 5))

# This configures the button frames
btn_frame = ttk.Frame(main_frame)
btn_frame.grid(row=4, column=0, columnspan=3, pady=10)

# This creates the Fahrenheit button
fahrenheit_btn = ttk.Button(btn_frame, text="Fahrenheit",
                            command=convert_to_fahrenheit, width=10)
fahrenheit_btn.pack(side=tk.LEFT, padx=15)

# This creates the Celsius button
celsius_btn = ttk.Button(btn_frame, text="Celsius",
                         command=convert_to_celsius, width=10)
celsius_btn.pack(side=tk.RIGHT, padx=15)

# This creates the result message
result = ttk.Label(main_frame, text="", font=('Arial', 16, 'bold'))
result.grid(row=5, column=0, columnspan=3, pady=20)

# This configures grid for centering content
# CodingAssist-AI: GPT helped to center the content in the grid
for i in range(3):
   main_frame.grid_columnconfigure(i, weight=1)

# Starts the GUI
root.mainloop()
