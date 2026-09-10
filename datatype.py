#list in python
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
marks = [90, 80, 75, 85]

print(marks) 

#accessing elements of list
marks = [90, 80, 75, 85]

print(marks[0]) 
print(marks[1]) 
print(marks[2])
print(marks[3])

#changing elements in a list
marks = [90, 80, 75]
marks[1] = 95
print(marks)

#adding elements in a list
marks = [90, 80, 75]

marks.append(85)
print(marks)

#remove element from list
marks = [80,90,75]

marks.remove(90)
print(marks)

#insert element in list
numbers=[10,20,30]
numbers.insert(1,15)
print(numbers)

#extend
a=[1,2,3]
b=[4,5,6]

a.extend(b)
print(a)

#clear
numbers=[10,20,30]
numbers.clear()
print(numbers)

#index
numbers = [10,20,30,40]
print(numbers.index(30))

#count
numbers = [10,20,20,30,20]
print(numbers.count(20))

#sort
numbers = [40,10,30,20]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#copy
a = [1,2,3]
b = a.copy()
print(b)

numbers = [10,20,30,40,50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-2])
print(numbers[-1::])