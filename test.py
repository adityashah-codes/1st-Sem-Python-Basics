wt = input("weight: ")
unit = input("kg(s) or L(s): ")
if unit.upper() == "KG":
    converted = float(wt) / 0.45
    print("your wieght in l(s) is " + str(converted))
else:
    converted = float(wt) * 0.45
    print(str(converted))
