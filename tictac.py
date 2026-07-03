import random
while True:
    print("\n----TIC-TAC----")
    a = ['Rock', 'Paper', 'Scissor']
    b = random.choice(a) # Computer's Choice
    c = str(input("----ENTER YOUR CHOICE----\n R for Rock \n P for Paper \n S for Scissor \n E for exit \n---->")) #User's Choice
    if c.upper() == "E":
        print("Well Played ;)")
        break
    else:
        if b == "Rock":
            if c.upper() == "P":
                print("Congrats , YOU WON!!")
            elif c.upper() == "S":
                print("you lost :( ")
            elif c.upper() == "R":
                print("Opps!! , its DRAW")
            else:
                print("Please Choose from (R/P/S/E) :")
        elif b == "Paper":
            if c.upper() == "S":
                print("Congrats , YOU WON!!")
            elif c.upper() == "R":
                print("you lost :(")
            elif c.upper() == "P":
                print("Oops!! , it's DRAW")
            else:
                print("Please Choose from (R/P/S/E) :")
        elif b == "Scissor":
            if c.upper() == "R":
                print("Congrats , YOU WON!!")
            elif c.upper() == "P":
                print("you lost , :( ")
            elif c.upper() == "S":
                print("Oops! , its DRAW")
            else:
                print("Please Choose from (R/P/S/E) :")
        else:
            print("Something went wrong.")
        print("Computer choosed " + b)