import pickle

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

class ContactList:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def add_contact(self, name, phone, email, address):
        """Add a new contact to the list."""
        if name in self.contacts:
            print("Contact with this name already exists.")
        else:
            self.contacts[name] = Contact(name, phone, email, address)
            print(f"Contact {name} added successfully.")

    def delete_contact(self, name):
        """Delete a contact from the list."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact with name {name} does not exist.")

    def view_contacts(self):
        """View all contacts."""
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts.values():
                print(contact)
                print("-" * 30)

    def edit_contact(self, name):
        """Edit an existing contact."""
        if name in self.contacts:
            print(f"Editing contact: {name}")
            phone = self.contacts.get('phone',input("Enter new phone number: "))
            email = self.contacts.get('email',input("Enter new email: "))
            address =self.contacts.get('address', input("Enter new address: "))
            self.contacts[name] = Contact(name, phone, email, address)
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact with name {name} does not exist.")

    def save_contacts(self):
        """Save contacts to a file."""
        with open('contacts.pkl', 'wb') as f:
            pickle.dump(self.contacts, f)
            print("Contacts saved successfully.")

    def load_contacts(self):
        """Load contacts from a file if available."""
        try:
            with open('contacts.pkl', 'rb') as f:
                self.contacts = pickle.load(f)
                print("Contacts loaded successfully.")
        except (FileNotFoundError, EOFError):
            print("No previous contacts found, starting fresh.")

def main():
    contact_list = ContactList()

    while True:
        print("\nContact List Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Delete Contact")
        print("4. Edit Contact")
        print("5. Save Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_list.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_list.view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            contact_list.delete_contact(name)
        elif choice == '4':
            name = input("Enter the name of the contact to edit: ")
            contact_list.edit_contact(name)
        elif choice == '5':
            contact_list.save_contacts()
        elif choice == '6':
            contact_list.save_contacts()
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
