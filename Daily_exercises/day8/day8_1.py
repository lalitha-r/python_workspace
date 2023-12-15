# Identify which portion of the code can be written as a function in all the programs below

# Problem #1.
# Write a program for calculating the profit for railways.
# For first class tickets, the profit is 25% of the price + Rs100 for every ticket sold.
# For Second class tickets, the profit is 15% of the price + Rs70 for every ticket sold.
# For Third class tickets (i don't know if there is a third class), the profit is 5% of the price.

# Get the price and no of tickets sold for each class and calculate the total profit.
# Identity what calculation in the above problem can be written as a function
# and what the input and output should be.

def calc_profit(price, tickets_sold, profit, add_charge):
    return (profit * price + add_charge) * tickets_sold


def main():
    classes = ["First", "Second", "Third"]
    total_profit = 0

    for class_name in classes:
        price = float(input(f"Enter price for {class_name} class ticket: "))
        tickets_sold = int(
            input(f"Enter number of {class_name} class tickets sold: "))

        if class_name == "First":
            total_profit += calc_profit(price, tickets_sold, 0.25, 100)
        elif class_name == "Second":
            total_profit += calc_profit(price, tickets_sold, 0.15, 70)
        elif class_name == "Third":
            total_profit += calc_profit(price, tickets_sold, 0.05, 0)

    print("Total profit for the railways:", total_profit)


if __name__ == "__main__":
    main()
