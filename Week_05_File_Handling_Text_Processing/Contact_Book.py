"""
TASK: 03 Contact Book

# Store contacts in a text file, each line containing
name,phone,email
Program must allow:
- Add contact
- Search contact (sequential search)
- Display all

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def add_contact(filename, name, phone, email):
    with open(filename, "a") as file:
        file.write(f"{name},{phone},{email}\n")

def search_contact(filename, name):
    with open(filename, "r") as file:
        contacts = file.readlines()
    for contact in contacts:
        if contact.split(",")[0].lower() == name.lower():
            return contact.strip("\n")

    return "Not found"

def display_contacts(filename):
    with open(filename, "r") as file:
        contacts = file.readlines()
    for contact in contacts:
        print(contact)

def main():
    filename = "contacts.txt"
    add_contact(filename, "Ben", "+44 372819372819", "test@gmail.com")
    add_contact(filename, "George", "+1 742193901", "bum@bum.co.uk")
    display_contacts(filename)
    print(search_contact(filename, "Ben"))
    print(search_contact(filename, "Jack"))


if __name__ == "__main__":
    main()
