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

#جان سخت مروری 2
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

#شهرکتاب
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

#مدرسه تاپلی
student1 = ('Alice', (85, 90, 78))
student2 = ('Bob', (88, 92, 95))
student3 = ('Charlie', (80, 85, 88))
# List of students
students = [student1, student2, student3]
# Input from user for student name
student_name = input("Enter student name (Alice/Bob/Charlie): ")
# Search for the student and calculate average score
for student in students:
    if student_name.lower() == student[0].lower():
        name = student[0]
        scores = student[1]
        average_score = sum(scores) / len(scores)
        print(f"{name}'s average score: {average_score}")
        break
else:
    print("Student not found")

###################################################

#File
#Write in file
file=open('products.txt','w')
file.write("namayandeh ha\nmohesen")

#Read file
productsFile=open('products.txt','r')
print(productsFile.read())

#Append to existing file
file=open('products.txt','a')
file.write("amir")

#Class
#Create new file and then write your name and age in it and then read it
file=open('Me.txt','w')
file.write("Maziyar\n20")
file=open('Me.txt','r')
print(file.read())

# Dictionary of students with grades and info
students = {
    "Alice": {
        "age": 20,
        "grades": [85, 90, 92],
        "active": True
    },
    "Bob": {
        "age": 19,
        "grades": [75, 82, 88],
        "active": False
    }
}

# Class
# Create a new file and write student records to it name, active, age, average, and grade status A B C D
file = open('student_data.txt', 'w')
file.write("STUDENT RECORDS\n")

# Process each student
for student_name, student_data in students.items():
    print(f"\nStudent: {student_name}")
    
    # Check status
    if student_data["active"]:
        status = "Currently Enrolled"
    else:
        status = "Not Enrolled"
        
    # Calculate average directly
    average = sum(student_data["grades"]) / len(student_data["grades"])
    
    # Grade evaluation
    if average >= 90:
        grade_status = "A"
    elif average >= 80:
        grade_status = "B"
    elif average >= 70:
        grade_status = "C"
    else:
        grade_status = "D"
    
    # Write to file
    file = open('student_data.txt', 'a')
    file.write(f"\n{student_name}\n")
    file.write(f"Status: {status}\n")
    file.write(f"Age: {student_data['age']}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Grade: {grade_status}\n")
    
    # Display on screen
    print(f"Status: {status}")
    print(f"Age: {student_data['age']}")
    print(f"Average: {average}")
    print(f"Grade: {grade_status}")

#Set
#Set is unpedictable and u cant edit it and it cant have repedetive items
shiriniha = {"tar","Khmeie","napoleini"}
print(shiriniha)
for shirini in shiriniha :
    print(shirini)

#if we have duplicate like two 3 in set, set will delete one of them so we cant have duplicate in set
shiriniha = {"tar","Khmeie","napoleini", "tar"}
print(shiriniha)

#Add
shiriniha = {"tar","Khmeie","napoleini"}
shiriniha.add("khoshk")
print(shiriniha)

#Remove --> if item not in set we get error
shiriniha = {"tar","Khmeie","napoleini"}
shiriniha.remove("tar")
shiriniha.remove("khoshk") #not in the set and gives error
print(shiriniha)

#Discard --> if item not on set we wont get error
shiriniha = {"tar","Khmeie","napoleini"}
shiriniha.discard("tar")
shiriniha.remove("khoshk") #not in the set and wont give error
print(shiriniha)

#Union - ejtema in another varaible
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho"}
cars=car1.union(car2)
print (cars)

#Or u can use Update
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho"}
car1.update(car2)
print (car1)
print (car2)

#Intersection - Eshterak in another variable
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
eshtrakcars=car1.intersection(car2)
print(eshtrakcars)

#Or u can use update
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
car1.intersection_update(car2)
print(car1)

#Symmetric difference (egtema bedon eshtrak)
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
sc=car1.symmetric_difference(car2)
print(sc)

#Or u can use update
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
car1.symmetric_difference_update(car2)
print(car1)

#Class
# Step 1: Create sets for courses
math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Bob", "Eve", "Frank", "Charlie"}
# Step 3: Add a student
math_students.add("Grace")
print("Updated Math Students:", math_students)
# Step 4: Remove a student
math_students.remove("David")
print("After removing 'David':", math_students)
# Step 5: Union of sets اجتماع
all_students = math_students.union(science_students)
print("All Unique Students:", all_students)
# Step 6: Intersection of sets اشتراک
common_students = math_students.intersection(science_students)
print("Students in Both Courses:", common_students)
# Step 7: Symmetric difference اجتماع بدون اشتراک
unique_students = math_students.symmetric_difference(science_students)
print("Students in Only One Course:", unique_students)
# Step 8: Final Summary
print("\nSummary:")
print(f"Total Math Students: {len(math_students)}")
print(f"Total Science Students: {len(science_students)}")
print(f"Total Unique Students: {len(all_students)}")
print(f"Students Enrolled in Both Courses: {len(common_students)}")
print(f"Students Enrolled in Only One Course: {len(unique_students)}")
