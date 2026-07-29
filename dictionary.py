contacts = {}

def validate_name(n):
    if not n or n.isdigit():
        print("Invalid Name")
        return True
    else:
        return False

def validate_number(n):
    if not n or not n.isdigit():
        print("Inavlid phone number.")
        return True
    else:
        return False


while True:

    action = input("----Menu----\n"
    "Enter the respective index no for the following task\n"
    "1 - Add contact\n"
    "2 - Search contact\n"
    "3 - Delete COntact\n"
    "4 - List all contact\n"
    "e - exit\n"
    "-----> ")

    if action.isdigit():

        if action == "1":

            name = input("Enter name: ")
            if validate_name(name):
                continue

            phone_no = input("Enter Phone number: ")
            if validate_number(phone_no):
                continue
            
            contacts[name] = phone_no

        elif action == "2":

            search_contact = input("Enter the name of contact for search: ")
            if validate_name(search_contact):
                continue

            if not search_contact in contacts:
                print(f"'{search_contact}' - no such contact found")
            
            else:
                print(f"Name: {search_contact}\nPhone Number: {contacts[search_contact]}")
        
        elif action == "3":

            del_contact = input("Enter the name of contact for search: ")
            
            if validate_name(del_contact):
                continue

            if not del_contact in contacts:
                print(f"'{del_contact}' - no such contact found")
                continue

            else:
                del contacts[del_contact]
                print(f"Contact deleted - {del_contact}(Phone no - {contacts[search_contact]})")
                continue
            
        elif action == "4":

            if not contacts:
                print("No contacts saved")
                continue

            print("----Saved Contacts----")

            for i,(key, value) in enumerate(contacts.items(), start=1):
                print(f"({i})Name: {key}\n   Phone no: {value}\n")

            print("-------------")
            continue


    elif action.lower() == "e":
        break

    else:
        continue 

print(contacts)        

