class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(price for name, price in self.items)


cart = ShoppingCart()
cart.add_item("Book", 200)
cart.add_item("Pen", 20)
print(cart.total())          # 220