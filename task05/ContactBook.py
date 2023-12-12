class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def addContact(self, contact):
        self.contacts.append(contact)

    def viewAllContacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name} \n"
                  f"Phone: {contact.phone} \n"
                  f"Email: {contact.email} \n"
                  f"Address: {contact.address}"
                  "\n")

    def searchContactByName(self, name):
        for contact in self.contacts:
            if name == contact.name:
                print(f"Name: {contact.name} \n"
                  f"Phone: {contact.phone} \n"
                  f"Email: {contact.email} \n"
                  f"Address: {contact.address}")

    def searchContactByPhone(self, phone):
        for contact in self.contacts:
            if phone == contact.phone:
                print(f"Name: {contact.name} \n"
                      f"Phone: {contact.phone} \n"
                      f"Email: {contact.email} \n"
                      f"Address: {contact.address}")

    def updateContact(self, name, updatedName, updatedPhone,
                      updatedEmail, updatedAddress):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.name = updatedName
                contact.phone = updatedPhone
                contact.address = updatedAddress
                contact.email = updatedEmail
                print("Contact updated successfully.")

    def deleteContact(self, name):
        self.contacts = [contact for contact in self.contacts
                         if contact.name.lower() is not name.lower()]
        print("Contact deleted successfully")

def createContact(book):
    name = input("Enter the name: ")
    phone = int(input("Enter the phone number: "))
    email = input("Enter the e-mail address: ")
    address = input("Enter the address: ")

    contact = Contact(name, email, phone, address)
    book.addContact(contact)

    print("Contact added successfully!")

def main():
    book = ContactBook()
    print("Welcome to the ContactBook!")

    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact by Name")
        print("4. Search Contact by Number")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")

        choice = int(input("enter your choice (1-7): "))

        if choice == 1:
            createContact(book)

        elif choice == 2:
            book.viewAllContacts()

        elif choice == 3:
            name = input("Enter the name to search: ")
            book.searchContactByName(name)

        elif choice == 4:
            phone = int(input("Enter the phone number: "))
            book.searchContactByPhone(phone)

        elif choice == 5:
            name = input("Enter the contact name you wish to update: ")
            updatedName = input("Enter the updated name: ")
            updatedPhone = int(input("Enter the updated number: "))
            updatedEmail = input("Enter the updated mail: ")
            updatedAddress = input("Enter the updated address: ")

            book.updateContact(name, updatedName, updatedPhone, updatedEmail, updatedAddress)

        elif choice == 6:
            name = input("Enter the name of contact you wish to delete: ")
            book.deleteContact(name)

        elif choice == 7:
            print("Thank you for using the ContactBook!")
            break
        else:
            print("Invalid entry. \n"
                  "Please Enter number between (1-7).")

if __name__ == "__main__":
    main()