# 3 tea and 2 vadai
# 2 coffee and 3 vadai

import re
# nested array-includes item, quantity, selling_price, profit, items_sold
menu = [
    ["vadai", 50, 15, 5, 0],
    ["tea", 45, 17, 5, 0],
    ["coffee", 40, 21, 6, 0]
]


for menu_item in menu:
    # list the menu card to customer
    print(f"{menu_item[0]}: {menu_item[2]} ")

order_count = 0

# get input from customer using while
while (order_count < 1):
    user_input = input(f"Enter input {order_count + 1} of 10: ")
    quantity = re.findall(r'\d+', user_input)
    items = re.findall(r'\b(vadai|tea|coffee)\b', user_input.lower())

    # loop throuh each item in current order
    for index, item in enumerate(items):

        # find the index of the menu based on item name
        menuIndex = next(
            (i for i, menuItem in enumerate(menu) if menuItem[0] == item))

        # get the menuItem based on the index
        currentMenuItem = menu[menuIndex]

        # check if asked quantity is more than available quantity
        # if yes print No stock
        if (int(quantity[index]) > currentMenuItem[1]):
            print("No stock")

        # reduce the  quantity if its a valid order
        currentMenuItem[1] -= int(quantity[index])

        # add item_sold to the menu
        currentMenuItem[4] += int(quantity[index])

    # print the available qty for each item
    for menu_item in menu:
        print(f"Available qty for {menu_item[0]}: {menu_item[1]} ")
    order_count += 1

# print the profit for each item
for menu_item in menu:
    print(f"Profit for {menu_item[0]} is {menu_item[3]*menu_item[4]}")

# output:
# Enter input 1 of 10: 5 coffee and 3 vadai
# Available qty for vadai: 47
# Available qty for tea: 45
# Available qty for coffee: 35
# Profit for vadai is 15
# Profit for tea is 0
# Profit for coffee is 30
