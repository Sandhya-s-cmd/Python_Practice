# 1. Check if a number is a perfect number
def is_perfect(num):
    if num <= 0:
        return False
    sum_divisors = sum(i for i in range(1, num) if num % i == 0)
    return sum_divisors == num

# Example
n = int(input("Enter a number: "))
print(f"{n} is a perfect number." if is_perfect(n) else f"{n} is not a perfect number.")

# 2. Check if a number is a strong number
import math

def is_strong(num):
    return num == sum(math.factorial(int(d)) for d in str(num))

# Example
n = int(input("Enter a number: "))
print(f"{n} is a strong number." if is_strong(n) else f"{n} is not a strong number.")

# 3. Print all prime numbers within a given range
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end} are:")
for i in range(start, end + 1):
    if is_prime(i):
        print(i, end=' ')

# 4. Find the HCF (Highest Common Factor) of two numbers
def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"The HCF of {x} and {y} is: {find_hcf(x, y)}")
