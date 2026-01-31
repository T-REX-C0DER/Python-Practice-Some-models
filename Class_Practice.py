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

# If-elif-else
marks = int(input("Enter your marks: "))

if marks >= 80 :
    print("Grade A")
elif marks >= 65 :
    print("Grade B")
elif marks >= 50 :
    print("Grade C")
elif marks >= 35 :
    print("Pass")
else :
    print("Fail")