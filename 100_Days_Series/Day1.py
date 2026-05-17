#1. Write a python program to arithmetical operations addition &division 
# Addition 
num1=float(input("Enter the first num for addition: "))
num2=float(input("Enter the Second num for addition: "))
Sum_result=num1+num2
print(f"Sum: {num1}+{num2}={Sum_result}")

#Division
num3=float(input("Enter the dividend for division: "))
num4=float(input("Enter the divisor for division: "))
if num4==0:
    print("Error :Division by zero is not allowed.")
else:
    div_result=num3/num4
    print(f"Division:{num3}/{num4}={div_result}")


#2. Write a program to find the area of triangle.
#Input the base & height from the user
base=float(input("Enter the lenght of the base of the triangle: "))
height=float(input("Enter the height of the triangle: "))
#Calculate the area of the triangle
area=0.5*base*height
# Display the result
print(f"The area of the triangle is :{area}")

# 3. Write a python program to swap variables
#Input two variables
a=input("Enter the value of first variable (a): ")
b=input("Enter the value of  Second variable(b): ")
#Display the original values
print(f"Original values : a{a}; b={b}")

#Swap the values using a temparary variable 
temp=a
a=b
b=temp
#Display the swapped values
print(f"Swapped values: a={a}, b={b}")

#4. Write a python program to generate a random number 
import math
import random
print(f"Random number: {random.randint(1,100)}")

#5. Write a python program to convert kilometers to miles
kilometers=float(input("Enter distance in Kilometer: "))
#Converson factor: 1 kilometer =0.621371 miles
Conversion_factor= 0.621371
miles= kilometers * Conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")

# 6. Write a python program to convert celsius fahrenheit
celsius=float(input("Enter temparature in Celsius: "))
#conversion formul : fahrenhit=(celsius*9/5)+32
fahrenheit=(celsius*9/5) +32
print(f"{celsius} degrees celsius is equal to {fahrenheit} degrees fahrenhit")

#7. Write a python program to display calender.
import calendar
year = int(input("Enter year: "))
month=int(input("Enter the month:"))

cal =calendar.month(year, month)
print(cal)


#8. Write a python program to solve quadratic equation



a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"The roots are {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The root is {root}")
else:
    print("The equation has no real roots")

#9. Write a python program to swap two numbers without using a temparary variable
a=float(input("Enter the values of the first number(a):"))
b=float(input("Enter the vale of the second number(b):"))
# Display the original values
print(f"Original values: a={a}, b={b}")
#Swap the values without using temparary variable
a,b=b,a
#Display the Swapped values
print(f"Swapped values: a={a}, b={b}")

# 10 Write a python program to check if a number is positive, negative or zero
num=float(input("Enter a number: "))
if num>0:
    print(f"{num} is a positive number.")
elif num<0:
    print(f"{num} is a negative number.")
else:
    print(f"{num} is zero.")    