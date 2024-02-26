from .bank import Bank

def print_menu():
    print("\n--- Bank System Main Menu ---")
    print("1. Add Customer")
    print("2. Update Customer Details")
    print("3. Delete Customer")
    print("4. Open Account")
    print("5. Close Account")
    print("6. Deposit")
    print("7. Withdraw")
    print("8. Transfer")
    print("9. View Customer Accounts")
    print("10. View Account Transactions")
    print("11. View All Customers")
    print("12. Exit")

def main():
    bank = Bank()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Customer name: ")
                address = input("Customer address: ")
                customer_id = bank.add_customer(name, address)
                print(f"Customer added with ID: {customer_id}")

            elif choice == "2":
                customer_id = int(input("Customer ID: "))
                name = input("New name: ")
                address = input("New address: ")
                bank.update_customer_details(customer_id, name, address)
                print("Customer details updated.")

            elif choice == "3":
                customer_id = int(input("Customer ID to delete: "))
                bank.delete_customer(customer_id)
                print("Customer deleted.")

            elif choice == "4":
                customer_id = int(input("Customer ID for new account: "))
                account_type = input("Account type (checking/savings): ")
                balance = float(input("Initial balance: "))
                account_id = bank.open_account(customer_id, account_type, balance)
                print(f"Account {account_id} opened.")

            elif choice == "5":
                account_id = int(input("Account ID to close: "))
                bank.close_account(account_id)
                print("Account closed.")

            elif choice == "6":
                account_id = int(input("Account ID for deposit: "))
                amount = float(input("Amount to deposit: "))
                bank.deposit_to_account(account_id, amount)
                print("Deposit successful.")

            elif choice == "7":
                account_id = int(input("Account ID for withdrawal: "))
                amount = float(input("Amount to withdraw: "))
                bank.withdraw_from_account(account_id, amount)
                print("Withdrawal successful.")

            elif choice == "8":
                from_account_id = int(input("From Account ID: "))
                to_account_id = int(input("To Account ID: "))
                amount = float(input("Amount to transfer: "))
                bank.transfer_between_accounts(from_account_id, to_account_id, amount)
                print("Transfer successful.")

            elif choice == "9":
                customer_id = int(input("Customer ID to view accounts: "))
                accounts = bank.get_customer_accounts(customer_id)
                for account in accounts:
                    print(account)

            elif choice == "10":
                account_id = int(input("Account ID to view transactions: "))
                transactions = bank.get_account_transactions(account_id)
                for transaction in transactions:
                    print(transaction)

            elif choice == "11":
                customers = bank.get_all_customers()
                for customer in customers:
                    print(f"ID: {customer[0]}, Name: {customer[1]}, Address: {customer[2]}")

            elif choice == "12":
                print("Exiting the bank system.")
                break

            else:
                print("Invalid choice, please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
