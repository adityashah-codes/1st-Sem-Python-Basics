with open ("a.txt", "w") as file:
    file.write("1\n")
    file.write("2\n")
print("task done")

print("reading data")
with open ("a.txt" , "r") as file:
    data = file.read()
    print(data)
print("task 2 done")