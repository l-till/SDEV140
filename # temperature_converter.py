# temperature_converter.py
# [Your Name]
# [Date]
# GUI Temperature Converter (Celsius ↔ Fahrenheit)

# Formula references:
# https://www.thoughtco.com/celcius-to-farenheit-formula-609227
# https://www.metric-conversions.org/temperature/celsius-to-fahrenheit.htm

import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius"""
    return (f - 32) * 5/9

def convert_to_fahrenheit():
    """Handle Celsius to Fahrenheit conversion"""
    try:
        c = float(entry_temp.get())
        f = celsius_to_fahrenheit(c)
        lbl_result.config(text=f"{f:.1f} °F")
    except ValueError:
        lbl_result.config(text="Invalid input!")

def convert_to_celsius():
    """Handle Fahrenheit to Celsius conversion"""
    try:
        f = float(entry_temp.get())
        c = fahrenheit_to_celsius(f)
        lbl_result.config(text=f"{c:.1f} °C")
    except ValueError:
        lbl_result.config(text="Invalid input!")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.resizable(False, False)

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

lbl_title = ttk.Label(frame, text="Temperature Converter", font=('Arial', 12))
lbl_title.grid(row=0, column=0, columnspan=2, pady=10)

lbl_instruction = ttk.Label(frame, text="Enter temperature:")
lbl_instruction.grid(row=1, column=0, sticky=tk.W, pady=5)

entry_temp = ttk.Entry(frame, width=15)
entry_temp.grid(row=1, column=1, sticky=tk.E, pady=5)

btn_to_fahr = ttk.Button(frame, text="Convert to Fahrenheit", command=convert_to_fahrenheit)
btn_to_fahr.grid(row=2, column=0, pady=5, sticky=tk.W)

btn_to_cels = ttk.Button(frame, text="Convert to Celsius", command=convert_to_celsius)
btn_to_cels.grid(row=2, column=1, pady=5, sticky=tk.E)

lbl_result = ttk.Label(frame, text="", font=('Arial', 14))
lbl_result.grid(row=3, column=0, columnspan=2, pady=15)

# Start the application
root.mainloop()