#1.Electriccity bill calculations based on given traffic slabs.
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Total bill: ₹", bill)


#2.Identify even, odd, and divisibility by 4.
num = int(input("Enter a number: "))

if num % 2 == 0:
    if num % 4 == 0:
        print("Even and Divisible by 4")
    else:
        print("Even but not Divisible by 4")
else:
    print("Odd")


#3.ATM Withdrawal Sytem with conditions on balance and denominations.

balance = 10000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw <= balance:
    if withdraw % 100 == 0:
        print("Transaction Successful! New Balance:", balance - withdraw)
    else:
        print("Amount must be a multiple of 100")
else:
    print("Insufficient Funds")

#4.Employee Bonus calculations based on experience and salary.

experience = int(input("Enter years of experience: "))
salary = float(input("Enter current salary: "))

if experience >= 5:
    bonus = salary * 0.10
    print("Bonus Amount: ₹", bonus)
else:
    print("No bonus")
 #5. Traffic light sugnal system baed on the signals 

light = input("Enter traffic light color (Red/Yellow/Green): ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get Ready")
elif light == "green":
    print("Go")
else:
    print("Invalid color")
