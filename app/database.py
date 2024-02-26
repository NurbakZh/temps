import sqlite3

class Database:
    def __init__(self, db_path='bank.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            account_type TEXT NOT NULL,
            balance REAL NOT NULL,
            FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
        );""")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_account_id INTEGER,
            to_account_id INTEGER,
            amount REAL NOT NULL,
            transaction_type TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(from_account_id) REFERENCES accounts(account_id),
            FOREIGN KEY(to_account_id) REFERENCES accounts(account_id)
        );""")
        self.conn.commit()

    def add_customer(self, name, address):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO customers (name, address) VALUES (?, ?)
        """, (name, address))
        self.conn.commit()
        return cursor.lastrowid

    def update_customer(self, customer_id, name, address):
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE customers SET name = ?, address = ? WHERE customer_id = ?
        """, (name, address, customer_id))
        self.conn.commit()

    def get_customer(self, customer_id):
        """Retrieve a customer's details by their customer ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers WHERE customer_id = ?", (customer_id,))
        return cursor.fetchone()
    
    def delete_customer(self, customer_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        DELETE FROM customers WHERE customer_id = ?
        """, (customer_id,))
        self.conn.commit()

    def add_account(self, customer_id, account_type, balance):
        cursor = self.conn.cursor()
        cursor.execute("""
        INSERT INTO accounts (customer_id, account_type, balance) VALUES (?, ?, ?)
        """, (customer_id, account_type, balance))
        self.conn.commit()
        return cursor.lastrowid


    def get_account(self, account_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT account_id, customer_id, account_type, balance FROM accounts WHERE account_id = ?
        """, (account_id,))
        return cursor.fetchone()
    

    
    def get_customer_accounts(self, customer_id):
        """Retrieve all accounts associated with a customer by their customer ID."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE customer_id = ?", (customer_id,))
        
        return cursor.fetchall()

    def update_account_balance(self, account_id, balance):
        cursor = self.conn.cursor()
        cursor.execute("""
        UPDATE accounts SET balance = ? WHERE account_id = ?
        """, (balance, account_id))
        self.conn.commit()

    def delete_account(self, account_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        DELETE FROM accounts WHERE account_id = ?
        """, (account_id,))
        self.conn.commit()

    def add_transaction(self, from_account_id, to_account_id, amount, transaction_type):
        self.conn.execute("INSERT INTO transactions (from_account_id, to_account_id, amount, transaction_type) VALUES (?, ?, ?, ?)",
                          (from_account_id, to_account_id, amount, transaction_type))
        self.conn.commit()

    def get_transactions(self, account_id):
        cursor = self.conn.cursor()
        cursor.execute("""
        SELECT transaction_id, from_account_id, to_account_id, amount, transaction_type, timestamp 
        FROM transactions 
        WHERE from_account_id = ? OR to_account_id = ?
        """, (account_id, account_id,))
        return cursor.fetchall()

    def get_all_customers(self):
        """Retrieve all customers from the database."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM customers ORDER BY customer_id ASC")
        return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()
