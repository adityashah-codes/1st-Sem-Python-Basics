bal = 0

def deposit(amt):
    global bal
    if amt <= 0:
        print("Please enter an amount greater than zero.")
        return
    bal = bal + amt
    print("Amount deposited")
      
def withdraw(amt):
    global bal
    if amt <= 0:
        print("Please enter an amount greater than zero.")
        return
    if amt >= bal:
        print(f"Not sufficient balance\nCurrent Balance - {bal}")    
    else:
        bal = bal - amt
        print("Amount deducted")

while True:

    action = input(
    "----MENU----\n" \
    "'1' for withdrawl\n" \
    "'2' for deposit\n" \
    "'3' for checking balance\n" \
    "'e' for exit\n" \
    "----> ")

    if action == "1":
        try:
            withdrawl_amt = int(input("Enter the amount to be withdrawn: "))
            withdraw(withdrawl_amt)
            continue
        except ValueError:
            print("invalid amount")
            continue

    elif action == "2":
        try:
            deposit_amt = int(input("Enter the amount to be deposited: "))
            deposit(deposit_amt)
            continue
        except ValueError:
            print("invalid amount")
            continue

    elif action == "3":
        print(f"Current balance: {bal}")
    
    elif action.lower() == "e":
        break

    else:
        continue

    

