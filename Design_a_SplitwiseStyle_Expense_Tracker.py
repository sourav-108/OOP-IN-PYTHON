from collections import defaultdict


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return self.name


class Expense:
    def __init__(self, description, amount, paid_by, participants):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if not participants:
            raise ValueError("At least one participant is required")

        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.participants = participants


class ExpenseTracker:
    def __init__(self):
        self.users = {}
        self.expenses = []
        self.balances = defaultdict(float)

    def add_user(self, user):
        self.users[user.user_id] = user

    def add_expense(self, expense):
        self.expenses.append(expense)
        share = expense.amount / len(expense.participants)

        # The payer covered everyone's share.
        self.balances[expense.paid_by.user_id] += expense.amount

        for user in expense.participants:
            self.balances[user.user_id] -= share

    def settle(self):
        creditors = []
        debtors = []

        for user_id, balance in self.balances.items():
            if balance > 0.01:
                creditors.append([user_id, balance])
            elif balance < -0.01:
                debtors.append([user_id, -balance])

        payments = []
        i = j = 0

        while i < len(debtors) and j < len(creditors):
            debtor_id, debt = debtors[i]
            creditor_id, credit = creditors[j]
            amount = min(debt, credit)

            payments.append(
                (self.users[debtor_id], self.users[creditor_id], round(amount, 2))
            )

            debtors[i][1] -= amount
            creditors[j][1] -= amount

            if debtors[i][1] < 0.01:
                i += 1
            if creditors[j][1] < 0.01:
                j += 1

        return payments


# Example
Angan = User(1, "Angan")
Sourav = User(2, "Sourav")
Durjoy = User(3, "Durjoy")

tracker = ExpenseTracker()
for user in (Angan ,Sourav, Durjoy):
    tracker.add_user(user)

tracker.add_expense(
    Expense("Dinner", 90,Angan, [Angan ,Sourav, Durjoy])
)

for debtor, creditor, amount in tracker.settle():
    print(f"{debtor} pays {creditor}: ${amount:.2f}")