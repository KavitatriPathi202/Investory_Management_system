# inventory.py - Product Stock CRUD Operations

# Global dictionary to store inventory data
inventory = {}

def add_product(sku, name, price, quantity, category):
    """Add a new product to the inventory using a unique SKU."""
    if sku in inventory:
        print(f"\n[Error] Product with SKU '{sku}' already exists!")
        return False

    try:
        inventory[sku] = {
            "name": name,
            "price": float(price),
            "quantity": int(quantity),
            "category": category
        }
        print(f"\n[Success] Product '{name}' added successfully!")
        return True
    except ValueError:
        print("\n[Error] Invalid price or quantity! Please enter numbers.")
        return False

def view_all_products():
    """Display all products in the inventory."""
    if not inventory:
        print("\n[Info] Inventory is currently empty.")
        return

    print("\n" + "="*60)
    print(f"{'SKU':<10} {'Name':<15} {'Price ($)':<10} {'Qty':<10} {'Category':<15}")
    print("="*60)
    for sku, details in inventory.items():
        print(f"{sku:<10} {details['name']:<15} {details['price']:<10.2f} {details['quantity']:<10} {details['category']:<15}")
    print("="*60)

def update_product_quantity(sku, new_qty):
    """Update stock quantity for an existing SKU."""
    if sku not in inventory:
        print(f"\n[Error] SKU '{sku}' not found.")
        return False
    try:
        inventory[sku]['quantity'] = int(new_qty)
        print(f"\n[Success] Quantity updated for SKU '{sku}'.")
        return True
    except ValueError:
        print("\n[Error] Please enter a valid integer for quantity.")
        return False

def delete_product(sku):
    """Delete a product from the inventory."""
    if sku in inventory:
        del inventory[sku]
        print(f"\n[Success] Product '{sku}' deleted.")
        return True
    else:
        print(f"\n[Error] SKU '{sku}' not found.")
        return False
