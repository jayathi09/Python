for i in range(1, 11):

    if i ==5:
        break # exit the loop

    print(i)

for i in range(1,11):
    if i ==5:
        continue #skip current literation

    print(i)

for i in range(1,6):

    if i==3:
        pass
    print(i)

age = 20

if age >= 18:
    pass #Eligible
else:
    print("Not eligible")


#print odd number from 1 to 10
for i in range(1,11):
    if i%2 ==0:
        continue

    print(i) 

#print numbers until user enters
while True:

    number =int(input("enter number"))

    if number == 0:
        break

    print("You entered :", number)  

#Print numbers from 1 to 100,but skip multiples of 3 and stop at 50
for i in range(1,101):

    if i == 50:
        break
    if i % 3 == 0:
        continue

    print(i)  
#Calculate the sum of positive numbers
total = 0
while True:

    number =int(input("enter number"))

    if number < 0:
        continue

    if number == 0:
        break

    total = total + number

    print("Total:", total)