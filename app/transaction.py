class Transaction:
    def __init__(self, database):
        self.database = database

    def deposit(self, account_id, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        account = self.database.get_account(account_id)
        if not account:
            raise ValueError("Account does not exist.")
        new_balance = account[3] + amount
        self.database.update_account_balance(account_id, new_balance)
        self.database.add_transaction(None, account_id, amount, "deposit")

    def withdraw(self, account_id, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        account = self.database.get_account(account_id)
        if account[3] < amount:
            raise ValueError("Insufficient funds.")
        new_balance = account[3] - amount
        self.database.update_account_balance(account_id, new_balance)
        self.database.add_transaction(account_id, None, amount, "withdrawal")

    def transfer(self, from_account_id, to_account_id, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        from_account = self.database.get_account(from_account_id)
        to_account = self.database.get_account(to_account_id)
        if from_account[3] < amount:
            raise ValueError("Insufficient funds in the source account.")
        self.database.update_account_balance(from_account_id, from_account[3] - amount)
        self.database.update_account_balance(to_account_id, to_account[3] + amount)
        self.database.add_transaction(from_account_id, to_account_id, amount, "transfer")
