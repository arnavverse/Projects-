'''
=====================================
 STUDENT RESULT MANAGEMENT SYSTEM
=====================================
What is the idea of the project?
Imagine you are a school teacher and need to calculate a student's result.
The program will take details from the user, perform calculations, and print the result.

--------------
grade_system
A+ : 90+
A : 80-89
B : 70-79
C : 60-69
D : 50-59
E : 33-49
F : Below 33
--------------
'''

print('''===========================
  STUDENT RESULT SYSTEM
========== MENU ===========
1. Add Student Result
2. View Result
3. Exit
===========================''')

name = input("ENTER STUDENT NAME : ")
eng_marks = input("ENTER ENGLSIH MARKS = ")
maths_marks = input("ENTER MATHEMATICS MARKS = ")
phy_marks = input("ENTER PHYSICS MARKS = ")
chem_marks = input("ENTER CHEMISTRY MARKS = ")
pe_marks = input("ENTER PHYSICAL EDUCATION MARKS = ")
total = int(phy_marks) + int(chem_marks) + int(maths_marks) + int(eng_marks) + int(pe_marks)
percentage = (total/5)
print('''=====================================
          RESULT CARD
=====================================''')
print("STUDENT :",name.capitalize())
print("TOTAL :",total,"/500")
print("PERCENTAGE :",percentage,"%")

if (percentage >= 90):
    print("Grade : A+")
elif (percentage >= 80):
    print("Grade : A")
elif (percentage >= 70):
    print("Grade = B")
elif (percentage >= 60):
    print("Grade : C")
elif (percentage >= 50):
    print("Grade : D")
elif (percentage >= 33):
    print("Grade : E")
else:
    print("Grade : F")

if (total < 165):
    print("RESULT : FAIL❗️")
else:
    print("RESULT : PASS 🎉")
print("----------------------------------------------")
