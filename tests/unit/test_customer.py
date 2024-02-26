# - In this file, you have to add your tests on Customer module.
# - See, app/customer.py
# - Test customer creation, loading, updating and deletion
# - Use mocks

from app.customer import Customer
from app.database import Database
import pytest
from unittest.mock import patch

@pytest.fixture
def db():
    return Database('')

@patch('app.database.Database')
def test_customer_initialization(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    mock_db_instance.add_customer.return_value = 26
    customer = Customer(mock_db_instance, name='Maks', address='Universitetskaya 1')
    assert customer.customer_id is not None
    mock_db_instance.add_customer.assert_called_once_with('Maks', 'Universitetskaya 1')

@patch('app.database.Database')
def test_customer_loading(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    customer_id = 26
    mock_db_instance.get_customer.return_value = (customer_id, 'Maks', 'Universitetskaya 1')
    customer = Customer(mock_db_instance, customer_id=customer_id)
    assert customer.name == 'Maks'
    assert customer.address == 'Universitetskaya 1'

@patch('app.database.Database')
def test_update_customer_details(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    customer_id = 26
    mock_db_instance.add_customer.return_value = customer_id
    customer = Customer(mock_db_instance, customer_id=customer_id, name='Maks', address='Universitetskaya 1')
    customer.update_details('Maks New', 'Universitetskaya 1/3')
    mock_db_instance.update_customer.assert_called_once_with(customer_id, 'Maks New', 'Universitetskaya 1/3')

@patch('app.database.Database')
def test_delete_customer(mock_db_class):
    mock_db_instance = mock_db_class.return_value
    customer_id = 26
    mock_db_instance.add_customer.return_value = customer_id
    customer = Customer(mock_db_instance, customer_id=customer_id)
    customer.delete_customer()
    mock_db_instance.delete_customer.assert_called_once_with(customer_id)