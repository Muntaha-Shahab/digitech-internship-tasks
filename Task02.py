def is_prime(n):
    """Check if a number is prime manually using a loop"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisibility from 3 to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_odds(numbers):
    """Return list of odd numbers"""
    return [num for num in numbers if num % 2 != 0]

def get_evens(numbers):
    """Return list of even numbers"""
    return [num for num in numbers if num % 2 == 0]

def get_primes(numbers):
    """Return list of prime numbers"""
    return [num for num in numbers if is_prime(num)]

def get_user_numbers():
    """Get 10 numbers from user"""
    numbers = []
    print("Please enter 10 numbers:")
    
    for i in range(1, 11):
        while True:
            try:
                num = int(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
    return numbers

def print_category_result(category_name, items):
    """Print results for a category"""
    if items:
        print(f"{category_name}: {items}")
    else:
        print(f"{category_name}: None found")

def main_task2():
    print("=" * 40)
    print("NUMBER CLASSIFIER")
    print("=" * 40)
    
    numbers = get_user_numbers()
    
    odds = get_odds(numbers)
    evens = get_evens(numbers)
    primes = get_primes(numbers)
    
    print("\n" + "=" * 40)
    print("CLASSIFICATION RESULTS")
    print("=" * 40)
    print(f"Original numbers: {numbers}")
    print("-" * 40)
    print_category_result("Odd numbers", odds)
    print_category_result("Even numbers", evens)
    print_category_result("Prime numbers", primes)
    print("=" * 40)

if __name__ == "__main__":
    main_task2()