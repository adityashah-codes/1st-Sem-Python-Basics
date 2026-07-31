while True:

    action = input(
        "----Menu----\n"
        "1 - Read Diary\n"
        "2 - Write In Diary\n"
        "e - exit\n"
        "----> ") 

    if action == "1":

        with open("diary_content.txt")as file:
            data = file.read()
            print(data)

    elif action == "2":

        to_write = input("Enter the content to write:\n")

        with open("diary_content.txt", "a")as file:
            file.write(to_write  + "\n")

        print("Added content successfully")

    elif action.lower() == "e":
        break
