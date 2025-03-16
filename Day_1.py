# 1. Write a program to print given number if is more than 100.s
num=int(input("Enter the number: "))
if num >=100:
  print("True",num)

# 2. Write a program to print the given string if it is having even number of characters in it. 
string=(input("Enter a String:"))
if len (string) %2 ==0:
  print("Given string is even no of characters",string)
else:
  print("Give the correct input")
# 3. Write a program to print the given string if it is having odd number of characters in it.
string=input("Enter a string: ")
if len (string)%2-1==0:
  print("Given string is odd of characters", string)
else:
  print("Give the correct input")  
