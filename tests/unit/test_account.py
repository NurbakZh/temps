# - In this file, you have to add your tests on Account module.
# - See, app/account.py
# - Test account creation and deletion
# - Use mocks

from app.account import Account
from app.database import Database

import pytest
from unittest.mock import patch

@pytest.fixture
def db():
    return Database("")

@patch('app.database.Database')
def test_account_creation(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_account.return_value = 26
    account = Account(mock_db_instance, customer_id=1, account_type="checking", balance=1000.0)
    assert account.account_id == 26
    mock_db_instance.add_account.assert_called_once_with(1, "checking", 1000.0)

@patch('app.database.Database')
def test_delete_account(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_account.return_value = 26
    mock_db_instance.get_account.return_value = (26, 1, "checking", 1000.0)
    account = Account(mock_db_instance, customer_id=1, account_type="checking", balance=1000.0)
    account.delete_account(account.account_id)
    mock_db_instance.delete_account.assert_called_once_with(account.account_id)