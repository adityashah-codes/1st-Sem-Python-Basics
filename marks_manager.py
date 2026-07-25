import json

def load_data():

    try:

        with open("students_data.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}   

def save_data(data):
    

        with open("students_data.json", "w") as file:
            json.dump(data, file, indent=4)

students = load_data()

while True:

    action = input(
    "----MENU----" \
    "\n\nEnter the respective number for the mentioned task" \
    "\n\nAdd new students Data - '1'" \
    "\nCheck old students Data - '2'" \
    "\nCheck all students Data - '3'" \
    "\nChange students Data- '4'" \
    "\nExit - 'e'"
    "\n\n----->")
    
    if action == "1":

        roll_no = input("Enter Roll NO. : ")

        if roll_no in students:
            print(f"Roll no ({roll_no}) already exists.")
        else:
            students_name = input("Enter students name:")
            students_mark = input("Enter students mark : ")
            
            students[roll_no] ={
                "Name": students_name,
                "Marks": students_mark
            }

        save_data(students)
        print("Data saved succesfully.")
        continue

    elif action == "2":

        roll_no = input("Enter Roll no: ")

        if roll_no in students:
            student = students[roll_no]
            print(f"Name:{student['Name']}\nMarks:{student['Marks']}")            
        else:
            print(f"Roll No '{roll_no}' doesn't exists.")
            continue

    elif action == "3":
        if not students:
            print("No records found")
        else:
            for roll_no, info in students.items():
                print(f"{roll_no}\t|\t{info['Name']}\t|\t{info['Marks']}")
    elif action == "4":

        roll_no = input("Enter the Roll number: ")

        if roll_no in students:

            while True:

                action_for_change = input(
                "----Menu----"
                "Enter '1' for changing name\n" \
                "Enter '2' for changing students mark\n"
                "Enter 'e' to exit" \
                "----> ")

                if action_for_change == "1":
                    new_name = input("Enter new name: ")
                    students[roll_no]["Name"] = new_name
                    print("Students name updated successfully.")
                    break
                    
                elif action_for_change == "2":
                    new_mark = input("Enter new Mark: ")
                    students[roll_no]["Marks"] = new_mark
                    print("Students Mark updated successfully.")
                    break
                                        

                elif action_for_change == "e":
                    break

                else:
                    print(f"Invalid input-'{action_for_change}',\nEnter Valid input from the given list.")
                    continue

        else:
            print(f"Roll No '{roll_no}' doesn't exists.")
            continue
            

    elif action.lower() == "e":
        break

    else:
        print(f"Invalid input-'{action}',\nEnter Valid input from the given list.")
        continue



















