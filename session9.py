#کار با فایل
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
# Create a new file and write student records to it name, active, age, average
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
    
    # Write to file
    file = open('student_data.txt', 'a')
    file.write(f"\n{student_name}\n")
    file.write(f"Status: {status}\n")
    file.write(f"Age: {student_data['age']}\n")
    file.write(f"Average: {average}\n")
    
    # Display on screen
    print(f"Status: {status}")
    print(f"Age: {student_data['age']}")
    print(f"Average: {average}")

#توابع ابتدایی
def check_backpack(item):
    backpack = {
        "sword": 1,
        "shield": 1,
        "potion": 5,
        "gold": 100
    }
    
    if item in backpack:
        print(f"You have {backpack[item]} {item}(s) in your backpack!")
    else:
        print(f"You don't have any {item} in your backpack!")

check_backpack("potion")    
check_backpack("sword")     
check_backpack("axe")       

#سینما پارادایس
movies = {
    "morning": "12 Angry Men",
    "evening": "Django Unchained",
    "night": "A clockwork orange"
}

# Viewers for each show stored in sets
morning_viewers = {"Mina", "Ali", "Sara", "Reza"}
evening_viewers = {"Ali", "Nima", "Sara", "Tina"}
night_viewers = {"Sara", "Saman"}

# Check who's watching multiple shows
all_day_viewers = morning_viewers.intersection(evening_viewers)
print("Loyal viewers watching multiple shows:", all_day_viewers)

# Total unique viewers today
total_viewers = morning_viewers.union(evening_viewers).union(night_viewers)
print(f"Total unique viewers today: {len(total_viewers)}")

# Count how many shows each loyal viewer watched
for viewer in all_day_viewers:
    show_count = 0
    if viewer in morning_viewers:
        show_count += 1
    if viewer in evening_viewers:
        show_count += 1
    if viewer in night_viewers:
        show_count += 1
    print(f"{viewer} watched {show_count} shows today")


# Show which movies each viewer watched
for viewer in total_viewers:
    viewer_movies = []
    if viewer in morning_viewers:
        viewer_movies.append(movies["morning"])
    if viewer in evening_viewers:
        viewer_movies.append(movies["evening"])
    if viewer in night_viewers:
        viewer_movies.append(movies["night"])
    print(f"{viewer} watched: {viewer_movies}")

#######################################################################

# یک و دو در جلسه قبل تدریس شدند

# 3. Functions with Parameters
def multiplyFive(n):
    print(f"{n} multiplied by 5 = {n * 5}")
#we give it a number
multiplyFive(10) 

#user gives it a number
number = int(input("Please enter number to multiply: "))
multiplyFive(number)

# 4. Functions with Default Parameters
def Greet(name="amir", age=23):
    print(f"name is {name} and {age} year's old")
Greet(name="ali", age=20)

# 5. Functions with Return Values - they do the job but wont print anything until we print it
def multiplyFive(n):
    return n * 5
multiplyFive(5) # --> this will not print anything
print(f"Direct print: {multiplyFive(5)}")
#user gives it a number
result = int(input("Please enter number for multiplication: "))
print(f"Result stored in variable: {multiplyFive(result)}")

# 6. Factorial Function with return
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(f"Factorial of 5 is: {factorial(5)}")

# توابع بازگشتی - مثال های اضافی برای یادگیری بیشتر
#6.Sum function
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)
print(f"Sum of first 5 numbers: {sum_recursive(5)}")

# توابع بازگشتی - مثال های اضافی برای یادگیری بیشتر
# 6. Factorial Function 
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)
print(f"Factorial of 5 (recursive): {factorial_recursive(5)}")

# توابع بازگشتی - مثال های اضافی برای یادگیری بیشتر
# 6. Power Function - recursive
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
print(f"2^3 = {power(2, 3)}")

# 7. Multiple Parameters
def greet(name, lastName, age):
    return f"my name is {name} {lastName} and i am {age} year's old"
#do it with user input
name,lastname,age = input("Please enter your name, lastname and age: ").split() #split() splits the input by space
print(greet(name,lastname,age))

#8. Calculator
def calculate(operation, a, b):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"
print(f"Add 5 and 3: {calculate('add', 5, 3)}")

# 9. Dictionary Return
def makeDictionary(username, password, email):
    return {
        'username': username,
        'password': password,
        'email': email
    }

#First way - using variables
user_info = makeDictionary("maziyar", "1234", "maziyarkolagar@gmail.com")
print(f"User Info: {user_info}")

#or like this - using input and variables
username,password,email = input("Please enter username and passsword and email: ").split()
user_info2 = makeDictionary(username, password, email)
print(f"User Info: {user_info2}")

# 10. Arbitrary Arguments آرگومان دلخواه
# * means that we can pass as many arguments as we want
def sayHello(*names):
    for name in names:
        print(f"hello {name}")
sayHello("amir", "reza", "jfr", "mani")

# 11. Temperature Converter 
def convertToFahrenheit(*degrees):
    for degree in degrees:
        print(f"{degree}°C = {(degree * 1.8) + 32}°F")
convertToFahrenheit(10, 20, 30)

# 12. Keyword Arguments
# ** means that we can pass as many key and value arguments as we want
def introduceFoods(**foods):
    print("Menu Prices:")
    for food, price in foods.items():
        print(f"{food} ----> {price}$")
introduceFoods(burger=50, pizza=300, chicken=200)

# 13. Lambda Functions
#its same as 
def multiply(x, y):
     return x * y
print(f"Multiply 5 and 3: {multiply(5, 3)}")

#What lambda does is to take a function and return it
multiply = lambda x, y: x * y
print(f"Multiply 5 and 3: {multiply(5, 3)}")

# 14. Nested Functions
def outer_function(x):    # Defines outer function that takes parameter x
    def inner_function(y):    # Defines inner function that takes parameter y
        return x + y          # Adds outer parameter x with inner parameter y
    return inner_function     # Returns the inner function
add_five = outer_function(5)  # Creates new function where x is fixed to 5
print(f"Adding 5 to 3: {add_five(3)}")  # Calls add_five with y=3, prints result

# 15. Function with Error Handling
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except :
        return "Please enter numbers only"
print("Testing different division cases:")
print(f"Normal division: {divide_numbers(10, 2)}")
print(f"Division by zero: {divide_numbers(10, 0)}")
print(f"String input: {divide_numbers('10', 2)}")
