class CardGateway:
    def charge(self, amount):
        return f"Card charged ${amount:.2f}"


class WalletGateway:
    def charge(self, amount):
        return f"Wallet charged ${amount:.2f}"


class Checkout:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def pay(self, amount):
        return self.payment_gateway.charge(amount)


checkout = Checkout(WalletGateway())
print(checkout.pay(35))