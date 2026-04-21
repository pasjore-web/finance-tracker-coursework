import unittest
from services.finance_manager import FinanceManager
from services.transaction_factory import TransactionFactory


class TestFinanceTracker(unittest.TestCase):

    def test_add_transaction(self):
        manager = FinanceManager()
        manager.add_user("Test")

        t = TransactionFactory.create_transaction("income", 100, "Test", "Test income")
        manager.add_transaction("Test", t)

        user = manager.users["Test"]
        self.assertEqual(user.wallet.balance, 100)

    def test_remove_transaction(self):
        manager = FinanceManager()
        manager.add_user("Test")

        t = TransactionFactory.create_transaction("income", 100, "Test", "Test income")
        manager.add_transaction("Test", t)

        transaction_id = manager.users["Test"].wallet.transactions[0].transaction_id
        manager.remove_transaction("Test", transaction_id)

        self.assertEqual(manager.users["Test"].wallet.balance, 0)

    def test_limit(self):
        manager = FinanceManager()
        manager.add_user("Test")

        manager.users["Test"].set_limit("daily", 50)

        t = TransactionFactory.create_transaction("expense", 100, "Test", "Too big")
        manager.add_transaction("Test", t)

        self.assertEqual(manager.users["Test"].wallet.balance, 0)
        self.assertEqual(len(manager.users["Test"].wallet.transactions), 0)

if __name__ == "__main__":
    unittest.main()