def withdraw(balance, amount):
    """
    Process withdrawal if valid
    Returns new balance or None if invalid
    """
    # Check if amount is positive
    if amount <= 0:
        return None, "Amount must be greater than 0"
    
    # Check if amount is multiple of 500
    if amount % 500 != 0:
        return None, "Amount must be a multiple of 500 (500, 1000, 1500, etc.)"
    
    # Check if sufficient balance
    if amount > balance:
        return None, f"Insufficient balance. Your balance is ₱{balance:,.2f}"
    
    # Process withdrawal
    new_balance = balance - amount
    return new_balance, f"Withdrawal successful! Remaining balance: ₱{new_balance:,.2f}"

def authenticate_user():
    """Authenticate user with PIN"""
    CORRECT_PIN = "1234"  # PIN
    
    pin = input("Enter your 4-digit PIN: ").strip()
    
    if pin != CORRECT_PIN:
        print("=" * 40)
        print("ACCESS DENIED!")
        print("Invalid PIN. Exiting program.")
        print("=" * 40)
        return False, None
    
    return True, get_initial_balance()

def get_initial_balance():
    """Get initial account balance from user"""
    while True:
        try:
            balance = float(input("Enter your account balance: ₱"))
            if balance >= 0:
                return balance
            else:
                print("Balance cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main_task3():
    print("=" * 40)
    print("ATM WITHDRAWAL SYSTEM")
    print("=" * 40)
    
    # Authenticate user
    authenticated, balance = authenticate_user()
    if not authenticated:
        return
    
    print(f"\nWelcome! Your current balance is: ₱{balance:,.2f}")
    print("-" * 40)
    
    # Withdrawal loop
    while True:
        print("\nWithdrawal options:")
        print("  • Amount must be multiple of ₱500")
        print("  • Enter 0 to exit")
        print("-" * 40)
        
        try:
            amount = float(input("Enter withdrawal amount: ₱"))
            
            # Exit condition
            if amount == 0:
                print("\n" + "=" * 40)
                print(f"Thank you for using our ATM!")
                print(f"Your final balance is: ₱{balance:,.2f}")
                print("=" * 40)
                break
            
            # Process withdrawal
            new_balance, message = withdraw(balance, amount)
            
            if new_balance is not None:
                balance = new_balance
                print(f"✓ {message}")
            else:
                print(f"✗ {message}")
                
        except ValueError:
            print("✗ Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main_task3()