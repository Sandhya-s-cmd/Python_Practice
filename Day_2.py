#1. Write a program to print the given number is even number or odd number
i=int(input("Enter any number: "))
if i % 2==0:
  print("Entered number is even",i)
else:
  print("Entered number is odd", i)
# 2. Write a program to find out the maximam among the given two numbers.
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
if a>b:
  print("Entered value a is max number",a)
elif b>a:
  print("Entered value b is max number",b)
else:
  print("Both are equal")
# 3. Write a program to print given string is palindrome or not.
a=input("Enter a string: ")
reversed_a="".join(reversed(a))
if a ==reversed_a:
  print("Entered string is a palindrome",a)
else:
  print("Entered string is not a palindrome")
# 4. Write a program to find out the maximum of 3 given numbers
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
if (a>b) and (a>c):
  print("Entered value a is max number",a)
elif (b>a) and (b>c):
  print("Entered value b is max number",b)
else:
  print("Entered value c is max number")