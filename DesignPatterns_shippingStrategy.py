class StandardShipping:
    def calculate(self, weight):
        return weight * 2


class ExpressShipping:
    def calculate(self, weight):
        return weight * 5


class Checkout:
    def __init__(self, shipping):
        self.shipping = shipping

    def shipping_cost(self, weight):
        return self.shipping.calculate(weight)


checkout = Checkout(ExpressShipping())
print(checkout.shipping_cost(3))  # 15