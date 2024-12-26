#بازشگت معکوس
def reverseNumber(n):
    temp, reverse = n, 0
    while temp > 0:
        reverse = reverse * 10 + (temp % 10)
        temp //= 10
    if n == reverse:
        print(f"{n} is palindrome")
    else:
        print(f"{n} is not palindrome")

reverseNumber(121)
reverseNumber(123)

#مدریت کلاس
def manage_students(*names):
    for name in names:
        print(f"Welcome to class {name}!")
    
    scores = {}
    for name in names:
        score = int(input(f"Enter score for {name}: "))
        scores[name] = score
    
    print("\nClass Report:")
    for name, score in scores.items():
        if score >= 90:
            print(f"{name}: A")
        elif score >= 80:
            print(f"{name}: B")
        else:
            print(f"{name}: Need improvement")

manage_students("Ali", "Sara")

#فوتبال
def track_points(**players):
    high_score = 0
    champion = ""
    
    for player, points in players.items():
        print(f"{player} scored: {points}")
        if points > high_score:
            high_score = points
            champion = player
    
    return f"Champion is {champion} with {high_score} points!"

# Get player data from user
players = {}
num_players = int(input("How many players? "))

for i in range(num_players):
    name = input(f"Enter player {i+1} name: ")
    score = int(input(f"Enter {name}'s score: "))
    players[name] = score

# Use the function with collected data
result = track_points(**players)
print(result)


# فیبوناچی
def print_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
# Use it
print_fibonacci(10)

#########################################################################
# OOP (Object Oriented Programming)
# Part 1: Introduction to Classes and Objects

#What is class?
print(type(1))
print(type('s'))
print(type([1,2,3]))

#First Example: Student Class
class Student:
    #constructor
    #method is a function inside a class
    #_init__ is a special method that is called when an object is created from a class
    def __init__(self,firstName,lastName,score) :
        #self is a reference to the current object being created
        self.firstName=firstName
        self.lastName=lastName
        self.score=score

s = Student("amir","ahmadi",20)
print(s.firstName)
print(s.lastName)
print(s.score)
print(type(s))
#for changing name or something
s.firstName="ali"
print(s.firstName)

#Class - make your own class of name, lastname, age, and programmig language

#Class Attributes
#1. Class Attributes
class Student:
    #class attribute
    #class attribute is shared by all objects of a class
    schoolName="Mojtama fani tehran"
    age = 18
    def __init__(self,firstName,lastName,score) :
        self.firstName=firstName
        self.lastName=lastName
        self.score=score
    def calculateBirthyear(self) :
        return 2023 - self.age
s = Student("amir","ahmadi",20)
print(s.schoolName)
print(s.calculateBirthyear())

#Class - Mostatil Class - ussing input - no method
class Mostatil :
    def __init__ (self,tol,ars) :
        self.tol=tol
        self.ars=ars
s=Mostatil(int(input('tol: ')),int(input('ars: ')))
print(f"masahat = {s.tol * s.ars} and mohit {(s.ars + s.tol)*2}")   

#Class - Method is a function in a class
class Mostatil :
     def __init__ (self,tol,ars) :
         self.tol=tol
         self.ars=ars
     def masahat(self) :
          print(self.tol * self.ars)
     def mohit(self) :
          print((self.ars + self.tol)*2)    
s=Mostatil(int(input('tol: ')),int(input('ars: ')))
print(f"masahat = {s.masahat()} and mohit {s.mohit()}")

#Employee Class
class Employee : 
    def __init__ (self,firstName,lastName,birthday,company,sallery,hiredYear):
        self.firstName=firstName
        self.lastName=lastName
        self.birthday=birthday
        self.company=company
        self.sallery=sallery
        self.hiredYear=hiredYear
    def printInfo(self):     
        print(f"{self.firstName} {self.lastName} {self.birthday} {self.company} {self.sallery} {self.hiredYear}")
    def getAge(self):
        print(f"{1402-self.birthday}")
    def getTotalSallery(self):
        print(self.sallery * (1402-self.hiredYear) * 12) 
    def increaseSallery(self,value):
        self.sallery=self.sallery + (value/100) * self.sallery
employee=Employee("Maziyar","kolagar",1000,"google",1383,1398)
employee.printInfo()
employee.getAge()
employee.getTotalSallery()
employee.increaseSallery(15)                 

#None
class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount = None
        self.last_item_added = None
    
    def add_item(self, item):
        self.items.append(item)
        self.last_item_added = item
    
    def set_discount(self, discount_code):
        if discount_code == "SAVE10":
            self.discount = 0.1
        else:
            self.discount = None
    
    def get_last_added(self):
        return self.last_item_added if self.last_item_added else "No items added yet"
# Create cart
cart = ShoppingCart()
# Check last added when empty
print(cart.get_last_added())  # Output: "No items added yet"
# Add items
cart.add_item("Book")
cart.add_item("Laptop")
print(cart.get_last_added())  # Output: "Laptop"
# Try discount
cart.set_discount("SAVE10")
print(cart.discount)  # Output: 0.1

#Class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def print_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")

# Creating and using Student objects
student1 = Student("Ali", "1001")
student2 = Student("Sara", "1002")

student1.add_grade(18)
student1.add_grade(20)
student2.add_grade(19)

student1.print_info()
print("\n")
student2.print_info()

#User guess - import random
import random

class NumberGuesser:
    def __init__(self):
        self.secret = random.randint(1, 10)
    
    def check_guess(self, guess):
        if guess == self.secret:
            print("You got it! 🎉")
        elif guess > self.secret:
            print("Too high! ⬆️")
        else:
            print("Too low! ⬇️")

game = NumberGuesser()
guess = int(input("Guess a number between 1-10: "))
game.check_guess(guess)

#Timer - import time
import time

class Timer:
    def countdown(self, seconds):
        print("Go!")
        for i in range(seconds):
            print(seconds - i)
            time.sleep(1) #Wait for 1 second
        print("Done!")

t = Timer()
t.countdown(3)

###############################################################

#Dice - import random
import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.current_value = None
        self.roll_history = []
    
    def roll(self):
        self.current_value = random.randint(1, self.sides)
        self.roll_history.append(self.current_value)
        return self.current_value
    
    def get_roll_history(self):
        return self.roll_history
    
    def get_average_roll(self):
        if self.roll_history:
            return sum(self.roll_history) / len(self.roll_history)
        return 0

# Create a regular 6-sided die
my_dice = Dice()

# Roll it 5 times
print("Rolling the dice 5 times:")
for i in range(5):
    result = my_dice.roll()
    print(f"Roll {i+1}: {result}")

# Show statistics
print("\nRoll history:", my_dice.get_roll_history())
print(f"Average roll: {my_dice.get_average_roll():.2f}")

# Create a special 20-sided die (like in D&D)
d20 = Dice(20)
print("\nRolling a 20-sided die:")
print("Result:", d20.roll())


#Class - Book Class
class Book:
    library_name = "City Library"
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.current_borrower = None
        self.borrow_history = []
    
    def borrow_book(self, student_name):
        if self.is_available:
            self.is_available = False
            self.current_borrower = student_name
            self.borrow_history.append(student_name)
            return f"{student_name} borrowed '{self.title}'"
        return f"'{self.title}' is not available"
    
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            self.current_borrower = None
            return f"'{self.title}' has been returned"
        return "Book already in library"
    
    def display_info(self):
        status = "Available" if self.is_available else f"Borrowed by {self.current_borrower}"
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")

# Example usage
book1 = Book("anna karenina", "Leo Tolstoy")
book2 = Book("100 years of solitude", "Gabriel Garcia Marquez")

print(book1.borrow_book("Alice"))
book1.display_info()

print(book2.borrow_book("Bob"))
print(book2.return_book())
book2.display_info()

