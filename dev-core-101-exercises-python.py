import random


def is_prime(num):
    if num < 2:  # Numbers less than 2 are not prime
        return False
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            return False
    return True


n = int(input()) 
random_list = [random.randint(1, 100) for _ in range(n)]  # Generates random integers between 1 and 100

# Find prime numbers in the list
prime_numbers = [num for num in random_list if is_prime(num)]

# Print the results
print("List of random integers:", random_list)
print("Prime numbers in the list:", prime_numbers)
