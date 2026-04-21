from models.transaction import IncomeTransaction, ExpenseTransaction
from services.finance_manager import FinanceManager


def main():
    manager = FinanceManager()

    manager.add_user("Jonas")
    manager.add_user("Petras")

    manager.add_transaction("Jonas", IncomeTransaction(1200, "Salary", "Monthly salary"))
    manager.add_transaction("Jonas", ExpenseTransaction(250, "Food", "Groceries"))

    manager.add_transaction("Petras", IncomeTransaction(600, "Freelance", "Side project"))
    manager.add_transaction("Petras", ExpenseTransaction(100, "Transport", "Bus card"))

    print("=== BEFORE SAVE ===")
    manager.show_user("Jonas")
    print("-----")
    manager.show_user("Petras")

    manager.save_data("data/finance_data.json")
    print("\nData saved to file.\n")

    new_manager = FinanceManager()
    new_manager.load_data("data/finance_data.json")

    print("=== AFTER LOAD ===")
    new_manager.show_user("Jonas")
    print("-----")
    new_manager.show_user("Petras")


if __name__ == "__main__":
    main()