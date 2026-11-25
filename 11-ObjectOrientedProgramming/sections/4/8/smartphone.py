from contact import Contact
from contact_list import Contact_List

contacts = Contact_List() # stworzenie listy kontaktow
contacts.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
contacts.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
contacts.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))
contacts.show_contacts() # wyswietlenie kontaktow
