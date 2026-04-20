class Wallet:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_transaction(self, transaction):
        transaction.apply(self)
        self.transactions.append(transaction)

    def show_balance(self):
        return self.balance

    def show_transactions(self):
        for transaction in self.transactions:
            print(f"{transaction.category}: {transaction.amount} ({transaction.description})")
