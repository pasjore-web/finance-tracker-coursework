from models.user import User
from services.file_handler import FileHandler


class FinanceManager:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = User(name)

    def add_transaction(self, username, transaction):
        user = self.users.get(username)
        if user:
            user.add_transaction(transaction)

    def remove_transaction(self, username, transaction_id):
        user = self.users.get(username)
        if user:
            return user.remove_transaction(transaction_id)
        return False

    def show_user(self, username):
        user = self.users.get(username)
        if user:
            user.show_data()

    def save_data(self, filename):
        FileHandler.save_to_file(filename, self.users)

    def load_data(self, filename):
        self.users = FileHandler.load_from_file(filename)