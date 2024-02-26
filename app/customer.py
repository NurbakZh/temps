class Customer:
    def __init__(self, database, customer_id=None, name=None, address=None):
        self.database = database
        self.customer_id = customer_id
        if customer_id is None and name and address:
            self.customer_id = self.database.add_customer(name, address)
        elif customer_id:
            self._load_customer()

    def _load_customer(self):
        details = self.database.get_customer(self.customer_id)
        if details:
            self.name, self.address = details[1], details[2]
        else:
            raise ValueError("Customer does not exist.")

    def update_details(self, name, address):
        self.database.update_customer(self.customer_id, name, address)

    def delete_customer(self):
        self.database.delete_customer(self.customer_id)
