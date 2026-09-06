#logical operators
age = 25
citizen = True

print( age >= 18 and citizen == True)

has_card = False
has_cash = True

print(has_card or has_cash) 

is_logged_in = True
print(not is_logged_in)

#atm eligibility check
balance = 10000
withdraw_amount = 5000  

print(withdraw_amount <= balance and withdraw_amount > 0)

#student scolarship eligibility check
marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

eligibility = marks >= 85 and attendance >= 75

print("Scholarship Eligibility:", eligibility)