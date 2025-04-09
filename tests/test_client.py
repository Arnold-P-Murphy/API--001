import pytest
import os
from app.client import Client, load_clients

# Use a test client file path (to prevent overwriting your actual data)
client_file = 'app/test_clients.json'

# Clear the clients.json file before each test to ensure test isolation
@pytest.fixture(autouse=True)
def clear_client_file():
    if os.path.exists(client_file):
        os.remove(client_file)
    # Ensure it's created as an empty list for every test run
    with open(client_file, 'w') as f:
        f.write("[]")

def test_save_new_client():
    """Test saving a new client."""
    client = Client(
        first_name="John",
        last_name="Doe",
        phone="123-456-7890",
        cellphone="987-654-3210",
        address="123 Elm St",
        city="Springfield",
        province="IL",
        postal_code="62701",
        file_path=client_file
    )
    client.save()

    # Load clients and check the saved data
    clients = load_clients()
    assert len(clients) > 0
    assert clients[0]['first_name'] == "John"
    assert clients[0]['last_name'] == "Doe"
    assert clients[0]['phone'] == "123-456-7890"

def test_no_duplicate_clients():
    """Test saving a duplicate client (same phone number)."""
    client1 = Client(
        first_name="John",
        last_name="Doe",
        phone="123-456-7890",
        cellphone="987-654-3210",
        address="123 Elm St",
        city="Springfield",
        province="IL",
        postal_code="62701",
        file_path=client_file
    )
    client1.save()

    # Save the same client again (duplicate)
    client2 = Client(
        first_name="John",
        last_name="Doe",
        phone="123-456-7890",
        cellphone="987-654-3210",
        address="123 Elm St",
        city="Springfield",
        province="IL",
        postal_code="62701",
        file_path=client_file
    )
    client2.save()

    # Load clients and check that only one client with that phone number exists
    clients = load_clients()
    assert len(clients) == 1  # Only one client should be saved
    assert clients[0]['phone'] == "123-456-7890"

def test_adding_unique_client():
    """Test adding a unique client and ensuring it is added only once."""
    client1 = Client(
        first_name="Alice",
        last_name="Smith",
        phone="555-123-4567",
        cellphone="555-765-4321",
        address="456 Oak St",
        city="Chicago",
        province="IL",
        postal_code="60601",
        file_path=client_file
    )
    client1.save()

    # Assert that the client is saved
    clients = load_clients()
    assert len(clients) > 0
    assert clients[0]['first_name'] == "Alice"
    assert clients[0]['last_name'] == "Smith"
    assert clients[0]['phone'] == "555-123-4567"
