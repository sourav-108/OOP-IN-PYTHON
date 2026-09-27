class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total(self, discount_percent=0):
        subtotal = sum(product.price for product in self.products)
        return subtotal * (1 - discount_percent / 100)


cart = ShoppingCart()
cart.add_product(Product("Shoes", 60))
cart.add_product(Product("Socks", 10))
print(cart.total(10))  # 63.0