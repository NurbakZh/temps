# - In this file, you have to add your tests on Database module.
# - See, app/database.py
# - Test most of the methods
# - Use mocks in proper parts

from app.database import Database
from unittest.mock import patch
import pytest

@pytest.fixture
def db():
    return Database('')

@patch('app.database.Database')
def test_add_customer(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_customer.return_value = 1
    assert mock_db_instance.add_customer('Maks', 'Universitetskaya 1') == 1
    mock_db_instance.add_customer.assert_called_once_with('Maks', 'Universitetskaya 1')

@patch('app.database.Database')
def test_get_customer(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.get_customer.return_value = (1, 'Maks', 'Universitetskaya 1')
    customer = mock_db_instance.get_customer(1)
    assert customer[1] == 'Maks'
    assert customer[2] == 'Universitetskaya 1'

@patch('app.database.Database')
def test_update_customer(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_customer.return_value = 1
    mock_db_instance.get_customer.return_value = (1, 'Maks New', 'Universitetskaya 1/3')
    customer_id = mock_db_instance.add_customer('Maks', 'Universitetskaya 1')
    mock_db_instance.update_customer(customer_id, 'Maks New', 'Universitetskaya 1/3')
    updated_customer = mock_db_instance.get_customer(customer_id)
    assert updated_customer[1] == 'Maks New'
    assert updated_customer[2] == 'Universitetskaya 1/3'

@patch('app.database.Database')
def test_delete_customer(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_customer.return_value = 1
    mock_db_instance.get_customer.return_value = None
    customer_id = mock_db_instance.add_customer('Maks', 'Universitetskaya 1')
    mock_db_instance.delete_customer(customer_id)
    deleted_customer = mock_db_instance.get_customer(customer_id)
    assert deleted_customer is None

@patch('app.database.Database')
def test_add_account(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_account.return_value = 1
    customer_id = mock_db_class.add_customer('Maks', 'Universitetskaya 1')
    account_id = mock_db_class.add_account(customer_id, 'deposit', 1000.00)
    assert account_id is not None

@patch('app.database.Database')
def test_get_account(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_customer.return_value = 1
    mock_db_instance.add_account.return_value = 1
    mock_db_instance.get_account.return_value = (1, 1, 'deposit', 1000.00)
    customer_id = mock_db_instance.add_customer('Maks', 'Universitetskaya 1')
    account_id = mock_db_instance.add_account(customer_id, 'deposit', 1000.00)
    retrieved_account = mock_db_instance.get_account(account_id)
    assert retrieved_account[2] == 'deposit'
    assert retrieved_account[3] == 1000.00

@patch('app.database.Database.add_transaction')
def test_add_transaction(mock_add_transaction, db):
    db.add_transaction(1, 2, 100, 'deposit')
    mock_add_transaction.assert_called_once_with(1, 2, 100, 'deposit')
