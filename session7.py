#فیبوناچی
n = int(input('Enter a number : '))  # Number of Fibonacci numbers to generate
a = 0  # Starting with 0 as first Fibonacci number
b = 1  # Second Fibonacci number
count = 0
while count < n:
    print(a, end=' ')
    temp = a  # Store current 'a' temporarily
    a = b     # Move 'b' to 'a'
    b = temp + b  # New 'b' is sum of previous numbers
    count += 1

#لیستکشنری
favoriteLanguages={
  'amir':'cpp',
  'ali':'farsi',
  'zolfaghari':'csharp'
}
programmers=["amir","zolfaghari"]
for name in favoriteLanguages.keys():
  if name in programmers:
    print(f"{name} is programmer and student")
  else:
    print(f"{name} just a student")

#مرتبب کردن
favoriteLanguages={
        'amir':'cpp',
        'ali':'python',
        'zolfaghari':'csharp'
    }
for key in sorted(favoriteLanguages) :
   print (key, favoriteLanguages[key])  

#مدرسه
students = {
    'Alex': 85,
    'Beth': 92,
    'Charlie': 78,
    'Diana': 95
}
# Add new student score
new_student = input("Enter student name: ")
new_score = int(input("Enter their score: "))
students[new_student] = new_score
# Find highest and lowest scores
highest_score = max(students.values())  
lowest_score = min(students.values())
# Print all students with their grades
print("\nClass Scores:")
for student, score in students.items():
    print(f"{student}: {score}")
print(f"\nHighest score: {highest_score}")
print(f"Lowest score: {lowest_score}")

######################################################

#Dictionary can be in list
users=[{'username':'amir','password':'a123'},{'username':'agha reza','password':'r123'},{'username':'babak','password':'b123'}]
username,password=input("please enter username: "),input("please enter password: ")
for user in users:
  if user['username']==username and password==user['password']:
    print("login")
    break
else:
  print("you need sign up at first")

#List can be in dictionary
programmers={
  'amir':['cpp','python','web'],
  'ali':['python'],
  'maziyar':['cpp','python','c#','django']
}
for name,skills in programmers.items():
  print(f"{name} skills: ")
  for skill in skills:
    print(f"\t{skill}")

#Dictionary can be in another dictionary
students={
  'amir':{'age':23,'skill':'python'},
  'ali':{'age':25,'skill':'cpp'},
  'zolfaghari':{'age':22,'skill':'csharp'}
}
for name,info in students.items():
  print(f"{name} info: {info}")

#Another example
books = {
    'book1': {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    'book2': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    'book3': {'title': 'Iliad', 'author': 'Homer', 'year': '8th century BC'}
}
for book_id, details in books.items():
    print(f"{book_id} details: {details}")

#In Python, tuples are immutable, which means that once a tuple is created, you cannot add, remove, or change its elements. 
# Tuple Basics
mixed_tuple = (1, 'Hello', 3.14, True, [1, 2, 3])
print(mixed_tuple)
print(type(mixed_tuple))
print(mixed_tuple[0])  # Accessing first element

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

# Nested Tuples
school_data = (
    ('Class A', ('John', 'Mary', 'Peter')),
    ('Class B', ('Sarah', 'Tom', 'Lucy'))
)
print(school_data[0][1][1])  # Will print student from first row, second col, number 1 in tuple --> Mary

# Tuple Methods
grades = (95, 87, 92, 95, 87, 90)
print(f"Number of 87s: {grades.count(87)}")
print(f"Index of first 95: {grades.index(95)}")

# Slicing Tuples
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(numbers[2:5])    # Elements from index 2 to 4
print(numbers[:4])     # Elements from start to index 3
print(numbers[6:])     # Elements from index 6 to end

# Tuple in Loop
courses = ('Python', 'Java', 'C++', 'JavaScript')
for course in courses:
    print(f"We offer {course} programming")

# Finding Length of Tuple
print(f"Number of elements: {len(mixed_tuple)}")

# Min and Max in Numeric Tuple
numeric_tuple = (23, 45, 12, 67, 89, 34)
print(f"Minimum: {min(numeric_tuple)}")
print(f"Maximum: {max(numeric_tuple)}")

#Example
student1 = ('Alice', 20, 'Biology', (85, 90, 78))
student2 = ('Bob', 22, 'Mathematics', (88, 92, 95))
student_name = input("Enter student name (Alice/Bob): ")
if student_name == student1[0]:
    print(f"Found: {student1}")
    print(f"Grades: {student1[3]}")
elif student_name == student2[0]:
    print(f"Found: {student2}")
    print(f"Grades: {student2[3]}")
else:
    print("Student not found")

#PIP (pip Install Packages)
pip install Django #Enter this in your terminal
django-admin startproject projectname #write this in CMD and put your project name in projectname
python manage.py migrate #In our project terminal
python manage.py runserver #In our project terminal
