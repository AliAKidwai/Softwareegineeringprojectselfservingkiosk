class Calculator:
    def __init__(self):
        self.cart = []

    def add_item(self, name, price, quantity=1):
        # Add item thats already chosen to the cart
        self.cart.append({
            "name": name,
            "price": float(price),
            "quantity": int(quantity)
        })

    def is_empty(self):
        return len(self.cart) == 0

    def subtotal(self):
        return sum(item["price"] * item["quantity"] for item in self.cart)

    def totals(self, tax_rate=0.0825, tip_percentage=0.0):
        sub = self.subtotal()
        tax = sub * tax_rate
        tip = sub * (tip_percentage / 100.0)
        total = sub + tax + tip
        return sub, tax, tip, total

    def print_receipt(self, tax_rate=0.0825, tip_percentage=0.0):
        sub, tax, tip, total = self.totals(tax_rate, tip_percentage)

        print("\n----- Cafe Blanc Receipt -----")
        for i, item in enumerate(self.cart, start=1):
            line_total = item["price"] * item["quantity"]
            print(f"{i}. {item['name']:<15} x{item['quantity']}  ${line_total:6.2f}")
        print("-------------------")
        print(f"Subtotal:         ${sub:6.2f}")
        print(f"Tax:              ${tax:6.2f}")
        print(f"Tip:              ${tip:6.2f}")
        print(f"TOTAL:            ${total:6.2f}")
        print("-------------------")
        print("Thank you for shopping at Blanc!")


def checkout(cart: Calculator, tax_rate=0.0825):
    if cart.is_empty():
        print("\nYour cart is empty. Nothing to check out.")
        return

    print("\n----- Payment Checkout -----")

    # Ask for the tip amount
    try:
        tip_percentage = float(input("Enter tip percentage: "))
    except ValueError:
        tip_percentage = 0.0

    # Ask if the user wants a receipt
    choice = input("Would you like a receipt? (yes/no): ").strip().lower()

    if choice == "yes":
        cart.print_receipt(tax_rate=tax_rate, tip_percentage=tip_percentage)
    else:
        _, _, _, total = cart.totals(tax_rate=tax_rate, tip_percentage=tip_percentage)
        print(f"\nYour total is: ${total:.2f}")
        print("Thank you for shopping at Blanc Cafe!")
