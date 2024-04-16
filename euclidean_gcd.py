def gcd(a, b):
    # Ensure a is greater than or equal to b
    if a < b:
        a, b = b, a
    
    # Apply Euclidean algorithm
    while b != 0:
        a, b = b, a % b
    
    return a

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)
