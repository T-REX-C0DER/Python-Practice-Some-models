# #Arithmatic operations 
# a = int(input(f"Enter the number : "))
# b = int(input(f"Enter the number : "))
# c = int(input(f"Enter the number : "))
# sum = a+b+c
# multi = a*b*c
# div = (a+b)/c
# print(f"The sum is : {sum}")
# print(f"The multi is : {multi}")
# print(f"The div is : {div}")


# #Type conversion
# b = 2.5
# a = int(b)
# print(a)
# c = "2534"
# print(type(c))
# d = int(c)
# print(type(d))


# #In python by default it takes the input as strings only so we have to use diff applications


# #STRINGS & Its functions
# str1 = "sanjay"
# str2 = "lade"
# str3 = str1 + str2
# print(str3)
# print(str3[1:5])
# print(str3[:6])
# print(str3[-1:-5])
# print(str2.endswith('y'))
# print(str1.capitalize())


# #Conditional statements (Gretest of three numbers)
# a = int(input("Enter the num : ")) 
# b = int(input("Enter the num : ")) 
# c = int(input("Enter the num : "))
# if(a>b and a>c):
#     print(f"{a} is large ")
# elif(b>a and b>c):
#     print(f"{b} is large ")
# else:
#     print(f"{c} is large")


# #LISTS & Its functions
# student = ["sanjay",34,"solapur"]
# student[0] = "SanjayLade"
# print(student)
# print(student[1:2])
# print(student[-1:-2])
# student.append(24062231995006)
# student.reverse()
# student.remove(34)
# print(student)


# #TUPLES
# student = ("sanjay",34,"solapur")
# print(student)
# print(student[1:2])
# print(student[-1:-2])


# #DICTIONARY & Its functions 
# dict = {
#     "Name" : "sanjay",
#     "RollNo" : 34,
#     "SGPA" : {
#         "FY" : 9.55,
#         "SY" : 9.31,
#     }
# }
# dict["RollNo"] = "45"
# print(dict)
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("SGPA"))


# #SET & Its methods
# set1 = {1,2,3,4,5}
# set2 = {5,4,3,2,1}
# null_set = set()
# set1.add(67)
# set1.remove(67)
# set2.pop()
# set1.union(set2)
# set2.intersection(set1)
# print(set1)
# print(set2)
# set1.clear()
# print(set1)


# # FUNCTIONS
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# num = int(input("Enter the number : "))
# result = factorial(num)
# print(f"The factorial of {num} is {result}")


# #LOOPS
# for i in range(1,11):
#     print(i)

# i = 1
# while i<=10:
#     print(i)
#     i += 1


# #BREAK & CONTINUE
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)    


# #wap using tuples to print even numbers only
# numbers = (1,2,3,4,5,6,7,8,9,10)
# for num in numbers:   
#     if num%2 != 0:
#         continue
#     print(num)


# #for loop with lists
# fruits = ["apple","banana","mango","grapes"]
# for fruit in fruits:
#     print(fruit)


# #for loop with dictionary
# student = {
#     "Name" : "sanjay",
#     "RollNo" : 34,
#     "City" : "solapur"
# }
# for key, value in student.items():
#     print(f"{key} : {value}")


# #for loop with else
# for i in range(1,6):
#     print(i)
# else:
#     print("Loop is completed")


# #for loop with string
# word = "sanjay"
# for letter in word:
#     print(letter)


# #// recursion factorial of a num
# def fact(n):
#     if(n==0):
#         return 1
#     fact = n*fact(n-1)
# print(f"The factorial of a number is : {fact(5)}")


# #exception handling 
# try :
#     a = int(input())
#     b = a/0
#     print(b)
# except zerodiv :
#     print("enter valid num")
# else :
#     print("df")
# finally:
#     print("sdf")


# #file handling
# #writing to a file    
# file = open("sample.txt","w")
# file.write("Hello World\n")
# file.write("This is Sanjay Lade\n")
# file.write("I am from Solapur\n")
# file.close()
# # reading from a file
# file = open("sample.txt","r")
# content = file.read()
# print(content)
# file.close()


# #shorthand if else
# a = 10
# b = 20
# max = a if a>b else b
# print(f"The max num is : {max}")


# #enumerate function
# fruits = ["apple","banana","mango","grapes"]
# for index, fruit in enumerate(fruits):
#     print(f"{index} : {fruit}")


# # if __name__ == "__main__":
# def greeting(name):
#     return f"Hello, {name}!"
# print(greeting("Sanjay"))


# if __name__ == "__main__":
#     print("This script is being run directly.")


# # Os modules 
# import os 
# for i in range(0 , 11 ):#to create folders
#     os.mkdir


# # Local and Global Variables
# x = "global x"
# def my_function():
#     y = "local y"
#     print(y)
#     print(x)
#     global x
#     x = "modified global x"
# my_function()
# print(x)


# # File handling 
# file = open("sanjay.txt" , "r") # it is first method to read a file
# data = file.read()
# print(data)
# file.close()


# with open("sanjay.txt" , "r") as f: #   it is second method to read a filewe dont have to provide file.close()
#     data = f.read()
#     print(data)


# with open("sanjat,txt" , "x") as f: # it is used to create a new file
#     f.write("This is sanjay lade")


# with open("sanjay.txt" , "a") as f: # it is used to append data to existing file
#     f.write("\nThis is appended line.")


# with open("sanjay.txt" , "r") as f: # it is used to read the file
#     data = f.readline()
#     data2 = f.readlines()
#     data3 = f.read(5)
#     print(data)


# with open("sanjay.txt" , "r") as f: # it is used to read the file
#     f.seek(10)# it is used to move the cursor to specific position
#     print(f.tell())# it is used to know the current position of cursor
#     data = f.read()
#     print(data)


# # Lambda Functions 
# a = 10
# b = 234
# mutli = lambda a,b : a*b
# print(mutli(a,b))


# # Map Function
# marks = [23,78,90,56,43,34]
# square = list(map(lambda x : x*x , marks))
# print(square)


# # Filter Function
# numbers = [1,2,3,4,5,6,7,8,9,10]
# Odd_num = list(filter(lambda X : X %2 != 0 , numbers))
# print(Odd_num)


# # Reduce Function
# from functools import reduce
# nums = [23,456,78,546,33]
# avg = reduce(lambda a,b : a+b , nums )/len(nums)
# print(avg)


# # Is vs == operator
# a = [1,2,3]
# b = [1,2,3]
# print(a == b)
# print(a is b)
# c = a
# print(a == c)
# print(a is c)


# # OOP in Python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# stu1 = Person("Sanjay", 28)   
# stu1.greet()   

# # Constructors in Python
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def display_info(self):
#         print(f"This is a {self.make} {self.model}.")

# car1 = Car("Toyota", "Camry")
# car1.display_info()

# class Greet :
#     def __init__(self, DOB):
#         self.DOB = DOB
    
#     def display(self):
#         print(f"the dob is {self.DOB}")

# g1 = Greet("24 june 1995")
# g1.display()

# Decorators in Python
def my_decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()

# Getters and Setters in Python
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative.")

student = Student("Sanjay", 28)
print(student.name)
student.name = "Lade"
print(student.name)
print(student.age)
student.age = 30
print(student.age)
student.age = -5
print(student.age)