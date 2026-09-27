class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock

    def sell(self, quantity):
        if quantity <= 0:
            return "Quantity must be positive"
        if quantity > self.__stock:
            return "Not enough stock"
        self.__stock -= quantity
        return "Sale complete"

    def stock_count(self):
        return self.__stock


product = Product("Coffee", 12)
print(product.sell(3))       # Sale complete
print(product.stock_count()) # 9