# asking for PIN and balance
correct_pin = 1234
pin = int(input("Enter your PIN: "))

# checking PIN
if pin != correct_pin:
    print("Wrong PIN. Access denied.")
else:
    balance = int(input("Enter your account balance: "))
    
    # withdraw function
    def withdraw(balance, amount):
        if amount > 0 and amount <= balance and amount % 500 == 0:
            balance = balance - amount
            print("Withdrawal successful!")
            print("Remaining balance:", balance)
            return balance
        else:
            if amount <= 0:
                print("Invalid amount. Amount must be greater than 0")
            elif amount > balance:
                print("Insufficient balance")
            elif amount % 500 != 0:
                print("Amount must be a multiple of 500")
            return balance
    
    # loop to keep asking for withdrawal
    while True:
        amount = int(input("\nEnter withdrawal amount (or 0 to exit): "))
        
        if amount == 0:
            print("Thank you for using our ATM. Goodbye!")
            break
        
        balance = withdraw(balance, amount)