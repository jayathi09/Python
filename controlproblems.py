print("hello class")
age=int(input("enter a age"))
if(age>=18):
    print("eligibile for vote")
    print("eligibile for bike ride")
else:   
    print("not eligible for vote")
    print("not eligible for bike ride")
print("enter your name")

number=int(input("enter a number:"))
if(number==1):
    print("MRDU")
elif(number==2):
    print("MBU")
elif(number==3):
    print("gitam")
else:
    print("select another college")



number=int(input("enter a number:"))
if(number>0):   
    if(number<50):
        print("number in between 1-50")
    else:
     print("number is greater than 50")
else: 
    print("-ve number")


marks = int(input("enter the number:"))
if (marks< 40):
    print("failed")
else:
    print("passed")

number = int(input("enter the number:"))
if (number % 5 == 0):
    print("number is divisible by 5")
else:
    print("number is not  divisible by 5")

temperature = float(input("enter the number: "))
if (temperature > 40):
    print("high temperature")
else:
    print('normal')


number = int(input("enter the number:"))

if (number > 0):
    print("number is positive")
elif (number ==0):
    print("number is   zero")
else:
    print("number is negative")


number = int(input("enter the number:"))
if number > 100:
    print("number is greater than 100")
else:
    print("number is not  greater than 100")



marks = int(input("enter the marks:"))
if marks >= 90:
    print("grade A")
elif marks >= 75:
    print("grade B")
elif marks >= 60:
    print("grade C")
elif marks >= 40:
    print("grade D")
else:
    print("fail")



a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
if a > b:
    print("largest:",a)
elif b > a:
    print("largest:",b)
else:
    print("equal")

a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a >= b and a>= c:
    print("largest:",a)
elif b >= a and b>= c:
    print("largest:",b)
else:
    print("largest:",c)


number = int(input("enter the number from :"))
if number == 1:
    print("MONDAY")
elif number == 2:
    print("TUESDAY")
elif number == 3:
    print("WEDNESDAY")
elif number == 4:
    print("THURSDAY")
elif number == 5:
    print("FRIDAY")
elif number == 6:
    print("SATURDAY")
elif number == 7:
    print("SUNDAY")
else:
    print("invalid")


a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
operator = input("enter the operator from +,-,*,/:")
if (operator == "+"):
    print("a+b",a+b)
elif (operator == "-"):
    print("a-b",a-b)
elif(operator == "*"):
    print("a*b",a*b)
elif(operator == "+"):
    print("a/b",a/b)
else:
    print("invalid operators")

    


