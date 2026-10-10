contacts = {}

while True:
    print("\n1. Add")
    print("2. Search")
    print("3. Show all")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Name: ")
        print(contacts.get(name, "Not found"))
    elif choice == "3":
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    elif choice == "4":
        break
