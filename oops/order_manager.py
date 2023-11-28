import re
from menu_item import MenuItem


class OrderManager:
    def __init__(self, menu_items):
        self.menu = {item[0]: MenuItem(*item) for item in menu_items}

    def display_menu(self):
        for item in self.menu.values():
            print(f"{item.name}: {item.price}")

    def take_order(self, number_of_orders):
        for _ in range(number_of_orders):
            user_input = input("Enter your order: ")
            quantities = re.findall(r'\d+', user_input)
            items = re.findall(r'\b(vadai|tea|coffee)\b', user_input.lower())

            for index, item_name in enumerate(items):
                if item_name in self.menu:
                    item = self.menu[item_name]
                    if item.update_stock(int(quantities[index])):
                        print(f"Order placed for {item_name}")
                    else:
                        print("No stock for", item_name)
                else:
                    print("Invalid item:", item_name)

    def print_profits(self):
        for item in self.menu.values():
            print(f"Profit for {item.name} is {item.calculate_profit()}")
