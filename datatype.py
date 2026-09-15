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

#tuple in python
#tuple is a collection of multiple values that is ordered and cannot be changed after creation 
student = ("s.jayathi",98,"python")

print(student[0])

#access values in a tuple
student = ("s.jayathi",19,95.3)

print (student[0])
print(student[1])
print(student[2])


#tuple are immutable, meaning they cannot be changed after are create.they are defined using parenthasis.
numbers = (10,20,20,30,20)
print(numbers.count(20))

#index 
numbers = (10,20,30,40)
print(numbers.index(30))

numbers = (10,20,30,40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python 
#set is a collection of unique values that is unordered and mutable

numbers = {10,20,30,20,10}

print(numbers)

#add values to a set
subjects = {"python","java"}
subjects.add("SQL")
print(subjects)

#remove values from a set
subjects.remove("java")

print(subjects)

#sets do not allow duplicates values
numbers = {1,2,2,3,3,4}

print(numbers)

#dictionaries in python
#dictionary is a collection of key-value pairs that is unordered and mutable
student = {
    "name": "jayathi",
    "age":00,
    "course": "python"
}
print(student)

#access element in dic
print(student["name"])
print(student["age"])
print(student["course"])

#add new data to a dictionary
student["city"] = "vijayawada" 

print(student)

## dictionaries are unordered collection
student = {
    "name": "jayathi",
    "age":19,
    "course": "python"
}
print(student.keys())
#keys() returns all the keys in the dictionary

print(student.items())
#item() return all key-value pairs

print(student.get("name"))
#get() returns the value of the specified key

print(student.values())
# values() returns all the values in the dictionary

student.update({"age":22})
#update()updates the value of the specified key

print(student)

student.pop("age")
#pop() removes the specified key and its value

print(student)

#popitem() removes the last inserted key-value pair
student = {
    "name": "jayathi",
    "age":19,
    "course": "python"
}
student.popitem()
print(student)

student = {
    "name": "jayathi",
}
student.setdefault("age",19)
print(student)
