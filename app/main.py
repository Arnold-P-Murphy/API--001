from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
from pathlib import Path

app = FastAPI()

# Define the Pydantic model for Client
class Client(BaseModel):
    first_name: str
    last_name: str
    phone: str
    cellphone: str
    address: str
    city: str
    province: str
    postal_code: str

    class Config:
        orm_mode = True

# Define the path to the client data file
CLIENT_FILE = "/app/apps/clients.json"

# Utility function to create the clients.json file if it doesn't exist
def create_clients_file():
    """Create the clients.json file with an empty list if it doesn't exist."""
    if not Path(CLIENT_FILE).exists():
        # Ensure the directory exists
        Path(CLIENT_FILE).parent.mkdir(parents=True, exist_ok=True)
        # Create the file with an empty list
        with open(CLIENT_FILE, "w") as file:
            json.dump([], file, indent=4)

# Utility function to read clients from the JSON file
def read_clients():
    """Read the clients from the clients.json file."""
    create_clients_file()  # Ensure the file exists before reading
    with open(CLIENT_FILE, "r") as file:
        return json.load(file)

# Utility function to save clients to the JSON file
def save_clients(clients):
    """Save the list of clients to the clients.json file."""
    with open(CLIENT_FILE, "w") as file:
        json.dump(clients, file, indent=4)

# POST endpoint to add a client
@app.post("/clients")
async def create_client(client: Client):
    clients = read_clients()
    # Add the new client to the list
    clients.append(client.dict())
    save_clients(clients)
    return {"message": "Client added successfully!", "client": client}

# GET endpoint to retrieve all clients
@app.get("/clients", response_model=List[Client])
async def get_clients():
    clients = read_clients()
    return clients

# Search for clients by name
@app.get("/clients/search")
async def search_by_name(name: str):
    clients = read_clients()
    results = [client for client in clients if name.lower() in client["first_name"].lower() or name.lower() in client["last_name"].lower()]
    return results

# Search for clients by phone number
@app.get("/clients/search/phone")
async def search_by_phone(phone: str):
    clients = read_clients()
    results = [client for client in clients if phone in client["phone"] or phone in client["cellphone"]]
    return results

# GET endpoint to show all clients sorted by last name
@app.get("/clients/sorted", response_model=List[Client])
async def get_sorted_clients():
    clients = read_clients()
    sorted_clients = sorted(clients, key=lambda x: x["last_name"])
    return sorted_clients
