from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


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
        return "\n".join([f"Name: {contact.name} \n"
                          f"Phone: {contact.phone} \n"
                          f"Email: {contact.email} \n"
                          f"Address: {contact.address}"
                          "\n" for contact in self.contacts])

    def searchContactByName(self, name):
        return [f"Name: {contact.name} \n"
                f"Phone: {contact.phone} \n"
                f"Email: {contact.email} \n"
                f"Address: {contact.address}" for contact in self.contacts if name.lower() == contact.name.lower()]

    def searchContactByPhone(self, phone):
        return [f"Name: {contact.name} \n"
                f"Phone: {contact.phone} \n"
                f"Email: {contact.email} \n"
                f"Address: {contact.address}" for contact in self.contacts if phone == contact.phone]

    def updateContact(self, name, updatedName, updatedPhone, updatedEmail, updatedAddress):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.name = updatedName
                contact.phone = updatedPhone
                contact.address = updatedAddress
                contact.email = updatedEmail
                return "Contact updated successfully."

    def deleteContact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        return "Contact deleted successfully"


class ContactBookApp(App):
    def build(self):
        self.book = ContactBook()
        self.layout = BoxLayout(orientation='vertical')

        # Widgets
        self.label = Label(text="Welcome to the ContactBook!", size_hint=(1, 1))
        self.layout.add_widget(self.label)

        # Buttons
        self.buttons = [
            Button(text="Add Contact", on_press=self.createContact),
            Button(text="View Contact List", on_press=self.viewAllContacts),
            Button(text="Search Contact by Name", on_press=self.searchContactByName),
            Button(text="Search Contact by Number", on_press=self.searchContactByPhone),
            Button(text="Update Contact", on_press=self.updateContact),
            Button(text="Delete Contact", on_press=self.deleteContact),
            Button(text="Exit", on_press=self.exitApp)
        ]

        for button in self.buttons:
            self.layout.add_widget(button)

        return self.layout

    def createContact(self, instance):
        popup = Popup(title='Add Contact',
                      content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        # Add TextInput widgets for each contact attribute
        name_input = TextInput(hint_text='Name')
        phone_input = TextInput(hint_text='Phone')
        email_input = TextInput(hint_text='Email')
        address_input = TextInput(hint_text='Address')

        popup.content.add_widget(name_input)
        popup.content.add_widget(phone_input)
        popup.content.add_widget(email_input)
        popup.content.add_widget(address_input)

        # Add a button to save the contact
        save_button = Button(text='Save', on_press=lambda x: self.saveContact(name_input.text, phone_input.text,
                                                                               email_input.text, address_input.text, popup))
        popup.content.add_widget(save_button)

        # Open the popup
        popup.open()

    def saveContact(self, name, phone, email, address, popup):
        contact = Contact(name, email, phone, address)
        self.book.addContact(contact)
        popup.dismiss()

    def viewAllContacts(self, instance):
        popup = Popup(title='Contact List',
                      content=Label(text=self.book.viewAllContacts()),
                      size_hint=(None, None), size=(400, 300))
        popup.open()

    def searchContactByName(self, instance):
        popup = Popup(title='Search Contact by Name',
                      content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        name_input = TextInput(hint_text='Name')
        search_button = Button(text='Search',
                               on_press=lambda x: self.showSearchResult(self.book.searchContactByName(name_input.text), popup))
        popup.content.add_widget(name_input)
        popup.content.add_widget(search_button)

        popup.open()

    def searchContactByPhone(self, instance):
        popup = Popup(title='Search Contact by Phone',
                      content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        phone_input = TextInput(hint_text='Phone')
        search_button = Button(text='Search',
                               on_press=lambda x: self.showSearchResult(self.book.searchContactByPhone(phone_input.text), popup))
        popup.content.add_widget(phone_input)
        popup.content.add_widget(search_button)

        popup.open()

    def updateContact(self, instance):
        popup = Popup(title='Update Contact',
                      content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        name_input = TextInput(hint_text='Current Name')
        updated_name_input = TextInput(hint_text='Updated Name')
        updated_phone_input = TextInput(hint_text='Updated Phone')
        updated_email_input = TextInput(hint_text='Updated Email')
        updated_address_input = TextInput(hint_text='Updated Address')

        update_button = Button(text='Update',
                               on_press=lambda x: self.showUpdateResult(
                                   self.book.updateContact(name_input.text, updated_name_input.text, updated_phone_input.text,
                                                           updated_email_input.text, updated_address_input.text), popup))

        popup.content.add_widget(name_input)
        popup.content.add_widget(updated_name_input)
        popup.content.add_widget(updated_phone_input)
        popup.content.add_widget(updated_email_input)
        popup.content.add_widget(updated_address_input)
        popup.content.add_widget(update_button)

        popup.open()

    def deleteContact(self, instance):
        popup = Popup(title='Delete Contact',
                      content=BoxLayout(orientation='vertical', spacing=10),
                      size_hint=(None, None), size=(400, 300))

        name_input = TextInput(hint_text='Name')
        delete_button = Button(text='Delete',
                               on_press=lambda x: self.showDeleteResult(self.book.deleteContact(name_input.text), popup))

        popup.content.add_widget(name_input)
        popup.content.add_widget(delete_button)

        popup.open()

    def showSearchResult(self, result, popup):
        if result:
            popup.content = Label(text="\n".join(result))
        else:
            popup.content = Label(text="No matching contacts found.")
        popup.height = 150

    def showUpdateResult(self, result, popup):
        popup.content = Label(text=result)
        popup.height = 150

    def showDeleteResult(self, result, popup):
        popup.content = Label(text=result)
        popup.height = 150

    def exitApp(self, instance):
        self.stop()


if __name__ == "__main__":
    ContactBookApp().run()
