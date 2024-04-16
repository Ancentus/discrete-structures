import random

def power_mod(base, exponent, modulus):
    # Calculates (base^exponent) % modulus efficiently using modular exponentiation
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def fermat_primality_test(n, k=5):
    # Test for primality of n using the Fermat primality test with k iterations
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)  # Randomly choose a base a
        if power_mod(a, n - 1, n) != 1:
            return False  # n is definitely composite
    return True  # n is likely prime

# Example usage:
num = int(input("Enter a number to test for primality: "))
if fermat_primality_test(num):
    print(num, "is likely to be prime.")
else:
    print(num, "is composite.")
