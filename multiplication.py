while True:
    
    print(f"\nMultiplication Table Generator\n-------------------------")
    
    num = input(f"\nEnter the Number or (e) to exit: ")
    
    if num.isdigit():
        
        for i in range(1,11):
            multiple = int(num) * i            
            print(f"{num} * {i} = {multiple}")

    elif num.lower() == "e":
        print("Exited")
        break

    else:
        print(f"Invalid input {num}, please enter proper number.\n")
        continue