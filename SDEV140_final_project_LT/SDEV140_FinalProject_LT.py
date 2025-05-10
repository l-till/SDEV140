# SDEV140_FinalProject_LT.py
# Logan Till
# 2025-05-02
# DineEasy - Restaurant Ordering System
# This program is for a restaurant ordering system
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("DineEasy (by Logan Till)")
print("***************************************\n")

# Import Libraries
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import os

# Constants
TAX_RATE = 0.07

# Variables
order_items = []
order_total = 0.0

# TKINTER STARTS HERE
# This creates the main window

class DineEasyApp:
   def __init__(self, root):
      self.root = root
      self.root.title("DineEasy")
      self.root.geometry("800x600")
      self.root.resizable(False, False)
      self.root.configure(bg="")
      self.root.grid_rowconfigure(0, weight=1)
      self.root.grid_columnconfigure(0, weight=1)
      self.root.grid_columnconfigure(1, weight=3)

      # This will create the menu items
      # CodeAssist-AI: IDE auto-completed this code 
      self.menu_items = {
         'Apps': [
            {'name': 'Spring Rolls', 'price': 5.99},
            {'name': 'Garlic Bread', 'price': 4.99},
            {'name': 'Bruschetta', 'price': 6.99},
            {'name': 'Calamari', 'price': 8.99},
            {'name': 'Stuffed Mushrooms', 'price': 7.99},
            {'name': 'Buffalo Wings', 'price': 9.99},
            {'name': 'Nachos', 'price': 8.49},
            {'name': 'Onion Rings', 'price': 5.49},
            {'name': 'Mozzarella Sticks', 'price': 6.49},
            {'name': 'Potato Skins', 'price': 7.49},
         ],
         'Salads': [
            {'name': 'Caesar Salad', 'price': 8.99},
            {'name': 'Greek Salad', 'price': 9.99},
            {'name': 'Caprese Salad', 'price': 10.99},
            {'name': 'Garden Salad', 'price': 7.99},
            {'name': 'Spinach Salad', 'price': 8.99},
            {'name': 'Cobb Salad', 'price': 11.99},
            {'name': 'Quinoa Salad', 'price': 9.49},
            {'name': 'Fruit Salad', 'price': 6.99},
            {'name': 'Chicken Salad', 'price': 12.99},
            {'name': 'Tuna Salad', 'price': 10.49},
         ],
         'Entrees': [
            {'name': 'Grilled Chicken', 'price': 14.99},
            {'name': 'Steak', 'price': 19.99},
            {'name': 'Salmon', 'price': 17.99},
            {'name': 'Pasta Primavera', 'price': 12.99},
            {'name': 'Vegetable Stir Fry', 'price': 11.99},
            {'name': 'Shrimp Scampi', 'price': 18.99},
            {'name': 'Beef Tacos', 'price': 10.99},
            {'name': 'Chicken Alfredo', 'price': 13.99},
            {'name': 'Lamb Chops', 'price': 22.99},
            {'name': 'Vegetable Curry', 'price': 11.49},
         ],
         'Desserts': [
            {'name': 'Cheesecake', 'price': 6.99},
            {'name': 'Chocolate Cake', 'price': 5.99},
            {'name': 'Tiramisu', 'price': 7.99},
            {'name': 'Ice Cream', 'price': 4.99},
            {'name': 'Fruit Tart', 'price': 6.49},
            {'name': 'Brownie Sundae', 'price': 8.49},
            {'name': 'Panna Cotta', 'price': 7.49},
            {'name': 'Apple Pie', 'price': 5.49},
            {'name': 'Crème Brûlée', 'price': 9.99},
            {'name': 'Chocolate Mousse', 'price': 6.99},
         ],
         'Beverages': [
            {'name': 'Soda', 'price': 2.99},
            {'name': 'Coffee', 'price': 2.49},
            {'name': 'Tea', 'price': 1.99},
            {'name': 'Juice', 'price': 3.49},
            {'name': 'Water', 'price': 0.00},
            {'name': 'Iced Tea', 'price': 2.99},
            {'name': 'Lemonade', 'price': 3.49},
            {'name': 'Milkshake', 'price': 4.99},
            {'name': 'Smoothie', 'price': 5.49},
            {'name': 'Hot Chocolate', 'price': 2.99},
         ],
         'Specials': [
            {'name': 'Lobster Tail', 'price': 29.99},
            {'name': 'Filet Mignon', 'price': 24.99},
            {'name': 'Seafood Paella', 'price': 22.99},
            {'name': 'Duck Confit', 'price': 21.99},
            {'name': 'Rack of Lamb', 'price': 26.99},
            {'name': 'Surf and Turf', 'price': 34.99},
            {'name': 'Truffle Risotto', 'price': 19.99},
            {'name': 'Osso Buco', 'price': 23.99},
            {'name': 'Beef Wellington', 'price': 28.99},
            {'name': 'Sea Bass', 'price': 24.49},
         ],
      }

      self.current_category = list(self.menu_items.keys())[0]
      self.setup_ui()

   def setup_ui(self):
      # This will style the widgets
      style = ttk.Style()
      style.theme_use("clam")
      font_style = ('Arial', 12)

      # This creates the main frame
      self.main_frame = ttk.Frame(self.root, padding=20)
      self.main_frame.pack(fill=tk.BOTH, expand=True)

      # This will configure the grid weights
      self.main_frame.columnconfigure(0, weight=1)
      self.main_frame.columnconfigure(1, weight=2)
      self.main_frame.rowconfigure(1, weight=1)


      # ORDER SUMMARY - Left Side
      # Order summary frame
      summary_frame = ttk.Frame(self.main_frame, padding=10)
      summary_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

      customer_frame = ttk.Frame(summary_frame)
      customer_frame.grid(row=0, column=0)
      customer_frame.columnconfigure(0, weight=1)
      customer_frame.columnconfigure(1, weight=2)

      ttk.Label(customer_frame, text="Name:").grid(row=0, column=0, sticky="e")
      self.name_entry = ttk.Entry(customer_frame)
      self.name_entry.grid(row=0, column=1, sticky="w")
      
      ttk.Label(customer_frame, text="Table #:").grid(row=1, column=0,
                                                      sticky="e")
      self.table_entry = ttk.Entry(customer_frame, width=5)
      self.table_entry.grid(row=1, column=1, sticky="w")
      
      self.order_tree = ttk.Treeview(summary_frame, columns=("Item", "Price"),
                                     show="headings")
      self.order_tree.heading("Item", text="Item")
      self.order_tree.heading("Price", text="Price")
      self.order_tree.column("Item", width=150)
      self.order_tree.column("Price", width=80)
      self.order_tree.grid(row=1, column=0, sticky="nsew", pady=(10, 0))

      # This sets a frame for the order total and buttons
      button_frame = ttk.Frame(summary_frame)
      button_frame.grid(row=2, column=0, pady=(10, 0), sticky="nsew")
      
      # This sets the order total label
      self.total_label = ttk.Label(button_frame, text="Total: $0.00",
                                    font=('Arial', 12, 'bold'))
      self.total_label.grid(row=0, column=0)

      # This sets the remove item button and submit order button
      """ ttk.Button(button_frame, text="Remove", command=self.remove_item).pack(side=tk.RIGHT, padx=5)
      ttk.Button(button_frame, text="Submit", command=self.submit_order).pack(side=tk.RIGHT) """

      remove_button = ttk.Button(button_frame, text="Remove Item",
                                 command=self.remove_item)
      remove_button.grid(row=0, column=1, padx=5)
      submit_button = ttk.Button(button_frame, text="Submit Order",
                                 command=self.submit_order)
      submit_button.grid(row=0, column=2, padx=5)

      # MENU 
      # Menu frame
      menu_frame = ttk.Frame(self.main_frame, padding=10)
      menu_frame.grid(row=0, column=1, padx = 10, pady=10, sticky="nsew")

      categories_frame = ttk.Frame(menu_frame,)
      categories_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
      
      for category in self.menu_items.keys():
         btn = ttk.Button(categories_frame, text=category, 
                        command=lambda c=category: self.show_menu_items(c))
         btn.pack(side=tk.LEFT, expand=True, padx=2)

      self.items_frame = ttk.Frame(menu_frame)
      self.items_frame.grid(row=1, column=0, sticky="nsew")
      self.show_menu_items(list(self.menu_items.keys())[0])

   def show_menu_items(self, category):
      # Clear the current menu items
      for widget in self.items_frame.winfo_children():
         widget.destroy()

      row = 0
      col = 0
      items = self.menu_items[category]
      
      for i, item in enumerate(items):
         item_frame = ttk.Frame(self.items_frame, padding=5, relief="solid", borderwidth=1)
         item_frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
         
         # Make entire frame clickable
         item_frame.bind("<Button-1>", lambda e, it=item: self.add_item(it))
         
         # Item name
         name_label = ttk.Label(item_frame, text=item['name'], font=('Arial', 10, 'bold'))
         name_label.pack()
         name_label.bind("<Button-1>", lambda e, it=item: self.add_item(it))
         
         # Item price
         price_label = ttk.Label(item_frame, text=f"${item['price']:.2f}")
         price_label.pack()
         price_label.bind("<Button-1>", lambda e, it=item: self.add_item(it))
         
         # Alternate columns
         col += 1
         if col > 2:  # 3 columns
               col = 0
               row += 1

         # Configure grid weights
         for i in range(3):  # 3 columns
            self.items_frame.columnconfigure(i, weight=1)
         for i in range(row + 1):
            self.items_frame.rowconfigure(i, weight=1)

   def add_item(self, item):
      # Check if item already exists
      for child in self.order_tree.get_children():
         if self.order_tree.item(child)['values'][0] == item['name']:
               messagebox.showwarning("Warning", f"{item['name']} is already in your order")
               return
      
      # Add to order
      self.order_tree.insert("", tk.END, values=(item['name'], f"${item['price']:.2f}"))
      self.update_total()

   def remove_item(self):
      selected_item = self.order_tree.selection()

      for item in selected_item:
         self.order_tree.delete(item)

      self.update_total()

   def update_total(self):
      global order_total
      order_total = 0.0

      for child in self.order_tree.get_children():
         price_str = self.order_tree.item(child)['values'][1]
         price = float(price_str.replace('$', ''))
         order_total += price

      # Update the total amount label
      self.total_label.config(text=f"Total: ${order_total:.2f}")

   def submit_order(self):
      name = self.name_entry.get()
      table = self.table_entry.get()

      order_summary = []
      for child in self.order_tree.get_children():
         item = self.order_tree.item(child)['values']
         order_summary.append(f"{item[0]} - {item[1]}")
      
      # Show confirmation
      message = f"Customer: {name}\nTable: {table}\n\nOrder:\n" + "\n".join(order_summary)
      message += f"\n\nTotal: ${order_total:.2f}"
      
      if messagebox.askyesno("Confirm Order", message + "\n\nSubmit this order?"):
         messagebox.showinfo("Success", "Order submitted successfully!")
         # Clear the order
         for item in self.order_tree.get_children():
               self.order_tree.delete(item)
         self.update_total()
      

# Starts the GUI
if __name__ == "__main__":
   root = tk.Tk()
   app = DineEasyApp(root)
   root.mainloop()