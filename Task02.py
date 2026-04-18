# taking 10 numbers from user
numbers = []

for i in range(10):
    num = int(input("Enter number " + str(i+1) + ": "))
    numbers.append(num)

# function to get odd numbers
def get_odds(nums):
    odd_list = []
    for n in nums:
        if n % 2 != 0:
            odd_list.append(n)
    return odd_list

# function to get even numbers
def get_evens(nums):
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

# function to get prime numbers
def get_primes(nums):
    prime_list = []
    for n in nums:
        if n <= 1:
            continue
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(n)
    return prime_list

# calling the functions
odd_numbers = get_odds(numbers)
even_numbers = get_evens(numbers)
prime_numbers = get_primes(numbers)

# printing results
print("\nOdd numbers:", odd_numbers)
if len(odd_numbers) == 0:
    print("Odd numbers: None found")

print("Even numbers:", even_numbers)
if len(even_numbers) == 0:
    print("Even numbers: None found")

print("Prime numbers:", prime_numbers)
if len(prime_numbers) == 0:
    print("Prime numbers: None found")