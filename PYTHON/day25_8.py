# Ask how many students
n = int(input("Enter number of students: "))

students = []
marks = []

# Taking input
for i in range(n):
    name = input("Enter student name: ")
    mark = float(input("Enter marks obtained: "))

    students.append(name)
    marks.append(mark)

# Finding highest, lowest and average
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

# Grade calculation based on average
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Output
print("\nStudent List:", students)
print("Marks List:", marks)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Grade based on Average:", grade)