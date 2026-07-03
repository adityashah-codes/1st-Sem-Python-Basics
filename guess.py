import random
print("----WELCOME TO NUMBER GUESSING GAME----")
print("I thought of a number , TRY GUESSING IT!!!")
secret_num = random.randint(1, 100)
b = 1
while True:
    a = int(input("Emter the guessed number : "))    
    if a > secret_num:
        print("You Gussed it High , lower your number : ")
        b = b + 1
    elif a < secret_num:
        print("You guessed it low , higher your number : ")
        b = b + 1
    else:
        print("Boom!, You Got it RIGHT!!!")
        break
print("You guseed the number in " + str(b) + " attempt(s)")      