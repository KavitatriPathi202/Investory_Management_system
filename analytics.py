# analytics.py - Stock Alerts and Analytics Module
import inventory

LOW_STOCK_THRESHOLD = 3

def show_analytics():
    """Displays low stock alerts and total inventory value."""
    if not inventory.inventory:
        print("\n[Info] No inventory data available for analytics.")
        return

    print("\n==========================================")
    print("        STOCK ALERTS & ANALYTICS          ")
    print("==========================================")

    # 1. Low Stock Alerts
    print("\n--- Low Stock Alerts (Qty < 3) ---")
    low_stock_found = False
    for sku, details in inventory.inventory.items():
        if details['quantity'] < LOW_STOCK_THRESHOLD:
            print(f" [ALERT] SKU: {sku} | Name: {details['name']} | Remaining Qty: {details['quantity']}")
            low_stock_found = True
    
    if not low_stock_found:
        print(" All products are sufficiently stocked.")

    # 2. Inventory Financial Valuation
    total_items = sum(item['quantity'] for item in inventory.inventory.values())
    total_valuation = sum(item['price'] * item['quantity'] for item in inventory.inventory.values())

    print("\n--- Inventory Summary ---")
    print(f" Total Unique Products: {len(inventory.inventory)}")
    print(f" Total Units in Stock:  {total_items}")
    print(f" Total Inventory Value: ${total_valuation:.2f}")
    print("==========================================")
