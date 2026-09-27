class Inventory:
    def __init__(self):
        self.stock = {}

    def add(self, item, quantity):
        self.stock[item] = self.stock.get(item, 0) + quantity

    def sell(self, item, quantity):
        if self.stock.get(item, 0) < quantity:
            return "Not enough stock"
        self.stock[item] -= quantity
        return "Sold"