class LocalDelivery:
    def calculate_fee(self, distance):
        return distance * 2


class ExpressDelivery:
    def calculate_fee(self, distance):
        return distance * 5


class DeliveryService:
    def __init__(self, pricing):
        self.pricing = pricing

    def fee_for(self, distance):
        return self.pricing.calculate_fee(distance)


delivery = DeliveryService(ExpressDelivery())
print(delivery.fee_for(4))  # 20