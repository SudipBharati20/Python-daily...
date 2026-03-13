# Student Grade Analyzer
# This program takes student information and calculates the grade.

print("Welcome to the Student Grade Analyzer")

# Taking input
name = input("Enter student name: ")
math = float(input("Enter Math marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calculating total and average
total = math + science + english
average = total / 3

# Determining grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

# Output
print("\n----- Result -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)