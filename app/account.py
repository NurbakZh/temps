class Account:

    def __init__(self, database, customer_id=None, account_type="checking", balance=0.0):
        self.database = database
        self.balance = balance
        if customer_id:
            self.account_id = self._create_account(customer_id, account_type, balance)

    def _create_account(self, customer_id, account_type, balance):
        return self.database.add_account(customer_id, account_type, balance)

    def delete_account(self, account_id):
        self.database.delete_account(account_id)
