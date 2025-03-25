#	Print the Fibonacci series up to N terms.
def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Enter the number of terms: "))
print(f"Fibonacci Series: {fibonacci(n)}")

#Calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num}: {factorial(num)}")

# Count the number of digits in a given number.
def count_digits(n):
    return len(str(abs(n)))  # Convert number to string and count digits

num = int(input("Enter a number: "))
print(f"Number of digits: {count_digits(num)}")

# Print a number pattern (triangle of numbers).
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Check if a number is a palindrome.
def is_palindrome(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")
