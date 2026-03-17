# Student Management System

# List to store student data
students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))
    student = {"name": name, "age": age, "marks": marks}
    students.append(student)
    print(f"Student {name} added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    print("All Students:")
    for i, student in enumerate(students):
        print(f"{i+1}. Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
    print()

def search_student():
    search_name = input("Enter student name to search: ")
    found = False
    for student in students:
        if student['name'].lower() == search_name.lower():
            print(f"Student Found: Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}\n")
            found = True
            break
    if not found:
        print("Student not found.\n")

def delete_student():
    delete_name = input("Enter student name to delete: ")
    for student in students:
        if student['name'].lower() == delete_name.lower():
            students.remove(student)
            print(f"Student {delete_name} deleted successfully!\n")
            return
    print("Student not found.\n")

def average_marks():
    if not students:
        print("No students to calculate average.\n")
        return
    total = sum(student['marks'] for student in students)
    avg = total / len(students)
    print(f"Average marks of students: {avg:.2f}\n")

def menu():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Average Marks")
        print("6. Exit")
        choice = input("Enter your choice: ")
        print()
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            average_marks()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!\n")

# Start the program
menu()