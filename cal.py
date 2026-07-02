a = input("First number: ")
b = input("second number: ")
c = int(a) + int(b)
d = int(a) - int(b)
e = int(a) * int(b)
f = int(a) / int(b)
g = input("Choose Your Operation \n A - Addition \n S - Subtraction \n M _ Multiplication \n D - Divison \n ")
if g.upper() == "A":
    print(c)
elif g.upper() == "S":
    print(d)
elif g.upper() == "M":
    print(e)
elif g.upper() == "D":
     if int(b) == 0:
        print("cant divide number by 0")
     else:   
        print(f)
else:
    print("something went wrong")                


