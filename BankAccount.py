class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return "Withdrawal successful"

    def get_balance(self):
        return self.balance


account = BankAccount(100)
account.withdraw(30)
print(account.get_balance())    # 70