# Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
# When the customer comes in, vendor asks "What do you want to buy?" .
# The customer can say "I want apple", or "Apple" or "three apple" or something like that.
# Your program will find out what fruit the customer is asking. 
# Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
# Print the quantity if the customer says the quantity. If not, ask him how much he wants.
# Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
# You can limit the quantity to single digit number.

fruits = ["apple", "orange", "mango", "banana", "quava"] # creating a list for fruits

while True: 
    customer_input = input("Fruit vendor: What do you want to buy? ").lower() # get input from customer to order

    # Initialize quantity and order as zero
    total_quantity = 0
    order_details = []

    # Split the customer input into words
    words = customer_input .split()

    for word in words:
        if word.isdigit() and 0 < int(word) <= 9: #check whether number found in input
            # If a number is found, update the total quantity
            total_quantity = int(word)
        elif word in fruits:#check for the fruit name in input
            # If a fruit name is found, add it to the order details
            order_details.append((total_quantity, word))
            total_quantity = 0  # Reset total quantity

    # If no specific fruit was mentioned, choose the first fruit in the list
    if not order_details:
        order_details.append((total_quantity, fruits[0]))

    # Print the customer's order
    for quantity, chosen_fruit in order_details:
        if quantity > 0:
            print(f"Fruit vendor: You want {quantity} {chosen_fruit}.")

    another_purchase = input("Fruit vendor: Would you like to buy something else? (yes/no) ").lower()
    if another_purchase != "yes":
        print("Fruit vendor: Thank you for shopping with us!")
        break

#     output

#     Fruit vendor: What do you want to buy? 1 apple 3 orange
# Fruit vendor: You want 1 apple.
# Fruit vendor: You want 3 orange.
# Fruit vendor: Would you like to buy something else? (yes/no) no
# Fruit vendor: Thank you for shopping with us!