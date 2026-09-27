class Order:
    def __init__(self, order_id, price):
        self.order_id = order_id
        self.price = price


class OnlineOrder(Order):
    def __init__(self, order_id, price, tracking_code):
        super().__init__(order_id, price)
        self.tracking_code = tracking_code


order = OnlineOrder("A501", 1200, "BD1013")
print(order.order_id, order.tracking_code)