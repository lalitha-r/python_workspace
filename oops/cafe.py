from order_manager import OrderManager


# Define your menu items
menu_items = [
    ["vadai", 50, 15, 5],
    ["tea", 45, 17, 5],
    ["coffee", 40, 21, 6]
]

# Create an OrderManager instance
order_manager = OrderManager(menu_items)

# Display the menu
order_manager.display_menu()

# Take an order
order_manager.take_order(3)

# Print the profits
order_manager.print_profits()
