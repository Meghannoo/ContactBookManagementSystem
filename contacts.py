import json
import os

class ContactBook:
    def __init__(self, file_name="contacts.json"):
        self.file_name = file_name
        self.contacts = []

    def load_contacts(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.contacts = json.load(file)
            print("Contacts loaded successfully.")
        else:
            print("No existing contact file found. Starting fresh.")

    def save_contacts(self):
        with open(self.file_name, "w") as file:
            json.dump(self.contacts, file, indent=4)
        print("Contacts saved successfully.")

    def add_contact(self):
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")

        # Validations
        if not name.isalpha():
            print("Error: Name must be a string.")
            return
        if not phone.isdigit():
            print("Error: Phone number must be an integer.")
            return
        if any(contact['Phone'] == phone for contact in self.contacts):
            print("Error: Phone number already exists.")
            return

        # Add new contact
        new_contact = {"Name": name, "Email": email, "Phone": phone, "Address": address}
        self.contacts.append(new_contact)
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for i, contact in enumerate(self.contacts, start=1):
            print(f" Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")

    def remove_contact(self):
        phone = input("Enter the Phone Number of the contact to remove: ")
        for contact in self.contacts:
            if contact["Phone"] == phone:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact removed successfully.")
                return
        print("Error: Contact not found.")

    def search_contact(self):
        phone = input("Enter the Phone Number to search: ")

        if not phone.isdigit():
            print("Error: Phone number must be numeric.")
            return

        results = [contact for contact in self.contacts if contact["Phone"] == phone]

        if not results:
            print("No matching contacts found.")
            return

        for contact in results:
            print(
                f"Name: {contact['Name']}, Email: {contact['Email']}, Phone: {contact['Phone']}, Address: {contact['Address']}")