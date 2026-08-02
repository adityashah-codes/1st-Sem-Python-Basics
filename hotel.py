print(
    "---------------------------------\n" \
    "             HOTEL\n" \
    "---------------------------------\n")

import datetime

class rooms:

    def __init__(self, room_no, room_name, max_occupancy, room_rate, status):
        self.room_no = room_no
        self.room_name = room_name
        self.max_occupancy = max_occupancy
        self.room_rate = room_rate
        self.status = status   

    def is_available(self):
        return self.status 



room_101 = rooms(101, "Standard", 2,  "800$", True)
room_102 = rooms(102, "Delux", 3, "2000$", True)
room_103 = rooms(103, "Suite", 1, "3000$", True)

all_room = {
    101: room_101,
    102: room_102,
    103: room_103
}


def menu():

    choice = input("" \
    "      [MAIN MENU]\n\n" \
    "1. Search Available Rooms\n" \
    "2. Create New Reservation\n" \
    "3. Modify / Cancel Reservation\n" \
    "4. Process Check-Out & Generate Invoice\n" \
    "5. Exit\n\n"
    "Select Option (1-5): ")
    return choice

def search_menu():

    date = input("Enter Check-In Date (YYYY-MM-DD): ")
    duration = input("Enter Duration (Nights): ")
    category = int(input("Select Category [1: Standard, 2: Deluxe, 3: Suite]: "))
    return date, duration, category 

while True:

    menu_choice = menu()

    if menu_choice == "1":
        date, duration, category = search_menu()
        searched_room = all_room[100 + category]
        if searched_room.is_available():
            print("Room is available.")
            ask_for_booking = input("Do you want book room (y/n): ")
            if ask_for_booking.lower() == "y":
                print("Room booked succesfully.")
                searched_room.status = False
        else:
            print("room currently unavilabe")

    elif menu_choice == "2":
        pass

    elif menu_choice == "3":
        pass

    elif menu_choice == "4":
        pass

    elif menu_choice == "5":
        break

    else:
        continue