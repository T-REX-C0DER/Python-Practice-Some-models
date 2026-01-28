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


# #Conditional statements (Greatest of three numbers)
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



# # Decorators in Python
# def my_decorator(func):
#     def wrapper():
#         print("Before the function call.")
#         func()
#         print("After the function call.")
#     return wrapper
# @my_decorator
# def say_hello():
#     print("Hello!")
# say_hello()



# # Getters and Setters in Python
# class Student:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self, new_name):
#         if len(new_name) > 0:
#             self._name = new_name
#         else:
#             print("Name cannot be empty.")
# student1 = Student("Sanjay")
# print(student1.name)
# student1.name = "Sanjay Lade"
# print(student1.name)
# student1.name = ""
# print(student1.name)



# # Single Inheritance
# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
# dog1 = Dog()
# dog1.speak()
# dog1.bark()



# # Multi-level Inheritance
# class Grandparent:
#     def grandparent_method(self):
#         print("Grandparent method")
# class Parent(Grandparent):
#     def parent_method(self):
#         print("Parent method")
# class Child(Parent):
#     def child_method(self):
#         print("Child method")
# child1 = Child()
# child1.grandparent_method()
# child1.parent_method()
# child1.child_method()



# # Multiple Inheritance
# class Father:
#     def father_method(self):
#         print("Father method")
# class Mother:
#     def mother_method(self):
#         print("Mother method")
# class Child(Father, Mother):
#     def child_method(self):
#         print("Child method")
# child2 = Child()
# child2.father_method()
# child2.mother_method()
# child2.child_method()   



# # Hierarchical Inheritance
# class Parent:
#     def parent_method(self):
#         print("Parent method")
# class Child1(Parent):
#     def child1_method(self):
#         print("Child1 method")
# class Child2(Parent):
#     def child2_method(self):
#         print("Child2 method")
# child3 = Child1()
# child3.parent_method()
# child3.child1_method()
# child4 = Child2()
# child4.parent_method()
# child4.child2_method()



# # Hybrid Inheritance
# class A:
#     def method_a(self):
#         print("Method A")
# class B(A):
#     def method_b(self):
#         print("Method B")
# class C(A):
#     def method_c(self):
#         print("Method C")
# class D(B, C):
#     def method_d(self):
#         print("Method D")
# d1 = D()
# d1.method_a()
# d1.method_b()
# d1.method_c()
# d1.method_d()



# # Access Modifiers in Python
# # Public Access Modifier
# class PublicExample:
#     def __init__(self, name):
#         self.name = name
# example1 = PublicExample("Sanjay")
# print(example1.name)



# # Protected Access Modifier
# class ProtectedExample:
#     def __init__(self, name):
#         self._name = name
# example2 = ProtectedExample("Sanjay")
# print(example2._name)

# # Private Access Modifier
# class PrivateExample:
#     def __init__(self, name):
#         self.__name = name
#     def get_name(self):
#         return self.__name
# example3 = PrivateExample("Sanjay")
# print(example3.get_name())



# # # Static methods in Python
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# class MathOperations:
#     @staticmethod
#     def substract(a,b):
#         return a-b
#     @staticmethod
#     def add(a, b):
#         return a + b
#     @staticmethod
#     def multiply(a, b):
#         return a * b
# result1 = MathOperations.add(a, b)
# result2 = MathOperations.multiply(a,b)
# result3 = MathOperations.substract(a,b)
# print(f"The addition of num is : {result1}")
# print(f"The multiplication of num is : {result2}")
# print(f"The subtraction of num is : {result3}")
# result1 = MathOperations.add(5, 3)
# result2 = MathOperations.multiply(4, 6)
# print(result1)
# print(result2)



# # Method Overriding in Python
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")
# dog1 = Dog()
# cat1 = Cat()
# dog1.sound()
# cat1.sound()



# # Magic/Dunder Methods in Python
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#     def __str__(self):
#         return f"Point({self.x}, {self.y})"
# point1 = Point(1, 2)
# point2 = Point(3, 4)
# result = point1 + point2
# print(result)



# # Operator Overloading in Python
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y  
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#     def __sub__(self, other):
#         return Point(self.x - other.x, self.y - other.y)
#     def __mul__(self, other):
#         return Point(self.x * other.x, self.y * other.y)    
#     def __str__(self):
#         return f"Point({self.x}, {self.y})"
# point1 = Point(1, 2)
# point2 = Point(3, 4)
# result = point1 + point2
# print(result)
# result = point1 - point2
# print(result)
# result = point1 * point2
# print(result)



# # Time Module in Python
# import time 
# #  To get the current time
# current_time  = time.time() 
# print(f"Current Time in seconds since epoch: {current_time}")

# # To get the current local time
# current_time = time.localtime()
# print(f"Current Local Time: {current_time}")

# # To format the current local time
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
# print(f"Formatted Time: {formatted_time}")

# # To pause the execution for 2 seconds
# print("Pausing for 2 seconds...")
# time.sleep(2)
# print("Resuming execution.")



# # Walrus Operator in python 
# # Normally in py
# name = "sanjay"
# string = len(name)
# print(string)
# # With walrus 
# if(n := len(name))>5:
#     pass



# # Shutil in python
# import shutil
# # Copying a file
# shutil.copy("sanjay.txt" , "sanjay_copy.txt")
# # Moving a file
# shutil.move("sanjay_copy.txt" , "new_folder/sanjay_moved.txt")
# # Deleting a file
# shutil.rmtree("new_folder")
# # Creating a zip file
# shutil.make_archive("sanjay_archive" , 'zip' , "sanjay.txt")
# # Extracting a zip file
# shutil.unpack_archive("sanjay_archive.zip" , "extracted_folder" , 'zip')


# # reuqeusts module in python
# import requests
# response = requests.get("https://api.github.com")
# print(f"Status Code: {response.status_code}")
# print(f"Content: {response.text}")
# print(f"Headers: {response.headers}")


# # Multithreading in Python
# import threading
# import time
# def print_numbers():
#     for i in range(1, 6):
#         print(f"Number: {i}")
#         time.sleep(1)
# def print_letters():
#     for letter in "ABCDE":
#         print(f"Letter: {letter}")
#         time.sleep(1)
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("Both threads have finished.")    

# Generators in Python
def generate_squares(n):
    for i in range(n):
        yield i * i
squares = generate_squares(5)
for square in squares:
    print(square)   

# Function Caching in Python
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
print(fibonacci.cache_info())
fibonacci.cache_clear()
print(fibonacci.cache_info())

# Regular Expressions in Python
import re
pattern = r'\b\w{4}\b'
text = "This is a test text with some four letter words like test, text, and some."
matches = re.findall(pattern, text)
print(matches)