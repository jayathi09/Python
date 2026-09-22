Username =  input("enter the username:")
Password = input("enter the password:")
username = "jayathi.s"
password = "3004556"
if Username == username :
  if Password == password:
    print("login succesful")
else:
    print("login failed")

balance = int(input("enter the number:"))
withdraw        = int(input("enter the withdraw number:"))
if withdraw >0:
  if withdraw <= balance:
    balance == balance-withdraw
    print("withdraw is succesfull:",balance)
  else:
    print("insufficient balance")
else:
    print("invalid amount")

marks = int(input("enter  marks:"))
attendences = float(input("enter the attendences percentage: "))

if marks>= 40:
  if attendences >= 75:
    print("eligible")
  else:
    print("not eligible due to attendences")
else:
    print("fail")

age = int(input("enter the age :"))
test = input("did you pass the driving test? yes/no:")
if age>=18:
  if test == "yes":
    print("eligible for license")
else:
    print("not eligible for license")

#order of evalution
print(2+13*2)

result = (10+5)*2
print(result)