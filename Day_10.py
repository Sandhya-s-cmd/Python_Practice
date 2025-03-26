#1.	Check if a number is an Armstrong number.
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#2.	Count even and odd digits in a number.

def count_even_odd(n):
    even_count = odd_count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        n //= 10
    return even_count, odd_count

num = int(input("Enter a number: "))
even, odd = count_even_odd(num)
print(f"Even digits: {even}, Odd digits: {odd}")

#3.	Find the GCD (Greatest Common Divisor) of two numbers.
def find_gcd(a, b):
    while b:
        a, b = b, a % b  # Using Euclidean algorithm
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"GCD of {num1} and {num2} is {find_gcd(num1, num2)}")

#4 Find the LCM of two numbers
def find_lcm(a, b):
    max_num = max(a, b)
    while True:
        if max_num % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"LCM of {num1} and {num2} is {find_lcm(num1, num2)}")
