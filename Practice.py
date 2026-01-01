#Arithmatic operations 
# a = int(input(f"Enter the number : "))
# b = int(input(f"Enter the number : "))
# c = int(input(f"Enter the number : "))
# sum = a+b+c
# multi = a*b*c
# div = (a+b)/c
# print(f"The sum is : {sum}")
# print(f"The multi is : {multi}")
# print(f"The div is : {div}")


#Type conversion
# b = 2.5
# a = int(b)
# print(a)
# c = "2534"
# print(type(c))
# d = int(c)
# print(type(d))


#In python by default it takes the input as strings only so we have to use diff applications


#STRINGS & Its functions
# str1 = "sanjay"
# str2 = "lade"
# str3 = str1 + str2
# print(str3)
# print(str3[1:5])
# print(str3[:6])
# print(str3[-1:-5])
# print(str2.endswith('y'))
# print(str1.capitalize())


#Conditional statements (Gretest of three numbers)
# a = int(input("Enter the num : ")) 
# b = int(input("Enter the num : ")) 
# c = int(input("Enter the num : "))
# if(a>b and a>c):
#     print(f"{a} is large ")
# elif(b>a and b>c):
#     print(f"{b} is large ")
# else:
#     print(f"{c} is large")


#LISTS & Its functions
# student = ["sanjay",34,"solapur"]
# student[0] = "SanjayLade"
# print(student)
# print(student[1:2])
# print(student[-1:-2])
# student.append(24062231995006)
# student.reverse()
# student.remove(34)
# print(student)


#TUPLES
# student = ("sanjay",34,"solapur")
# print(student)
# print(student[1:2])
# print(student[-1:-2])


#DICTIONARY & Its functions 
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


#SET & Its methods
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

# FUNCTIONS
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# num = int(input("Enter the number : "))
# result = factorial(num)
# print(f"The factorial of {num} is {result}")


#LOOPS
# for i in range(1,11):
#     print(i)

# i = 1
# while i<=10:
#     print(i)
#     i += 1


#BREAK & CONTINUE
# for i in range(1,11):
#     if i==5:
#         break
#     print(i)    

#wap using tuples to print even numbers only
# numbers = (1,2,3,4,5,6,7,8,9,10)
# for num in numbers:   
#     if num%2 != 0:
#         continue
#     print(num)
