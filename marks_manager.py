marks = []



while True:
    students_mark = input(f"Enter students mark or (e) to exit: ")
    if students_mark.isdigit():
        marks.append(students_mark)
        continue
    elif students_mark.lower() == "e":
        break
    else:
        print("invalid input")

print(marks)
        