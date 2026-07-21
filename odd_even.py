while True:

    num = input(f"\n----ODD/EVEN Checker----\nEnter Your Number or (e) to exit: ")

    if num.lower() == "e":
        print("Exited")
        break
    
    elif num.isdigit():
    
        if int(num) % 2 == 0:
            print(f"{num} is an even number.")
        
        elif int(num) % 2 != 0:
            print(f"{num} is an odd number.")
        
    else:
        print(f"Invalid input ({num}), Please enter proper integer.")
        continue
        
