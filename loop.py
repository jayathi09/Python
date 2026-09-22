#for loop
#used to repeat code or iterate  through a sequence

for i in range(1,6):
    print(i)

#use while when repetition depends on a condition.
#looping through number 1 to 5 using while loop
i = 1 

while i<=5:
    print(i)
    i = i+1

#print 1 to 10
for i in range (1,11):
    print(i)

#print 10 to 1
for i in range (10,0,-1):
    print(i)



#print even number from 2 to 50
for i in range (2,51,2):
    print(i)


#print odd number from 1 to 51
for i in range (1,51,2):
    print(i)

# print multiple of 5 from 5 to 50
for i in range (5,51,5):
    print(i)

#multiplication
number = int(input("enter number:"))
for i in range (1,11):
    print(number,"*",i,"=",number*i)


#sum of number from 1 to n 
n = int(input("enter n:"))
total = 0
for i in range(1,n+1):
    total = total+i
    print("sum:",total)

#factorial of numbers
n = int(input("enter n:"))
factorial = 1
for i in range (1,n+1):
    factorial = factorial*i
    print("factorial:",factorial)

#sum of  even number from 2 to n 
n = int(input("enter n:"))
total = 0
for i in range(2,n+1,2):
    total = total+i
    print("sum:",total)


#Count multiples of 3
n=int(input("enter n:"))

count=0

for i in range(1,n+1):
    if i % 3 == 0:
        count = count + 1

print("count:", count)

#sum of multiples of 5
n=int(input("enter n:"))

total=0

for i in range(1,n+1):
    if i % 5 == 0:
        total = total + 1

print("sum:", total )

# print all even numberes from 2 to 50
i=2

while i<=50:
    print(i)
    i= i + 2

# print all odd numberes from 1 to 49
i=1

while i<=49:
    print(i)
    i= i + 2

#print total of numbers entered by user until 0 is entered
total = 0

number = int(input("enter number:"))

while number !=0:
    total = total + number
    number = int(input("enter number"))

    print("Total:",total) 

#Password check
password=""

while password !="python123":
    password = input("enter password:")

    print("login successful")



#count the number of digits in a number 
number = int(input("enter the number:"))

count = 0

while number > 0:
    number = number // 10
    count = count + 1

print("number of digits:",count) 

#sum of digits in a number
number = int(input("enter number:"))

total=0

while number>0:
    digit = number%10
    total = total+ digit
    number=number//10
print("sum of digits:",total)

#reverse a number
number = int(input("enter a number:"))

reverse = 0 

while number > 0:
    digit = number % 10
    number = number // 10
    reverse =  reverse * 10 + digit

print("reverse:", reverse)



#check if a number is a palindrome
number = int(input("enter number:"))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("palindrome")
else:
    print("not plindrome")


#check if a number is prime
number = int(input("enter number"))

count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count==2:

    print("prime number")
else:
    print("not a prime number")


#print all prime numbers between 2 and 100
for number in range (2, 101):

    count = 0
    for i in range(1, number + 1):
     if number % i == 0:
        count = count + 1

if count==2:

    print("prime number")
else:
    print("not a prime number")