class Wallet:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def transfer(self, other, amount):
        if amount <= 0 or self.balance < amount:
            return False
        self.balance -= amount
        other.balance += amount
        return True