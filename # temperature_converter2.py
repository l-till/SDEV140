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
        lbl_result.config(text=f"{f:.1f} °F", foreground="blue")
    except ValueError:
        lbl_result.config(text="Invalid input!", foreground="red")

def convert_to_celsius():
    """Handle Fahrenheit to Celsius conversion"""
    try:
        f = float(entry_temp.get())
        c = fahrenheit_to_celsius(f)
        lbl_result.config(text=f"{c:.1f} °C", foreground="blue")
    except ValueError:
        lbl_result.config(text="Invalid input!", foreground="red")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")  # Larger window size
root.resizable(False, False)

# Configure style for larger widgets
style = ttk.Style()
style.configure("TFrame", padding=20)
style.configure("TButton", font=('Arial', 12), padding=10)
style.configure("TLabel", font=('Arial', 12))
style.configure("TEntry", font=('Arial', 12), padding=5)

# Create and place widgets with larger dimensions
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

lbl_title = ttk.Label(main_frame, text="Temperature Converter", font=('Arial', 14, 'bold'))
lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

input_frame = ttk.Frame(main_frame)
input_frame.grid(row=1, column=0, columnspan=2, pady=10)

lbl_instruction = ttk.Label(input_frame, text="Enter temperature:")
lbl_instruction.grid(row=0, column=0, padx=5, sticky=tk.W)

entry_temp = ttk.Entry(input_frame, width=20)
entry_temp.grid(row=0, column=1, padx=5)

button_frame = ttk.Frame(main_frame)
button_frame.grid(row=2, column=0, columnspan=2, pady=20)

btn_to_fahr = ttk.Button(button_frame, text="Convert to Fahrenheit", 
                        command=convert_to_fahrenheit, width=20)
btn_to_fahr.grid(row=0, column=0, padx=10)

btn_to_cels = ttk.Button(button_frame, text="Convert to Celsius", 
                        command=convert_to_celsius, width=20)
btn_to_cels.grid(row=0, column=1, padx=10)

lbl_result = ttk.Label(main_frame, text="", font=('Arial', 16, 'bold'))
lbl_result.grid(row=3, column=0, columnspan=2, pady=20)

# Start the application
root.mainloop()
