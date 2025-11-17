#payment calculater
import json
import math
import Administer
import Menu

#payment calculater
import json
import math
import Administer
import Menu

class calculater():
    def __init__(self, price, name, quantity):
        self.cart = []
        self.price = price
        self.name = name
        self.quantity = quantity

    def items(self, category, item, quantity):
        with open(MENU_FILE, "r") as f:
            menu = json.load(f)
        price = menu[category].get(item_name)
        if price is None:
            print(f"Item '{item_name}' not found in category '{category}'.")
            return
        self.cart.append({
            "name": item_name,
            "price": price,
            "quantity": quantity
        })

    def calculate(self):
        total = 0
        for item in self.cart:
            total += item[price] * item[quantity]
        return total



#payment method
