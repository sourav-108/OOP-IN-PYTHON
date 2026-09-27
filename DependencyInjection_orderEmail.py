class EmailSender:
    def send(self, address, message):
        print(f"Email sent to {address}: {message}")


class OrderService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def confirm_order(self, customer_email, order_id):
        message = f"Your order {order_id} is confirmed."
        self.email_sender.send(customer_email, message)


sender = EmailSender()
orders = OrderService(sender)
orders.confirm_order("username@example.com", "A104")