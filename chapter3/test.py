from contacts import Contact, Supplier, ContactList
c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
print([c.name for c in Contact.all_contacts.search('John')])

