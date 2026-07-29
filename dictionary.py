contacts = {}

while True:

    action = input("----Menu----\n"
    "Enter the respective index no for the following task\n"
    "1 - Add contact\n"
    "2 - Search contact\n"
    "3 - Delete COntact\n"
    "4 - List all contact\n"
    "e - exit")

    if action.isdigit():

        if action == "1":
            name = input("Enter name: ")
            phone_no = input("Enter Phone number: ")
            contacts[name] = phone_no

        elif action == 1:
            pass
        
        elif action == 3:
            pass

        elif action == 4:
            pass

    elif action.lower() == "e":
        break

    else:
        continue 

print(contacts)        

