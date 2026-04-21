import json
from models.user import User
from models.wallet import Wallet
from models.transaction import IncomeTransaction, ExpenseTransaction


class FileHandler:
    @staticmethod
    def save_to_file(filename, users):
        data = {}

        for username, user in users.items():
            data[username] = user.to_dict()

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        users = {}

        for username, user_data in data.items():
            user = User(user_data["name"])
            user.limits = user_data["limits"]

            if user_data["wallet"] is not None:
                wallet = Wallet()
                wallet.balance = user_data["wallet"]["balance"]

                for transaction_data in user_data["wallet"]["transactions"]:
                    if transaction_data["type"] == "IncomeTransaction":
                        transaction = IncomeTransaction(
                            transaction_data["amount"],
                            transaction_data["category"],
                            transaction_data["description"],
                            transaction_data["transaction_id"],
                            transaction_data["created_at"]
                        )
                    else:
                        transaction = ExpenseTransaction(
                            transaction_data["amount"],
                            transaction_data["category"],
                            transaction_data["description"],
                            transaction_data["transaction_id"],
                            transaction_data["created_at"]
                        )

                    wallet.transactions.append(transaction)

                user.wallet = wallet

            users[username] = user

        return users