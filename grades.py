print("----STUDENTS GRADE ANALYZIER----")
a = []
while True:
    b = input("Enter students Grade or 'done' to exit : ")
    if b.lower() == "done":
        break
    c = int(b)
    a.append(c)
if len(a) == 0:
    print("NO grades were entered")
else:
    total = sum(a)
    num_std = len(a)
    avg = total / num_std
    max = max(a)
    min = min(a)
print("\n----DATA----\n TOTAL MARKS : " + str(total) + "\n TOTAL NUMBER OF STUDENTS : " + str(num_std) + "\n AVERAGE MARKS : " + str(avg) + "\n MAXIMUM MARKS : " + str(max) + "\n MINIMUM MARKS : " + str(min)) 