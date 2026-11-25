class Contact_List:
    def __init__(self):
        self.contacts = [] # lista kontaktow

    def add_contact(self, contact):
        self.contacts.append(contact) # dodanie kontaktu

    def show_contacts(self):
        for contact in self.contacts:
            print(contact.name, contact.email, contact.telephone)
