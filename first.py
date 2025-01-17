def show_balance():
    print(f"your balance is ${balance:.2f}")


def deposit():
    amount= float(input("enter an amount to be deposited:"))
    
    if amount < 0:
        print("this is not valid.")
        return 0
    else:
       print("SUCCESSFULLY DONE.")
       return amount
def withdrawn():
    global balance
    
    amount= float(input("enter an amount to be withdrawn:"))
     
    if amount < 0:
        print("invalid withdrawn.")
    elif amount > balance:
        print("insufficient balance.")
    else:
        balance -= amount
        print("withdrawn successfully.")
    

balance = 0

while True:
    print("***BANKING PROGRAM***")
    print("1.SHOW BALANCE")
    print("2.DEPOSIT")
    print("3.WITHDRAWN")
    print("4.EXIT")
    
    Choice = input("Enter your choice (1-4):")
    
    if Choice == '1':
        show_balance()
    elif Choice == '2':
        balance += deposit()
    elif Choice == '3':
        withdrawn()
    elif Choice == '4':
        print("THANKS FOR VISITING")
        break
    else:
        print("Your choice is not valid.")
        

