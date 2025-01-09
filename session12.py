# Parent Class: Vehicle (Encapsulation)
class Vehicle:
    def __init__(self, brand, model, year):
        self._brand = brand  # Protected attribute
        self._model = model  # Protected attribute
        self._year = year    # Protected attribute

    # Getter for brand
    def get_brand(self):
        return self._brand

    # Setter for brand
    def set_brand(self, brand):
        if len(brand) >= 2:
            self._brand = brand
            print("Brand updated successfully.")
        else:
            print("Brand must be at least 2 characters.")

    # Getter for model
    def get_model(self):
        return self._model

    # Setter for model
    def set_model(self, model):
        if len(model) >= 1:
            self._model = model
            print("Model updated successfully.")
        else:
            print("Model must be at least 1 character.")

    # Getter for year
    def get_year(self):
        return self._year

    # Setter for year
    def set_year(self, year):
        if 1900 <= year <= 2023:
            self._year = year
            print("Year updated successfully.")
        else:
            print("Year must be between 1900 and 2023.")


# Child Class: Car (Inheritance)
class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)  # Call the parent class constructor
        self._fuel_type = fuel_type  # Protected attribute

    # Getter for fuel_type
    def get_fuel_type(self):
        return self._fuel_type

    # Setter for fuel_type
    def set_fuel_type(self, fuel_type):
        if fuel_type in ["Petrol", "Diesel", "Electric"]:
            self._fuel_type = fuel_type
            print("Fuel type updated successfully.")
        else:
            print("Fuel type must be Petrol, Diesel, or Electric.")


# Create a Vehicle object
vehicle = Vehicle("Toyota", "Corolla", 2020)
print(vehicle.get_brand())  # Output: Toyota

# Create a Car object
car = Car("Ford", "Mustang", 2022, "Petrol")
print(car.get_brand())  # Output: Ford
print(car.get_fuel_type())  # Output: Petrol

    # Use setters
car.set_brand("Chevrolet")
car.set_model("Camaro")
car.set_year(2021)
car.set_fuel_type("Diesel")
print(car.get_brand())  # Output: Chevrolet
print(car.get_model())  # Output: Camaro
print(car.get_year())  # Output: 2021


####################################################################

# Part 3: Advanced OOP Concepts
# This session covers polymorphism, private, __str__, random, Time and datetime

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


#User guess - import random
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
