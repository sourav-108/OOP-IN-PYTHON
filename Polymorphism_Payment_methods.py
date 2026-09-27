class CardPayment:
    def pay(self, amount):
        return f"Paid ${amount} by card"


class CashPayment:
    def pay(self, amount):
        return f"Paid ${amount} in cash"


def checkout(payment_method, amount):
    print(payment_method.pay(amount))


checkout(CardPayment(), 50)
checkout(CashPayment(), 20)