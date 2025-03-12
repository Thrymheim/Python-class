#جان سخت مروری 1
students = []
grades = []
while True:
    print("\nOptions:")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Display Students")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter student's name: ")
        grade = int(input("Enter student's grade: "))
        students.append(name)
        grades.append(grade)
        print(f"Added: {name} with grade {grade}")

    elif choice == '2':
        name = input("Enter student's name to remove: ")
        if name in students:
            index = students.index(name)
            removed_student = students.pop(index)
            removed_grade = grades.pop(index)
            print(f"Removed: {removed_student} with grade {removed_grade}")
        else:
            print("Student not found.")

    elif choice == '3':
        if not students:
            print("No students in the list.")
        else:
            print("Students and their grades:")
            for i in range(len(students)):
                print(f"{students[i]}: {grades[i]}")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid option. Please try again.")


#جان سخت 2
users = {
    'user1': {'username': 'maziyar', 'password': 'abc123', 'login_attempts': 0},
    'user2': {'username': 'amir', 'password': 'xyz789', 'login_attempts': 0},
    'user3': {'username': 'sara', 'password': '123456', 'login_attempts': 0}
}

max_attempts = 3
username = input("Enter username: ")
password = input("Enter password: ")

for user_id, user_info in users.items():
    if username == user_info['username']:
        if user_info['login_attempts'] >= max_attempts:
            print("Account locked! Too many attempts")
            break
        elif password == user_info['password']:
            print("Login successful!")
            user_info['login_attempts'] = 0
            break
        else:
            user_info['login_attempts'] += 1
            print(f"Wrong password! Attempts left: {max_attempts - user_info['login_attempts']}")
            break
else:
    print("Username not found!")

###############################################################

#In Python, tuples are immutable, which means that once a tuple is created, you cannot add, remove, or change its elements. 
# Tuple Basics
mixed_tuple = (1, 'Hello', 3.14, True, [1, 2, 3])
print(mixed_tuple)
print(len(mixed_tuple))
print(type(mixed_tuple))
print(mixed_tuple[0])  # Accessing first element

# Min and Max in Numeric Tuple
numeric_tuple = (23, 45, 12, 67, 89, 34)
print(f"Minimum: {min(numeric_tuple)}")
print(f"Maximum: {max(numeric_tuple)}")

# Multiple Tuples
teacher1 = ('John', 35, 'Math')
teacher2 = ('Sarah', 28, 'Physics')

name = input("Enter teacher name: ")
if name in teacher1:
    print(f"Found: {teacher1}")
elif name in teacher2:
    print(f"Found: {teacher2}")
else:
    print("Teacher not found")


#Excercise
teacher1 = ('John', 35, 'Math', 50000)
teacher2 = ('Sarah', 28, 'Physics', 48000)
teacher3 = ('Mike', 41, 'English', 52000)

subject = input("Enter subject to search: ")

if subject in teacher1:
    print(f"Teacher found: {teacher1}")
    print(f"Name: {teacher1[0]}")
    print(f"Salary: ${teacher1[3]}")

elif subject in teacher2:
    print(f"Teacher found: {teacher2}")
    print(f"Name: {teacher2[0]}")
    print(f"Salary: ${teacher2[3]}")

elif subject in teacher3:
    print(f"Teacher found: {teacher3}")
    print(f"Name: {teacher3[0]}")
    print(f"Salary: ${teacher3[3]}")

else:
    print("No teacher found for this subject")


# Nested Tuples
school_data = (
    ('Class A', ('John', 'Mary', 'Peter')),
    ('Class B', ('Sarah', 'Tom', 'Lucy'))
)
print(school_data[0][1][1])  # Access students in Class A

#Excercise
tournament_data = (
    ('Team Red', ('Alex', 'Emma', 'James')),
    ('Team Blue', ('Sofia', 'Lucas', 'nolan')),
    ('Team Green', ('Noah', 'Lily', 'Oliver'))
)

# Print specific players
print(tournament_data[0][1][0])  # Prints: Alex (first player of Team Red)
print(tournament_data[1][1][2])  # Prints: Mia (last player of Team Blue)
print(tournament_data[2][0])     # Prints: Team Green (team name)

# Print all players from Team Red
print("Team Red players:", tournament_data[0][1])


# Tuple Methods
grades = (95, 87, 92, 95, 87, 90)
print(f"Number of 87s: {grades.count(87)}") #how many 87s is there
print(f"Index of first 95: {grades.index(95)}") #where is 95

# Slicing Tuples
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[2:5])    # Elements from index 2 to 4
print(numbers[:4])     # Elements from start to index 3
print(numbers[6:])     # Elements from index 6 to end
print(numbers[::2])    # Every second element

# Tuple in Loop
courses = ('Python', 'Java', 'C++', 'JavaScript')
for course in courses:
    print(f"We offer {course} programming")

#Excercise
destinations = ('Paris', 'Tokyo', 'Rome', 'New York', 'Dubai')
landmarks = ('Eiffel Tower', 'Mount Fuji', 'Colosseum', 'Statue of Liberty', 'Burj Khalifa')
for i in range(len(destinations)):
    print(f"In {destinations[i]}, you can visit the {landmarks[i]}")

#Class - Define two students with grades
student1 = ('Alice', 20, 'Biology', (85, 90, 78))
student2 = ('Bob', 22, 'Mathematics', (88, 92, 95))

# Input from user for student name
student_name = input("Enter student name (Alice/Bob): ")

if student_name == student1[0]:
    print(f"Found: {student1}")
    print(f"Grades: {student1[3]}")
elif student_name == student2[0]:
    print(f"Found: {student2}")
    print(f"Grades: {student2[3]}")
else:
    print("Student not found")

#Excercise
# Define book tuples
book1 = ('Pride and Prejudice', 'Jane Austen', 1813)
book2 = ('To Kill a Mockingbird', 'Harper Lee', 1960)
book3 = ('The Great Gatsby', 'F. Scott Fitzgerald', 1925)
# List of books
books = [book1, book2, book3]
# Input from user for book title or author
search = input("Enter book title or author: ")
# Search for the book
for book in books:
    if search.lower() == book[0].lower() or search.lower() == book[1].lower():
        print(f"Found: {book[0]}")
        print(f"Author: {book[1]}, Year: {book[2]}")
        break
else:
    print("Book not found")


#Type cast
#convert dictionary to tuple
student_dict = {'name': 'Alice', 'age': 20, 'major': 'Biology'}
student_tuple = tuple(student_dict.items())
print(student_tuple)

#convert tuple to dictionary
student_tuple = (('name', 'Alice'), ('age', 20), ('major', 'Biology'))
student_dict = dict(student_tuple)
print(student_dict)

#convert list to tuple
student_list = ['Alice', 20, 'Biology']
student_tuple = tuple(student_list)
print(student_tuple)

#convert list to dictionary
student_list = ['Alice', 20, 'Biology']
student_dict = dict(enumerate(student_list)) #when we use enumerate it will add index to the list
print(student_dict)



#Macth case
day = input("Enter a day (mon/tue/wed/thu/fri/sat/sun): ").lower()

match day:
    case "sat" | "sun":
        print("It's weekend! Time to relax!")
    case "fri":
        print("It's Friday! Weekend is coming!")
    case "mon":
        print("It's Monday! Fresh week ahead!")
    case _:
        print("It's a regular weekday!")


#Write match case for month
month = input("Enter a month (jan/feb/mar/apr/may/jun/jul/aug/sep/oct/nov/dec): ").lower()
match month:
    case "jan" | "mar" | "may" | "jul" | "aug" | "oct" | "dec":
        print("This month has 31 days.")
    case "apr" | "jun" | "sep" | "nov":
        print("This month has 30 days.")
    case "feb":
        print("This month has 28 days (or 29 in a leap year).")
    case _: #_case means if the input is not in the list it will print this message
        print("Invalid month.")

# Match the operation and perform calculation
# Get the operation from user
operation = input("Enter operation (+, -, *, /): ")
# Get two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

match operation:
    case "+":
        result = num1 + num2
        print(f"Addition: {num1} + {num2} = {result}")
    
    case "-":
        result = num1 - num2
        print(f"Subtraction: {num1} - {num2} = {result}")
    
    case "*":
        result = num1 * num2
        print(f"Multiplication: {num1} * {num2} = {result}")
    
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Division: {num1} / {num2} = {result}")
        else:
            print("Error: Cannot divide by zero")
    
    case _:
        print("Invalid operation")
