# 1. Write a program to print numbers from 1 to N using a loop
N = int(input("Enter a number: "))
for i in range(1, N + 1):
    print(i, end=" ")

# 2. Write a program to find the sum of the first N natural numbers.
N = int(input("\n Enter a number: "))
sum_n = 0
for i in range(1, N + 1):
    sum_n += i
print("Sum of first", N, "natural numbers is:", sum_n)

# 3. Write a program to print the multiplication table of a given number.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 4. Write a program to reverse a given number using a loop.
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed number:", rev)

# 5. Write a program to print the Fibonacci series up to N terms.
N = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:", a, b, end=" ")
for _ in range(N - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c