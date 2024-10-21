import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Define a folder path where the inventory file will be stored
folder_path = 'inventory_data'

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# File to store inventory data inside the folder
inventory_file = os.path.join(folder_path, 'inventory.json')


# Load inventory from file
def load_inventory():
    if os.path.exists(inventory_file):
        with open(inventory_file, 'r') as file:
            return json.load(file)
    return {}


# Save inventory to file
def save_inventory(inventory):
    with open(inventory_file, 'w') as file:
        json.dump(inventory, file, indent=4)


# Add a new product
def add_product(inventory, root):
    product_id = simpledialog.askstring("Input", "Enter product ID:", parent=root)
    if not product_id:
        return
    if product_id in inventory:
        messagebox.showerror("Error", "Product ID already exists!")
        return

    name = simpledialog.askstring("Input", "Enter product name:", parent=root)
    price = simpledialog.askfloat("Input", "Enter product price:", parent=root)
    quantity = simpledialog.askinteger("Input", "Enter product quantity:", parent=root)
    minimum_stock = simpledialog.askinteger("Input", "Enter minimum stock level:", parent=root)

    inventory[product_id] = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'minimum_stock': minimum_stock
    }

    save_inventory(inventory)
    messagebox.showinfo("Success", f"Product {name} added successfully!")


# Edit an existing product
def edit_product(inventory, root):
    product_id = simpledialog.askstring("Input", "Enter product ID to edit:", parent=root)
    if not product_id or product_id not in inventory:
        messagebox.showerror("Error", "Product ID does not exist!")
        return

    product = inventory[product_id]

    name = simpledialog.askstring("Input", f"Enter new name (current: {product['name']}):", parent=root)
    price = simpledialog.askfloat("Input", f"Enter new price (current: {product['price']}):", parent=root)
    quantity = simpledialog.askinteger("Input", f"Enter new quantity (current: {product['quantity']}):", parent=root)
    minimum_stock = simpledialog.askinteger("Input", f"Enter new minimum stock level (current: {product['minimum_stock']}):", parent=root)

    if name:
        product['name'] = name
    if price is not None:
        product['price'] = price
    if quantity is not None:
        product['quantity'] = quantity
    if minimum_stock is not None:
        product['minimum_stock'] = minimum_stock

    save_inventory(inventory)
    messagebox.showinfo("Success", "Product updated successfully!")


# Delete a product
def delete_product(inventory, root):
    product_id = simpledialog.askstring("Input", "Enter product ID to delete:", parent=root)
    if product_id in inventory:
        del inventory[product_id]
        save_inventory(inventory)
        messagebox.showinfo("Success", f"Product {product_id} deleted successfully!")
    else:
        messagebox.showerror("Error", "Product ID does not exist!")


# Show inventory summary
def show_inventory(inventory, root):
    if not inventory:
        messagebox.showinfo("Info", "Inventory is empty!")
        return

    summary = ""
    for product_id, details in inventory.items():
        summary += (f"ID: {product_id}\n"
                    f"Name: {details['name']}\n"
                    f"Price: {details['price']}\n"
                    f"Quantity: {details['quantity']}\n"
                    f"Minimum Stock Level: {details['minimum_stock']}\n"
                    f"-------------------------\n")

    messagebox.showinfo("Inventory Summary", summary)


# Check for low stock products
def check_low_stock(inventory, root):
    low_stock_items = [prod for prod, details in inventory.items() if details['quantity'] < details['minimum_stock']]

    if not low_stock_items:
        messagebox.showinfo("Low Stock", "No low stock products.")
    else:
        alert = "\n".join([f"{inventory[prod]['name']} (ID: {prod})" for prod in low_stock_items])
        messagebox.showwarning("Low Stock", f"Low stock products:\n{alert}")


# Main menu
def main_menu(root):
    inventory = load_inventory()

    tk.Button(root, text="Add Product", command=lambda: add_product(inventory, root)).pack(pady=5)
    tk.Button(root, text="Edit Product", command=lambda: edit_product(inventory, root)).pack(pady=5)
    tk.Button(root, text="Delete Product", command=lambda: delete_product(inventory, root)).pack(pady=5)
    tk.Button(root, text="Show Inventory", command=lambda: show_inventory(inventory, root)).pack(pady=5)
    tk.Button(root, text="Check Low Stock", command=lambda: check_low_stock(inventory, root)).pack(pady=5)
    tk.Button(root, text="Exit", command=root.quit).pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Inventory Management")
    root.geometry("300x300")

    main_menu(root)

    root.mainloop()
