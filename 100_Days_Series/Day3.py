# 1. Write a python program  to find LCM
 
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(f"The LCM of {num1} and {num2} is: {lcm(num1,num2)}")

#2. Write a python program to find HCF

def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print(f"The HCF of {num1} and {num2} is: {hcf(num1,num2)}")
