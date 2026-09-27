from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Enter a valid amount"
        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount
        return f"Withdrawal complete. Balance: ${self.balance}"


account = SavingsAccount(500)
print(account.withdraw(100))