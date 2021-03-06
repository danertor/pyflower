<<<<<<< HEAD
class ContactList(list):
    def __init__(self):
        list.__init__(self)
        print("ContactList:" + str(type(self)))

    def search(self, name):
        """Return all contacts that contain the search value
        in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()  # class variable! shared by all instances of the class!

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        print("Contact:" + str(type(self)))


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send {} order to {}".format(order, self.name))


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here


class EmailableContact(Contact, MailSender):
    pass

=======
class ContactList(list):
    def __init__(self):
        list.__init__(self)
        print("ContactList:" + str(type(self)))

    def search(self, name):
        """Return all contacts that contain the search value
        in their name."""
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()  # class variable! shared by all instances of the class!

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)
        print("Contact:" + str(type(self)))


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send {} order to {}".format(order, self.name))


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here


class EmailableContact(Contact, MailSender):
    pass

>>>>>>> b829bcb465b0e32104dbe492037b6da0f67e9948
