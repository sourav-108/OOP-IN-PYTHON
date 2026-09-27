class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Enter a positive amount"
        self.__balance += amount
        return "Deposit complete"

    def withdraw(self, amount):
        if amount <= 0:
            return "Enter a positive amount"
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return "Withdrawal complete"

    def get_balance(self):
        return self.__balance


account = BankAccount("Maya", 500)
account.deposit(100)
print(account.get_balance())  # 600