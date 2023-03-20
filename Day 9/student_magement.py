# Write a program to manage student information (student code, student name and gpa)
# The program will have the following functions:
# 1. Add a new student
# 2. Display all students
# 3. Search a student by student code
# 4. Delete a student by student code
# 5. Update a student by student code
# 6. Find best student who has the highest gpa
codes = [] 
names = []
gpas = []

def print_menu():
    print(' ~~~~ Student Management System ~~~~')
    print('1. Add a new student')
    print('2. Display all students')
    print('3. Search a student by student code')
    print('0. Exit')

def add_student():
    # Add a new student to the list by asking user to input student code, 
    # student name and gpa
    name = input('Enter student name: ')
    code = input('Enter student code: ')
    gpa = float(input('Enter student gpa: '))

    names.append(name)
    codes.append(code)
    gpas.append(gpa)

    print('Student added successfully!')

def display_all():
    print(f'There are {len(codes)} students in the system')
    for i in range(len(codes)):
        print(f'Code: {codes[i]:10} Name: {names[i]:25} GPA: {gpas[i]:5}')

def search_student():
    # Search a student by student code by for loop, use found position to get name & gpa
    found = False
    code = input('Enter student code to search: ')
    for i in range(len(codes)):
        if code == codes[i]:
            found = True
            print(f'Found student: Name: {names[i]:25} GPA: {gpas[i]:5}')
            break
    if not found:
        print(f'Student not found for code {code}!')

def delete_student():
    # Todo
    # Ask user to enter student code
    # Find student with that code and delete it, print not found if not found
    pass

def update_student():
    # Todo
    # Ask user to enter student code
    # Find student with that code and update it (ask new name, new gpa)
    # print not found if not found
    pass

def find_best_student():
    # Todo
    # Use max algorithm to find the best student and print name & code corresponding
    pass

running = True
while running:
    print_menu()
    choice = input('Enter your choice: ')
    if choice == '1': add_student()
    elif choice == '2': display_all()
    elif choice == '3': search_student()
    elif choice == '0': running = False