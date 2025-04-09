import os
import pytest
from app.client import Client  # Import the Client class

class TestClient:
    # Path to the test file
    test_file_path = 'apps/clients.json'

    def setup_method(self):
        """Ensure the test file exists before each test."""
        # Call the Client's initialize_file method to create the file and directory if they don't exist
        Client.initialize_file()

    def test_save_client(self):
        client = Client(
            first_name="John",
            last_name="Doe",
            phone1="123-456-7890",
            phone2="987-654-3210",
            address="123 Main St",
            city="City",
            state="State",
            postal_code="12345"
        )
        client.save_client()
        clients = Client.load_clients()
        assert len(clients) > 0  # Ensure that a client was added

    def test_search_by_name(self):
        client = Client(
            first_name="John",
            last_name="Doe",
            phone1="123-456-7890",
            phone2="987-654-3210",
            address="123 Main St",
            city="City",
            state="State",
            postal_code="12345"
        )
        client.save_client()
        found_clients = Client.search_by_name("John", "Doe")
        assert len(found_clients) > 0

    def test_search_by_phone(self):
        client = Client(
            first_name="Jane",
            last_name="Doe",
            phone1="555-555-5555",
            phone2="987-654-3210",
            address="123 Elm St",
            city="City",
            state="State",
            postal_code="12345"
        )
        client.save_client()
        found_clients = Client.search_by_phone("555-555-5555")
        assert len(found_clients) > 0

    def test_show_clients_sorted(self):
        client1 = Client(
            first_name="Alice",
            last_name="Zebra",
            phone1="111-222-3333",
            phone2="444-555-6666",
            address="456 Oak St",
            city="City",
            state="State",
            postal_code="12345"
        )
        client2 = Client(
            first_name="Bob",
            last_name="Apple",
            phone1="333-444-5555",
            phone2="777-888-9999",
            address="789 Pine St",
            city="City",
            state="State",
            postal_code="12345"
        )
        client1.save_client()
        client2.save_client()
        sorted_clients = Client.show_clients_sorted()
        assert sorted_clients[0]['last_name'] == 'Apple'
        assert sorted_clients[1]['last_name'] == 'Zebra'

    def test_no_clients(self):
        clients = Client.load_clients()
        assert len(clients) == 0  # Ensure there are no clients initially
