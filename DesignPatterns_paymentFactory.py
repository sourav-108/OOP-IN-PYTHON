class CardPayment:
    def pay(self, amount):
        return f"Paid ${amount} by card"


class WalletPayment:
    def pay(self, amount):
        return f"Paid ${amount} by wallet"


class PaymentFactory:
    @staticmethod
    def create(method):
        if method == "card":
            return CardPayment()
        if method == "wallet":
            return WalletPayment()
        raise ValueError("Unsupported payment method")


payment = PaymentFactory.create("card")
print(payment.pay(50))