class Transaction:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def apply(self, wallet):
        raise NotImplementedError("Subclasses must implement this method")


class IncomeTransaction(Transaction):
    def apply(self, wallet):
        wallet.balance += self.amount


class ExpenseTransaction(Transaction):
    def apply(self, wallet):
        wallet.balance -= self.amount