class EmailSender:
    def send(self, message):
        print(f"Email: {message}")


class SMSSender:
    def send(self, message):
        print(f"SMS: {message}")


class OrderService:
    def __init__(self, notification_sender):
        self.notification_sender = notification_sender

    def confirm_order(self, order_id):
        self.notification_sender.send(f"Order {order_id} confirmed")


OrderService(EmailSender()).confirm_order("A104")
OrderService(SMSSender()).confirm_order("A104")