# main.py - Integrated Entry Point for Inventory Management System
import inventory
import billing
import analytics 

def inventory_sub_menu():
    """Sub-menu for inventory CRUD operations."""
    while True:
        print("\n--- INVENTORY MANAGEMENT ---")
        print("1. Add New Product")
        print("2. View All Products")
        print("3. Update Product Quantity")
        print("4. Delete Product")
        print("5. Back to Main Menu")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            sku = input("Enter SKU code: ").strip()
            name = input("Enter Product Name: ").strip()
            price = input("Enter Price ($): ").strip()
            qty = input("Enter Initial Quantity: ").strip()
            cat = input("Enter Category: ").strip()
            inventory.add_product(sku, name, price, qty, cat)
            
        elif choice == '2':
            inventory.view_all_products()
            
        elif choice == '3':
            sku = input("Enter SKU to update: ").strip()
            qty = input("Enter New Quantity: ").strip()
            inventory.update_product_quantity(sku, qty)
            
        elif choice == '4':
            sku = input("Enter SKU to delete: ").strip()
            inventory.delete_product(sku)
            
        elif choice == '5':
            break
        else:
            print("\nInvalid choice! Please select 1-5.")

def main_menu():
    """Main application loop."""
    while True:
        print("\n==========================================")
        print("   INVENTORY MANAGEMENT SYSTEM (IMS)")
        print("==========================================")
        print("1. Inventory Management (CRUD)")
        print("2. Billing & Point of Sale")
        print("3. Stock Alerts & Analytics")
        print("4. Exit")
        print("==========================================")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            inventory_sub_menu()
        elif choice == '2':
            billing.generate_bill()
        elif choice == '3':
            analytics.show_analytics()
        elif choice == '4':
            print("\nThank you for using Inventory Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main_menu()
