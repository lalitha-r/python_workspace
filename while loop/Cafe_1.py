
menu_card = ["tea", "vadai", "coffee", "biscuit"]
price =["15", "5", "12", "10"]

print("Here are the menu")
for i in range(len(menu_card)):
    print(f'{i+1}. {menu_card[i]}  =  {price[i]}')


# Initialize an empty list (array)
myOrders_array = []
count_array = []

# Ask the user for string input in a loop
while True:
    user_input = input("Enter your Order (or 'enough' to close the menu): ")

    if user_input.lower() == 'enough':
        break  # Exit the loop if the user enters 'enough'

    if user_input not in menu_card:
        print("You have entered a wrong item or it's not on the menu")
        # continue
    else:
        # Append the user's input (string) to the array
        myOrders_array.append(user_input)


# Print the items in array
print(" You need:", myOrders_array)

for index, order in enumerate(myOrders_array):
    user_input_2 = input(f'How many {myOrders_array[index]} you want: ')
    count_array.append(int(user_input_2))

print("count:", count_array)

# Print the items and quantities
print("You ordered:")
for i in range(len(myOrders_array)):
    print(f'{myOrders_array[i]} x{count_array[i]}')

# calculating the price
total_price_amount = 0

for i in range(len(myOrders_array)):
    item = myOrders_array[i]
    quantity = count_array[i]
    item_index = menu_card.index(item)
    item_price = int(price[item_index])
    total_price_amount += item_price * quantity

print("Total bill amount:", total_price_amount)