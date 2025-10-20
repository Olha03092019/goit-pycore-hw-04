def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added"
    except ValueError:
        return "Error: please provide both name and phone"


def update_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated"
        else:
            return "Contact not found"
    except ValueError:
        return "Error: please provide both name and phone"


def get_contact(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found"
    except IndexError:
        return "Error: please provide a name"


def get_all_contacts(contacts):
    if not contacts:
        return "No contacts found"
    return "\n".join(f"{name}:{phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(update_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
