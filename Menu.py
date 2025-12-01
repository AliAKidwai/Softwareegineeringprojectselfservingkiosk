matcha = ["Matcha Latte", "Strawberry Matcha", "Blueberry Matcha"]
coffee = ["Espresso", "Flat White", "Latte"]
tea = ["Green Tea", "Black Tea", "Fruit Tea"]
snacks = ["Croissant", "Cookie", "Muffin"]

import rewards  

def display_menu():
    print("Welcome to Coffee Shop!")
    print("1. matcha")
    print("2. coffee")
    print("3. tea")
    print("4. snacks")
    print("5. Checkout")

def menu_selection():
    option = input("Select a menu (1-5): ")
    while option not in ["1", "2", "3", "4", "5"]:
        print("Please enter a valid menu number.")
        option = input("Select a menu (1-5): ")
    return option

def select(option, cart):
    if option == "1":
        print(matcha)
        category = matcha
    elif option == "2":
        print(coffee)
        category = coffee
    elif option == "3":
        print(tea)
        category = tea
    elif option == "4":
        print(snacks)
        category = snacks
    elif option == "5":
        rewards.main()  
        return "checkout"  
    else:
        return

    print("Type 'back' to return to the main menu.")
    item = input("Select item: ")
    if item == "back":
        return
    while item not in category:
        print("Please select an item in the menu.")
        item = input("Select item: ")
    cart.append(item)
    print("Added to cart,", item)

def main():
    cart = []
    keepOrdering = "yes"

    while keepOrdering == "yes":
        display_menu()
        option = menu_selection()
        result = select(option, cart)
        if result == "checkout":
            break
        keepOrdering = input("Would you like to keep ordering? (yes/no): ")

main()

