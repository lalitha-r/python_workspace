class MenuItem:
    def __init__(self, name, quantity, price, profit_per_item):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.profit_per_item = profit_per_item
        self.items_sold = 0

    def is_available(self, qty):
        return self.quantity >= qty

    def update_stock(self, qty):
        if self.is_available(qty):
            self.quantity -= qty
            self.items_sold += qty
            return True
        return False

    def calculate_profit(self):
        return self.profit_per_item * self.items_sold
