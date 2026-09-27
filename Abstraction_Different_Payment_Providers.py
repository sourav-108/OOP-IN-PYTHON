from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentProvider):
    def pay(self, amount):
        return f"Card charged ${amount}"


class WalletPayment(PaymentProvider):
    def pay(self, amount):
        return f"Wallet charged ${amount}"


def checkout(provider, amount):
    print(provider.pay(amount))


checkout(CardPayment(), 75)
checkout(WalletPayment(), 30)