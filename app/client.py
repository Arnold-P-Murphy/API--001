import json
import os
import uuid

CLIENTS_FILE = 'app/test_clients.json'  # Use a test-specific file for isolation

class Client:
    def __init__(self, first_name, last_name, phone, cellphone, address, city, province, postal_code, file_path):
        self.client_id = str(uuid.uuid4())  # Generate unique ID for each client
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.cellphone = cellphone
        self.address = address
        self.city = city
        self.province = province
        self.postal_code = postal_code
        self.file_path = file_path

    def to_dict(self):
        """Convert the client instance to a dictionary."""
        return {
            'client_id': self.client_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'phone': self.phone,
            'cellphone': self.cellphone,
            'address': self.address,
            'city': self.city,
            'province': self.province,
            'postal_code': self.postal_code
        }

    def is_duplicate(self, clients):
        """Check if the client already exists in the list by phone number."""
        return any(client['phone'] == self.phone for client in clients)

    def save(self):
        """Save the client to the JSON file, ensuring no duplicates."""
        clients = load_clients()

        if not self.is_duplicate(clients):
            clients.append(self.to_dict())
            with open(self.file_path, 'w') as file:
                json.dump(clients, file, indent=4)
        else:
            print("Duplicate client detected. Skipping save.")

def load_clients():
    """Load clients from the JSON file."""
    if os.path.exists(CLIENTS_FILE):
        with open(CLIENTS_FILE, 'r') as file:
            return json.load(file)
    return []
