from models.transaction import IncomeTransaction, ExpenseTransaction


class TransactionFactory:
    @staticmethod
    def create_transaction(transaction_type, amount, category, description):
        if transaction_type == "income":
            return IncomeTransaction(amount, category, description)
        elif transaction_type == "expense":
            return ExpenseTransaction(amount, category, description)
        else:
            raise ValueError("Invalid transaction type")