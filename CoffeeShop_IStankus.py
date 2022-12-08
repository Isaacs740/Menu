total = 0
name = {
    'Coffee': "3.15",
    'Latte': "5.25",
    'Espresso': "5.55",
    'Cappuccino': "4.55",
    'Hot Chocolate': "3.55",
}


# print menu
def menu(order):
    print("Welcome to MyCoffee Shop")
    print("_________MENU_________")
    print("Name    Cost")
    for x, y in order.items():
        print(x + "  " + y)


menu(name)

while True:
    item = input("What would you like to order?\nEnter item name (or '99 to end')\n")
    if item == "99":
        print("Thanks for shopping at MyCoffee Shop")
        break
    if item in name:
        qty = input("How many would you like?\n")
        total = total + (float(name[item]) * int(qty))
        print("Total for your order is " + str(total))
    else:
        print("That item - " + item + " - is not available")
