from datetime import datetime, timedelta

class vitualclock:

    def __init__(self):
        self.current_time = datetime.now()

    def advance_time(self, hours=0, days=0):
        self.current_time += timedelta(hours=hours,days=days)
        print(f"Advanced Time by {timedelta(hours=hours,days=days)}\nCurrent Time: {self.current_time}")

    def revrse_time(self, hours=0, days=0):
        self.current_time -= timedelta(hours=hours,days=days)
        print(f"Reversed Time by {timedelta(hours=hours,days=days)}\nCurrent Time: {self.current_time}")

class rooms:

    def __init__(self, room_no, room_rate):
        self.room_no = room_no
        self.room_rate = room_rate
        self.booking_end_time = None

    def booking(self, starting_booking_time, duration):
        self.booking_end_time = starting_booking_time + timedelta(hours=duration)

    def is_available(self, current_time):
        if self.booking_end_time is None or self.booking_end_time <= current_time:
            return True
        else:
            return False

clock = vitualclock()

room_101 = rooms(101, 800)
room_102 = rooms(102, 2000)
room_103 = rooms(103, 3000)

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

print(
    "---------------------------------\n" \
    "             HOTEL\n" \
    "---------------------------------\n")

while True:

    menu_choice = menu()

    if menu_choice == "1":

        room_to_book = input("Which Room no you want to book(1-3): ")
        searched_room = all_room[100 + int(room_to_book)]

        if searched_room.is_available(clock.current_time):
            print("Room is available.")
            ask_for_booking = input("Do you want book room (y/n): ")

            if ask_for_booking.lower() == "y":
                ask_for_time = input("Enter Booking start time (dd-mm-yyyy HH:MM) or Enter For current time : ")
                if ask_for_time.strip():
                    booking_start_time = datetime.strp(ask_for_time,"%d-%m-%Y %H:%M")
                else:
                    booking_start_time = clock.current_time
                duration = input("Enter duration (in hrs): ")
                searched_room.booking(booking_start_time, float(duration))
                print("Room booked succesfully.")

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