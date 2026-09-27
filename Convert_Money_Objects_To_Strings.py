class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"${self.amount:.2f}"


price = Money(12.5)
print(price)               # $12.50