# student_name = "rahul ubale"
# student_rollno = 68
# student_aadharno = "3565578811"
# student_email = "rahulubale0101@gmail.com"
# student_password = "123456"
# print(f'Student Name: {student_name} and his rollno is {student_rollno} , aashar no is {student_aadharno}, email is {student_email} and password is {student_password} ')

# student_name = input("Enter the name of student :")
# student_rollno = int(input("Enter the name of rollno :"))
# student_aadharno = input("Enter the name of aadharno :")
# student_email = input("Enter the name of email :")
# student_password = input("Enter the name of password :")
# print(f"Student Name: {student_name} and his rollno is {student_rollno} , aadharno is {student_aadharno}, email is {student_email} and password is {student_password} ")

# student_subjects = input("Enter Student Subjects")
# student_grades1 = int(input("Enter Student Grades"))
# student_grades2 = int(input("Enter Student Grades"))
# student_grades3 = int(input("Enter Student Grades"))
# print(f" The students 3 subjects are {student_subjects} and teh grades are {student_grades1} and {student_grades2} ,{student_grades3}")


# Celcius to Farenheit convertor
# temp = int(input("Enter the temperature in celcius: "))
# faren = (temp*9/5)+32;
# print(f"The Temperature in Farenheit is {faren}")


# radius = float(input("Enter the radius of circle: "))
# PI = 3.14
# area = PI * radius * radius
# print(f"The area of circle is {area} having radius {radius}")


# User_Name = input("Enter Your Name: ")
# principal_amount = float(input("Enter the Principal Amount: "))
# rate_of_interest = float(input("Enter the Rate of Interest (in %): "))  
# time_period = float(input("Enter the Time Period (in years): "))
# simple_interest = (principal_amount * rate_of_interest * time_period) / 100 

# # If-elif-else
# marks = int(input("Enter your marks: ")) # It takes input from user and converts it to integer

# if marks >= 80 :
#     print("Grade A") # If marks are 80 or above, print Grade A
# elif marks >= 65 :
#     print("Grade B") # If marks are 65 or above but less than 80, print Grade B
# elif marks >= 50 :
#     print("Grade C") # If marks are 50 or above but less than 65, print Grade C
# elif marks >= 35 :
#     print("Pass")    # If marks are 35 or above but less than 50, print Pass
# else :
#     print("Fail")    # If marks are less than 35, print Fail

# # The class problem
# girls_count = int(input("Enter the no of girls present in class : "))
# boys_count = int(input("Enter the no of boys present in class : "))
# tubligts = ["tub1" , "tub2" , "tub3" , "tub4"]
# fan = ["fan1" , "fan2" , "fan3" , "fan4" , "fan5" , "fan6"]
# if boys_count >= 10 and girls_count >= 10 :
#     print(f"For girls the {tubligts[2]} is on and the {fan[5]} is on")
#     print(f"For boys the {tubligts[0]} is on and the {fan[0]} is on")
# elif boys_count >= 25 and girls_count >= 25 :
#     print(f"For girls the {tubligts[3]} is on and the {fan[4]} is on")
#     print(f"For boys the {tubligts[0]} is on and the {fan[3]} is on")


# WAP to print the simple interest with bonus of a employee
employee_name = input("Enter Employee Name: ")
principal_amount = float(input("Enter the Principal Amount: ")) 
rate_of_interest = float(input("Enter the Rate of Interest (in %): "))
time_period = float(input("Enter the Time Period (in years): "))
bonus_percentage = float(input("Enter the Bonus Percentage (in %): "))
simple_interest = (principal_amount * rate_of_interest * time_period) / 100
bonus_amount = (simple_interest * bonus_percentage) / 100
total_amount = principal_amount + simple_interest + bonus_amount
print(f"Employee Name: {employee_name}")
print(f"Simple Interest: {simple_interest}")
print(f"Bonus Amount: {bonus_amount}")
print(f"Total Amount: {total_amount}")
    

