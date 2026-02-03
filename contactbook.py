

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print(" Contact added successfully\n")

def view_contacts():
    if not contacts:
        print(" No contacts found\n")
        return

    print("\n Contact List:")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()

def search_contact():
    keyword = input("Search by name or phone: ").lower()
    found = False

    for c in contacts:
        if keyword in c['name'].lower() or keyword in c['phone']:
            print("\n Contact Found:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}\n")
            found = True

    if not found:
        print(" No matching contact found\n")

def update_contact():
    view_contacts()
    if not contacts:
        return

    index = int(input("Enter contact number to update: ")) - 1
    if 0 <= index < len(contacts):
        c = contacts[index]
        print("Leave blank to keep old value")

        name = input(f"New name ({c['name']}): ") or c['name']
        phone = input(f"New phone ({c['phone']}): ") or c['phone']
        email = input(f"New email ({c['email']}): ") or c['email']
        address = input(f"New address ({c['address']}): ") or c['address']

        contacts[index] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        print(" Contact updated successfully\n")
    else:
        print(" Invalid selection\n")

def delete_contact():
    view_contacts()
    if not contacts:
        return

    index = int(input("Enter contact number to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        print(" Contact deleted successfully\n")
    else:
        print("Invalid selection\n")

def menu():
    while True:
        print("===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print(" Exiting Contact Book")
            break
        else:
            print(" Invalid choice\n")

menu()
