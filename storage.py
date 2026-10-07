import inventory

FILE_NAME = "inventory_data.txt"

def save_data():
    """Saves inventory data to a text file separated by commas."""
    try:
        with open(FILE_NAME, "w") as f:
            for sku, item in inventory.inventory.items():
                f.write(f"{sku},{item['name']},{item['price']},{item['quantity']},{item['category']}\n")
        print("\n[Success] Data saved to inventory_data.txt")
    except Exception as e:
        print(f"\n[Error] Could not save data: {e}")

def load_data():
    """Loads inventory data from text file back into inventory dictionary."""
    try:
        with open(FILE_NAME, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    sku, name, price, qty, cat = parts
                    inventory.inventory[sku] = {
                        "name": name,
                        "price": float(price),
                        "quantity": int(qty),
                        "category": cat
                    }
        print("\n[Success] Data loaded from inventory_data.txt")
    except FileNotFoundError:
        print("\n[Info] No saved file found. Starting fresh.")
