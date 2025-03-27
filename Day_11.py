#1. Write a python progrm to find the area of triangle
# Taking the inputs like base and height from user
base=float(input("Enter the lenght of the base of he triangle: "))
height=float(input("Enter the height of the triangle:"))
# Calculating the area of the triangle
area=0.5*base*height
print(f"Area of the triangle is: {area}")
# 2. Swaping two variables
#input of two variables
a=input("Enter the value of the 'a' : ")
b=input("Enter the value of 'b' is: ")
print(f"Original values of a,b: {a,b}")
# swapig the values using a tem values
temp=a
a=b
b=temp
# Display the swapped values
print(f"Swapped values: a={a},b={b}")

#3.Generating a random number
import random
print(f"Random number: {random.randint(1,100)}")
