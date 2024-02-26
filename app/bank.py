from .database import Database
from .transaction import Transaction
from .customer import Customer
from .account import Account

class Bank:
    def __init__(self, db_path='bank.db'):
        self.database = Database(db_path)
        self.transaction_system = Transaction(self.database)

    def add_customer(self, name, address):
        """Add a new customer to the bank."""
        return self.database.add_customer(name, address)

    def update_customer_details(self, customer_id, name, address):
        """Update details for an existing customer."""
        self.database.update_customer(customer_id, name, address)

    def delete_customer(self, customer_id):
        """Remove a customer and their accounts from the bank."""

        accounts = self.database.get_customer_accounts(customer_id)
        for account in accounts:
            self.close_account(account[0])
        self.database.delete_customer(customer_id)

    def open_account(self, customer_id, account_type, balance):
        """Open a new account for an existing customer."""

        account = Account(self.database, customer_id=customer_id, account_type=account_type, balance=balance)
        return account.account_id

    def close_account(self, account_id):
        """Close an existing account."""

        self.database.delete_account(account_id)

    def deposit_to_account(self, account_id, amount):
        """Deposit money into an account."""
        self.transaction_system.deposit(account_id, amount)

    def withdraw_from_account(self, account_id, amount):
        """Withdraw money from an account."""
        self.transaction_system.withdraw(account_id, amount)

    def transfer_between_accounts(self, from_account_id, to_account_id, amount):
        """Transfer money between two accounts."""
        self.transaction_system.transfer(from_account_id, to_account_id, amount)

    def get_customer_accounts(self, customer_id):
        """Retrieve all accounts associated with a customer."""

        return self.database.get_customer_accounts(customer_id)

    def get_account_transactions(self, account_id):
        """Get a list of transactions for a specific account."""

        return self.database.get_transactions(account_id)

    def get_all_customers(self):
        """Retrieve all customers from the bank."""
        return self.database.get_all_customers()
    
    def get_account(self, account_id):
        """Retrieve details for a specific account."""
        return self.database.get_account(account_id)
    
    def close_connection(self):
        self.database.close()
