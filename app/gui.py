import tkinter as tk
from tkinter import messagebox

class ClientManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Client Manager")
        
        # Create menu
        self.create_menu()

        self.create_widgets()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.exit_app)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Client Management menu
        client_menu = tk.Menu(menu_bar, tearoff=0)
        client_menu.add_command(label="Create New Client", command=self.create_client)
        client_menu.add_command(label="Search Client", command=self.search_client)
        client_menu.add_command(label="Show All Clients", command=self.show_all_clients)
        menu_bar.add_cascade(label="Client Management", menu=client_menu)

        # Configure the root window to display the menu
        self.root.config(menu=menu_bar)

    def create_widgets(self):
        label = tk.Label(self.root, text="Client Manager", font=("Helvetica", 16))
        label.pack(anchor="w", padx=10, pady=10)

        # Buttons for actions (Create, Search, Show)
        self.create_button = tk.Button(self.root, text="Create New Client", command=self.create_client)
        self.create_button.pack(anchor="w", padx=10, pady=5)

    def create_client(self):
        create_client_window = tk.Toplevel(self.root)
        create_client_window.title("Create New Client")

        # Add input fields for client data
        tk.Label(create_client_window, text="First Name:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        first_name_entry = tk.Entry(create_client_window)
        first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Add more fields for last name, phone, etc.

        # Save client action
        def save_client():
            messagebox.showinfo("Success", "Client Created Successfully!")

        save_button = tk.Button(create_client_window, text="Save Client", command=save_client)
        save_button.grid(row=8, column=0, columnspan=2, pady=10)

    def search_client(self):
        # Add functionality to search for clients
        messagebox.showinfo("Search", "Search for clients functionality goes here.")

    def show_all_clients(self):
        # Add functionality to display all clients
        messagebox.showinfo("Show Clients", "Display all clients functionality goes here.")

    def exit_app(self):
        self.root.quit()

def run_gui():
    root = tk.Tk()
    app = ClientManagerApp(root)
    root.mainloop()
