import re

# nested dictionary-includes item as key and details like quantity, selling_price, profit, items_sold as value
menu = {
    "vadai": {"quantity": 50, "selling_price": 15, "profit": 5, "items_sold": 0},
    "tea": {"quantity": 45, "selling_price": 17, "profit": 5, "items_sold": 0},
    "coffee": {"quantity": 40, "selling_price": 21, "profit": 6, "items_sold": 0}
}

# list the menu card to customer
for item, details in menu.items():
    print(f"{item}: {details['selling_price']} ")

order_count = 0

# get input from customer using while
while order_count < 2:
    user_input = input(f"Enter input {order_count + 1} of 10: ")
    quantity = re.findall(r'\d+', user_input)
    items = re.findall(r'\b(vadai|tea|coffee)\b', user_input.lower())

    # loop through each item in current order
    for index, item in enumerate(items):
        # check if asked quantity is more than available quantity
        if int(quantity[index]) > menu[item]['quantity']:
            print("No stock")
        else:
            # reduce the quantity if its a valid order
            menu[item]['quantity'] -= int(quantity[index])
            # add item_sold to the menu
            menu[item]['items_sold'] += int(quantity[index])

    # print the available qty for each item
    for item, details in menu.items():
        print(f"Available qty for {item}: {details['quantity']} ")

    order_count += 1

# print the profit for each item
for item, details in menu.items():
    print(f"Profit for {item} is {details['profit'] * details['items_sold']}")

print(menu)