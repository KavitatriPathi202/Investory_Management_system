def validate_positive_int(prompt):
    """Prompts user and ensures input is a positive integer."""
    while True:
        try:
            val = int(input(prompt).strip())
            if val >= 0:
                return val
            print("[Error] Number cannot be negative.")
        except ValueError:
            print("[Error] Invalid input! Please enter a whole number.")

def validate_positive_float(prompt):
    """Prompts user and ensures input is a positive decimal number."""
    while True:
        try:
            val = float(input(prompt).strip())
            if val >= 0:
                return val
            print("[Error] Price cannot be negative.")
        except ValueError:
            print("[Error] Invalid input! Please enter a valid price.")
