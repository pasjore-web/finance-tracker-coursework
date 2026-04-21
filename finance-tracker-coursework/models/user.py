class User:
    def __init__(self, name):
        self.name = name
        self.wallet = None
        self.limits = {
            "daily": None,
            "weekly": None,
            "monthly": None
        }

    def create_wallet(self):
        from models.wallet import Wallet
        self.wallet = Wallet()

    def add_transaction(self, transaction):
        if self.wallet is None:
            self.create_wallet()

        if transaction.__class__.__name__ == "ExpenseTransaction":
            if self.limits["daily"] is not None and transaction.amount > self.limits["daily"]:
                print("Daily limit exceeded!")
                return

            if self.limits["weekly"] is not None and transaction.amount > self.limits["weekly"]:
                print("Weekly limit exceeded!")
                return

            if self.limits["monthly"] is not None and transaction.amount > self.limits["monthly"]:
                print("Monthly limit exceeded!")
                return

        self.wallet.add_transaction(transaction)

    def remove_transaction(self, transaction_id):
        if self.wallet is None:
            return False
        return self.wallet.remove_transaction(transaction_id)

    def set_limit(self, period, amount):
        if period in self.limits:
            self.limits[period] = amount

    def show_data(self):
        if self.wallet:
            print(f"User: {self.name}")
            print("Balance:", self.wallet.show_balance())
            print("Limits:", self.limits)
            self.wallet.show_transactions()

    def to_dict(self):
        return {
            "name": self.name,
            "limits": self.limits,
            "wallet": self.wallet.to_dict() if self.wallet else None
        }