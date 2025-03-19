#1 Determine if a number is an Armstrong number
def is_armstrong(num):
    num_str = str(num)  
    num_digits = len(num_str)  
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)  
    return num == sum_of_powers  
num = 153
print(is_armstrong(num))  
 
#2 Compute the sum of digits of a given number. 
def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

num = 1234
print(sum_of_digits(num))  

#3 Generate Fibonacci sequence up to a given term. 

def fibonacci_series(n):
    fib_list = [0, 1]  # First two Fibonacci numbers
    for i in range(2, n):  # Generate the next numbers
        next_term = fib_list[-1] + fib_list[-2]  # Sum of last two terms
        fib_list.append(next_term)
    return fib_list[:n]  # Return the series up to 'n' terms

num = int(input("Enter number of terms: "))
print("Fibonacci Series:", fibonacci_series(num))

#4 Reverse the digits of a number
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        last_digit = number % 10  # Get last digit
        reversed_num = reversed_num * 10 + last_digit  # Shift left and add new digit
        number //= 10  # Remove last digit
    return reversed_num

num = int(input("Enter a number: "))
print("Reversed Number:", reverse_number(num))

#5 Compute the factorial of a given number. 
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    result = 1
    for i in range(2, n + 1):  # Multiply numbers from 2 to n
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))
