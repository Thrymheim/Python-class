# Part 3: Advanced OOP Concepts
# This session covers polymorphism, private and method overriding

#Shape Polymorphism - Means using one method for multiple classes the way it can adjust itself for each one
class Shape:
    def calculate_area(self):
        print("Area calculation method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        area = self.length * self.width
        print(f"Rectangle area: {area}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Circle area: {area}")

# Test Shapes
rect = Rectangle(5, 3)
circle = Circle(4)
rect.calculate_area()
circle.calculate_area()

#Another example - Class
class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement this")

class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Credit Card (Charging 2% fee: ${amount * 1.02})")

class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal (Charging $1 flat fee: ${amount + 1})")

class Crypto(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing ${amount} via Crypto (No fees! ${amount})")

# Test Polymorphism
payment_methods = [CreditCard(), PayPal(), Crypto()]
amount = 100
for method in payment_methods:
    method.process_payment(amount)  # Same method, different behavior

#Private Employee
class Employee:
    def __init__(self, firstName, lastName, birthday, company, sallery, hiredYear):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthday = birthday
        self.__company = company
        self.__sallery = sallery
        self.__hiredYear = hiredYear

    # Setters
    def setFirstName(self, firstName):
        self.__firstName = firstName
    def setLastName(self, lastName):
        self.__lastName = lastName
    def setbirth(self, birthday):
        self.__birthday = birthday
    def setcom(self, company):
        self.__company = company
    def setsall(self, sallery):
        self.__sallery = sallery
    def sethire(self, hiredYear):
        self.__hiredYear = hiredYear

    # Getters
    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getbirth(self):
        return self.__birthday
    def getcom(self):
        return self.__company
    def getsall(self):
        return self.__sallery
    def gethire(self):
        return self.__hiredYear

    # String representation of the class
    def __str__(self):
        return f"my name is {self.__firstName} {self.__lastName} {self.__birthday} {self.__company} {self.__sallery} {self.__hiredYear}"

# Test Encapsulated Employee
employee = Employee("Maziyar", "kolagar", 1000, "google", 1383, 1398)
print(employee)
employee.setFirstName("amir")
print(employee.getFirstName())

import random
class NumberGuesser:
    def __init__(self):
        self.secret = random.randint(1, 10)
    
    def check_guess(self, guess):
        if guess == self.secret:
            print("You got it!")
            return True  # Return True if the guess is correct
        elif guess > self.secret:
            print("Too high!")
        else:
            print("Too low!")
        return False  # Return False if the guess is incorrect

game = NumberGuesser()

while True:
    guess = int(input("Guess a number between 1-10: "))
    if game.check_guess(guess):
        break  # Exit the loop if the guess is correct
    

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


#datetime - Getting current date and time
import datetime
now = datetime.datetime.now()
print(now)
