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

#Class Attributes
class Student:
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

#Method is a function in a class
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
employee=Employee("Maziyar","kolagar",1000,"google",1383,1398)
employee.printInfo()
employee.getAge()
employee.getTotalSallery()

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
