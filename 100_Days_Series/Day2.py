#1. Write a python program to check if a number is even or odd
num=int(input("Enter a number: "))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")

# 2. Write a python prgram to check the leap year
year=int(input("Enter a year: "))

#Divided by 100 means century year
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is a leap year.")    

# t divided by 100 means not a leap year
# Year divided by 4 is a leap year
elif(year%4==0 and year%100!=0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 3. Write a python program to find the prime number
num=int(input("Enter a number: "))  
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime number.")
            break
else:
    print(f"{num} is a prime number.")
        

# 4. Write a python program to print all prime numbers in an interval 1-10

lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: ")) 
print(f"Prime numbers between {lower} and {upper} are: ")
for num in range(lower, upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)


# 5. Write a python program to find the factorial of a number
num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Factorial does not exist for negative numbers.")
elif num==0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"The factorial of {num} is {factorial}.")


# 6. Write a python program to find the multiplicatetion table of a number
num=int(input("Enter a number: "))
print(f"Multiplication table of {num}:")
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")


# 7. Write a python program to print the fibonacci sequence
n=int(input("Enter the number of terms: "))
a,b=0,1
count=0 

if n<=0:
    print("Please enter a positive integer.")   
elif n==1:
    print("Fibonacci sequence upto", n, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count<n:
        print(a)
        a,b=b,a+b
        count+=1

# 8. Write a python program to check if a number is armstrong number

num=int(input("Enter a number: "))
order=len(str(num))
sum=0   
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**order
    temp//=10
if num==sum:
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")

# 9. Write a python program to find armstrong numbers in an interval
lower=int(input("Enter the lower limit: "))
upper=int(input("Enter the upper limit: "))
print(f"Armstrong numbers between {lower} and {upper} are: ")
for num in range(lower, upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp//=10
    if num==sum:
        print(num)  


# 10. Write a python program to find the sum of natural numbers
num=int(input("Enter a number: "))  
if num<0:
    print("Please enter a positive integer.")   
else:
    sum=num*(num+1)//2
    print(f"The sum of the first {num} natural numbers is: {sum}")
