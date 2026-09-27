class OrderItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def subtotal(self):
        return self.quantity * self.price


class FoodOrder:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item.subtotal() for item in self.items)


order = FoodOrder("Sam")
order.add_item(OrderItem("Burger", 2, 8))
order.add_item(OrderItem("Juice", 1, 3))
print(order.total())  # 19