# - In this file, you have to add your tests on Transaction module.
# - See, app/transaction.py
# - Test transaction with different types - deposit, withdraw and transfer
# - Use mocks accordingly

from app.transaction import Transaction
from app.database import Database

import pytest
from unittest.mock import patch

@pytest.fixture
def mock_database():
    return Database("")

@patch('app.database.Database')
def test_deposit_positive_amount(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    transaction = Transaction(mock_db_instance)
    account_id = 1
    amount = 500
    initial_balance = 1000
    mock_db_instance.get_account.return_value = (account_id, None, None, initial_balance)
    transaction.deposit(account_id, amount)
    mock_db_instance.get_account.assert_called_once_with(account_id)
    mock_db_instance.update_account_balance.assert_called_once_with(account_id, initial_balance + amount)
    mock_db_instance.add_transaction.assert_called_once_with(None, account_id, amount, "deposit")

@patch('app.database.Database')
def test_withdraw_positive_amount(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    transaction = Transaction(mock_db_instance)
    account_id = 1
    amount = 500
    initial_balance = 1000
    mock_db_instance.get_account.return_value = (account_id, None, None, initial_balance)
    transaction.withdraw(account_id, amount)
    mock_db_instance.get_account.assert_called_once_with(account_id)
    mock_db_instance.update_account_balance.assert_called_once_with(account_id, initial_balance - amount)
    mock_db_instance.add_transaction.assert_called_once_with(account_id, None, amount, "withdrawal")

@patch('app.database.Database')
def test_transfer_positive_amount(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    transaction = Transaction(mock_db_instance)
    from_account_id = 1
    to_account_id = 2
    amount = 500
    initial_balance_from = 1000
    initial_balance_to = 2000
    mock_db_instance.get_account.side_effect = [
        (from_account_id, None, None, initial_balance_from),
        (to_account_id, None, None, initial_balance_to)
    ]
    transaction.transfer(from_account_id, to_account_id, amount)
    mock_db_instance.get_account.assert_any_call(from_account_id)
    mock_db_instance.get_account.assert_any_call(to_account_id)
    mock_db_instance.update_account_balance.assert_any_call(from_account_id, initial_balance_from - amount)
    mock_db_instance.update_account_balance.assert_any_call(to_account_id, initial_balance_to + amount)
    mock_db_instance.add_transaction.assert_called_once_with(from_account_id, to_account_id, amount, "transfer")