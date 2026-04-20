from models.transaction import IncomeTransaction, ExpenseTransaction
from models.wallet import Wallet


def main():
    wallet = Wallet()

    wallet.add_transaction(IncomeTransaction(1000, "Salary", "Monthly salary"))
    wallet.add_transaction(ExpenseTransaction(200, "Food", "Groceries"))

    print("Balance:", wallet.show_balance())
    wallet.show_transactions()


if __name__ == "__main__":
    main()