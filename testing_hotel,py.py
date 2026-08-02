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

room_list = {
    101: room_101,
    102: room_102,
    103: room_103
}

def search_menu():

    date = input("Enter Check-In Date (YYYY-MM-DD): ")
    duration = input("Enter Duration (Nights): ")
    category = int(input("Select Category [1: Standard, 2: Deluxe, 3: Suite]: "))
    return date, duration, category 


date, duration, action = search_menu()

selected_room = room_list[100 + action]
print(selected_room.room_name)

if selected_room.is_available():
    print("availabe")
    selected_room.status = False

else:
    print("unavailabe")



