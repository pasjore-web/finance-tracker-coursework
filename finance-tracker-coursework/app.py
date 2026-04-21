from services.finance_manager import FinanceManager
from services.transaction_factory import TransactionFactory


def main():
    manager = FinanceManager()

    manager.add_user("Jonas")
    manager.add_user("Petras")
    manager.users["Jonas"].set_limit("daily", 300)
    manager.users["Jonas"].set_limit("monthly", 1000)

    t1 = TransactionFactory.create_transaction("income", 1200, "Salary", "Monthly salary")
    t2 = TransactionFactory.create_transaction("expense", 500, "Food", "Big groceries")
    t3 = TransactionFactory.create_transaction("income", 600, "Freelance", "Side project")
    t4 = TransactionFactory.create_transaction("expense", 100, "Transport", "Bus card")

    manager.add_transaction("Jonas", t1)
    manager.add_transaction("Jonas", t2)
    manager.add_transaction("Petras", t3)
    manager.add_transaction("Petras", t4)

    manager.show_user("Jonas")
    print("-----")
    manager.show_user("Petras")
  
    print("\n=== GROUP DEPOSIT ===")

    manager.group_deposit(
    ["Jonas", "Petras"],
    "income",
    200,
    "Bonus",
    "Group bonus"
    )

    manager.show_user("Jonas")
    print("-----")
    manager.show_user("Petras")


if __name__ == "__main__":
    main()