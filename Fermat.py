# GCD function using Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Simple function to check if p is prime
def is_prime(p):
    if p <= 1:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True


# Fermat's Little Theorem verifier
def verify_fermats_theorem(a, p):
    if gcd(a, p) != 1:
        print(f"{a} and {p} are not coprime. Fermat's theorem doesn't apply.")
        return

    result = pow(a, p - 1, p)
    if result == 1:
        print(f"Fermat's Little Theorem holds for a = {a}, p = {p}")
    else:
        print(f"Fermat's Little Theorem fails for a = {a}, p = {p}")


# Main program
try:
    a = int(input("Enter value of a: "))
    p = int(input("Enter value of p: "))

    if not is_prime(p):
        print(f"{p} is not a prime number. The theorem may not hold.")

    verify_fermats_theorem(a, p)

except ValueError:
    print("Please enter valid integers for a and p.")
