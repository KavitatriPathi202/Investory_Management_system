# billing.py - Billing and Point of Sale Module
import inventory

def generate_bill():
    """Processes a sale and deducts sold items from inventory."""
    sku = input("Enter Product SKU to buy: ").strip()
    
    if sku not in inventory.inventory:
        print(f"\n[Error] SKU '{sku}' not found in inventory!")
        return
    
    try:
        qty_to_buy = int(input("Enter Quantity to buy: ").strip())
    except ValueError:
        print("\n[Error] Please enter a valid number for quantity.")
        return

    current_qty = inventory.inventory[sku]['quantity']
    
    if qty_to_buy > current_qty:
        print(f"\n[Error] Not enough stock! Only {current_qty} available.")
        return
    
    unit_price = float(inventory.inventory[sku]['price'])
    total_cost = unit_price * qty_to_buy
    
    inventory.inventory[sku]['quantity'] -= qty_to_buy
    
    print("\n==========================================")
    print("             CUSTOMER RECEIPT             ")
    print("==========================================")
    print(f" Item:       {inventory.inventory[sku]['name']}")
    print(f" Quantity:   {qty_to_buy}")
    print(f" Unit Price: ${unit_price:.2f}")
    print(f" Total Paid: ${total_cost:.2f}")
    print("==========================================")
    print(" Thank you for your purchase!")
