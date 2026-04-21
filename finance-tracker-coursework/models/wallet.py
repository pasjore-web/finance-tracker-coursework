class Wallet:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_transaction(self, transaction):
        transaction.apply(self)
        self.transactions.append(transaction)

    def remove_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                if transaction.__class__.__name__ == "IncomeTransaction":
                    self.balance -= transaction.amount
                elif transaction.__class__.__name__ == "ExpenseTransaction":
                    self.balance += transaction.amount

                self.transactions.remove(transaction)
                return True
        return False

    def show_balance(self):
        return self.balance

    def show_transactions(self):
        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            print(
                f"ID: {transaction.transaction_id} | "
                f"{transaction.category}: {transaction.amount} "
                f"({transaction.description}) | {transaction.created_at}"
            )

    def to_dict(self):
        return {
            "balance": self.balance,
            "transactions": [transaction.to_dict() for transaction in self.transactions]
        }
