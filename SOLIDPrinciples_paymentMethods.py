class CardPayment:
    def pay(self, amount):
        print(f"Paid ${amount} by card")


class WalletPayment:
    def pay(self, amount):
        print(f"Paid ${amount} by wallet")


def checkout(payment_method, amount):
    payment_method.pay(amount)


checkout(CardPayment(), 50)
checkout(WalletPayment(), 25)