# 1. Simple Interest Calculation
def simple_interest(principal, rate, time):
    if principal > 0 and rate > 0 and time > 0:
        interest = (principal * rate * time) / 100
        return interest
    else:
        return "Invalid input. All values must be positive."

p = float(input("Enter Principal: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time in years: "))
print("Simple Interest:", simple_interest(p, r, t))


# 2. BMI Calculator
def bmi_calculator(weight, height):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            return f"BMI: {bmi:.2f} (Underweight)"
        elif bmi < 24.9:
            return f"BMI: {bmi:.2f} (Normal weight)"
        elif bmi < 29.9:
            return f"BMI: {bmi:.2f} (Overweight)"
        else:
            return f"BMI: {bmi:.2f} (Obese)"
    else:
        return "Invalid input. Weight and height must be positive."

w = float(input("Enter Weight (kg): "))
h = float(input("Enter Height (m): "))
print(bmi_calculator(w, h))


# 3. Temperature Converter
def temperature_converter(temp, scale):
    if scale.lower() == 'c':
        fahrenheit = (temp * 9/5) + 32
        return f"{temp}°C = {fahrenheit:.2f}°F"
    elif scale.lower() == 'f':
        celsius = (temp - 32) * 5/9
        return f"{temp}°F = {celsius:.2f}°C"
    else:
        return "Invalid scale! Use 'C' for Celsius or 'F' for Fahrenheit."

t = float(input("Enter Temperature: "))
s = input("Enter Scale (C/F): ")
print(temperature_converter(t, s))


# 4. Greatest of Three Numbers
def greatest_of_three(a, b, c):
    if a > b:
        if a > c:
            return f"Largest number: {a}"
        else:
            return f"Largest number: {c}"
    else:
        if b > c:
            return f"Largest number: {b}"
        else:
            return f"Largest number: {c}"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(greatest_of_three(num1, num2, num3))


# 5. Check Palindrome Number
def is_palindrome(number):
    if number < 0:
        return "Negative numbers are not palindromes."
    original = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = (reverse * 10) + digit
        number //= 10
    if original == reverse:
        return f"{original} is a Palindrome."
    else:
        return f"{original} is not a Palindrome."

num = int(input("Enter a number: "))
print(is_palindrome(num))
