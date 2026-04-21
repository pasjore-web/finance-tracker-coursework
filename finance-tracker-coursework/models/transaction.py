from datetime import datetime
import uuid


class Transaction:
    def __init__(self, amount, category, description, transaction_id=None, created_at=None):
        self.transaction_id = transaction_id if transaction_id else str(uuid.uuid4())[:8]
        self.amount = amount
        self.category = category
        self.description = description
        self.created_at = created_at if created_at else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def apply(self, wallet):
        raise NotImplementedError("Subclasses must implement this method")

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "created_at": self.created_at,
            "type": self.__class__.__name__
        }


class IncomeTransaction(Transaction):
    def apply(self, wallet):
        wallet.balance += self.amount


class ExpenseTransaction(Transaction):
    def apply(self, wallet):
        wallet.balance -= self.amount