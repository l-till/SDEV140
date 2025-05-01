# SDEV140_FinalProject_LT.py
# Logan Till
# 2025-04-19
# DineEasy - Restaurant Ordeing System
# This program is for a restaurant ordering system
# No coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("DineEasy (by Logan Till)")
print("***************************************\n")

# Import Libraries
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import os


input_file = 'input.txt'
output_file = 'output.txt'

# Constants
TAX_RATE = 0.07

# Variables
order_items = []
order_total = 0.0

# FUNCTIONS START HERE

   


# TKINTER STARTS HERE

# This creates the main window
root = tk.Tk()
root.title("DineEasy")
root.geometry("800x600")
root.resizable(True, True)
#root.configure(bg="")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)



# This will style the widgets
style = ttk.Style()
style.theme_use("clam")
font_style = ('Arial', 12)

#This creates the main frame
#main_frame = ttk.Frame(root, padding=20)
#main_frame.pack(fill=tk.BOTH, expand=True)

# ORDER SUMMARY
# Order summary frame
summary_frame = ttk.Frame(root, padding=10)
summary_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
summary_frame.grid_rowconfigure(0, weight=1)
summary_frame.grid_rowconfigure(1, weight=3)
summary_frame.grid_columnconfigure(0, weight=1)

customer_info = ttk.LabelFrame(summary_frame, text="Customer Information",
                               padding=10)
customer_info.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#customer

order_summary = ttk.LabelFrame(summary_frame, text="Order Summary",
                               padding=10)
order_summary.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

summary_text = tk.Text(order_summary, font=font_style)
summary_text.grid(row=0, column=0, sticky="nse")
#109

# MENU 
# Menu frame
menu_frame = ttk.Frame(root, padding=10)
menu_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
menu_frame.grid_rowconfigure(0, weight=1)
menu_frame.grid_rowconfigure(1, weight=3)
menu_frame.grid_columnconfigure(0, weight=1)

menu_tabs = ttk.LabelFrame(menu_frame, text="Menu Tabs", padding=10)
menu_tabs.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
#menu_tabs = ttk.Label(menu_frame, padding=10)

menu_items = ttk.LabelFrame(menu_frame, text="Menu Items", 
                            padding=10)
menu_items.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")



# Starts the GUI
root.mainloop()