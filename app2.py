
student_grades = {}

def add_student(name, grade):
    
    student_grades[name] = grade
    print(f"Student {name} added with grade {grade}.")

def update_grade(name, grade):
   
    if name in student_grades:
        student_grades[name] = grade
        print(f"Student {name} updated with grade {grade}.")
    else:
        print(f"Student {name} not found.")

def print_grades():
   
    if student_grades:
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No student records found.")


while True:
    print("\nChoose an option:")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        name = input("Enter student's name: ")
        grade = input("Enter student's grade: ")
        add_student(name, grade)
    
    elif choice == "2":
        name = input("Enter student's name: ")
        grade = input("Enter new grade: ")
        update_grade(name, grade)
    
    elif choice == "3":
        print_grades()
    
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
