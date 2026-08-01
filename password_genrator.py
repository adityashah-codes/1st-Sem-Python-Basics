import secrets
import string

characters = string.ascii_letters + string.digits + string.punctuation

while True:

    try:
        length_of_password = int(input("Enter the length of password: "))
        if length_of_password <= 0:
            print("Please enter a Positive integer")
            continue
    except ValueError:
        print("Choose an integer(e.g. 8,10)")
        continue

    genrated_password = ''.join(secrets.choice(characters) for _ in range (length_of_password))

    print(f"Your genrated password: {genrated_password}")

    again = input("Do you want to contiue? (y/n): ")

    if again.lower() != "y":
        break