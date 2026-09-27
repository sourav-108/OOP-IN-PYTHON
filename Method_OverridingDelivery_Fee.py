class Delivery:
    def fee(self):
        return 50


class ExpressDelivery(Delivery):
    def fee(self):
        return 120


regular = Delivery()
express = ExpressDelivery()

print(regular.fee())  # 50
print(express.fee())  # 120