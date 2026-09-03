#Arthematic operations

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#student marks calculation
name = input("Enter student name: ")

m1 = int(input("Enter marks for Python:"))
m2 = int(input("Enter marks for Java:"))
m3 = int(input("Enter marks for SQL:"))

total = m1 + m2 + m3
average = total / 3

print("\n----Student Marks Report----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

#shopping bill calculation
price1 = float(input("Enter price of product 1: "))
price2 = float(input("Enter price of product 2: "))
price3 = float(input("Enter price of product 3: "))

total_bill = price1 + price2 + price3
discount = total_bill * 0.1 
final_bill = total_bill - discount
print("Total Bill Amount: Rs.", total_bill)
print("Discount: Rs.", discount)
print("Final Bill Amount: Rs.", final_bill)

#comparison operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#assignment operators
x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)

x /= 4
print(x)

#bank balance
balance = 10000

deposit = 5000
balance += deposit
print("Balance after deposit: Rs.", balance)
withdraw = 2000
balance -= withdraw
print("Balance after withdrawal: Rs.", balance)

#age eligibility check
age = int(input("Enter your age: "))

print("Eligible to vote:", age >= 18)

#pass or fail check
marks = int(input("Enter your marks: "))    
print("Passed:", marks >= 40)

#login validation
correct_username = "admin"
correct_password = "password123"

username = input("Enter username: ")
password = input("Enter password: ")

print("Login successful:", username == correct_username and password == correct_password)

#logical operators
age = 25
citizen = True

print( age >= 18 and citizen == True)

has_card = True
has_cash = False
print("Eligible for loan:", has_card == True or has_cash == True)

is_raining = True
print("Stay indoors:", not is_raining)