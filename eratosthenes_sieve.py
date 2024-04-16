def sieve_of_eratosthenes(limit):
    # Create a boolean list "prime" and initialize all entries as True
    prime = [True for _ in range(limit+1)]
    prime[0] = prime[1] = False  # 0 and 1 are not primes

    p = 2
    while p * p <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, limit+1, p):
                prime[i] = False
        p += 1

    # Return a list of prime numbers
    primes = [i for i in range(2, limit+1) if prime[i]]
    return primes

# Get the limit from the user
limit = int(input("Enter the limit to find prime numbers: "))
print("Prime numbers up to", limit, "are:")
print(sieve_of_eratosthenes(limit))
