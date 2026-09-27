from abc import ABC, abstractmethod

class Shipping(ABC):
    @abstractmethod
    def calculate_cost(self, weight):
        pass


class LocalShipping(Shipping):
    def calculate_cost(self, weight):
        return weight * 2


class InternationalShipping(Shipping):
    def calculate_cost(self, weight):
        return weight * 8


def show_shipping_cost(method, weight):
    print(method.calculate_cost(weight))


show_shipping_cost(LocalShipping(), 3)
show_shipping_cost(InternationalShipping(), 3)