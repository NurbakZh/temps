# - In this file, you have to write an E2E test on Bank project.
# - See, app/bank.py
# - For understanding purposes, you can interact with main.py
# - Create a real life usage scenario for this project and follow the order for testing components
# - Make sure that the test tests almost all of the functionalities of the project.
import os

import pytest
from app.bank import Bank

@pytest.fixture
def bank():
    return Bank(db_path='db')

def test_customer_operations(bank):
    customer_id = bank.add_customer("Maks", "Universitetskaaya 1")
    assert customer_id is not None

    customers = bank.get_all_customers()
    assert len(customers) >= 1

    bank.update_customer_details(customer_id, "Maks New", "Universitetskaaya 1/3")
    updated_customer = bank.get_all_customers()[0]
    print(updated_customer)
    assert updated_customer[1] == "Maks New"

    bank.delete_customer(customer_id)
    customers_after_delete = bank.get_all_customers()
    assert len(customers_after_delete) == 0

def test_account_operations(bank):
    customer_id = bank.add_customer("Nikita", "Universitetskaya 1/1")
    account_id = bank.open_account(customer_id, "deposit", 1000)
    assert account_id is not None

    account = bank.get_account(account_id)
    assert account[1] == customer_id

    bank.deposit_to_account(account_id, 500)
    account = bank.get_account(account_id)
    assert account[3] == 1500

    bank.withdraw_from_account(account_id, 200)
    account = bank.get_account(account_id)
    assert account[3] == 1300

    bank.close_account(account_id)
    closed_account = bank.get_account(account_id)
    assert closed_account is None

def test_transfer_between_accounts(bank):
    customer_id = bank.add_customer("Nikita", "Universitetskaya 1/1")
    account1_id = bank.open_account(customer_id, "deposit", 1000)
    account2_id = bank.open_account(customer_id, "sending", 2000)

    bank.transfer_between_accounts(account1_id, account2_id, 500)
    account1 = bank.get_account(account1_id)
    account2 = bank.get_account(account2_id)
    assert account1[3] == 500
    assert account2[3] == 2500

def test_get_account_transactions(bank):
    customer_id = bank.add_customer("Nikita", "Universitetskaya 1/1")
    account_id = bank.open_account(customer_id, "deposit", 1000)

    transactions = bank.get_account_transactions(account_id)
    assert len(transactions) == 0

    bank.deposit_to_account(account_id, 500)
    bank.withdraw_from_account(account_id, 200)

    transactions = bank.get_account_transactions(account_id)
    assert len(transactions) == 2

@pytest.fixture(scope="session", autouse=True)
def delete_test_database():
    db_file = 'db'
    yield
    if os.path.exists(db_file):
        os.remove(db_file)