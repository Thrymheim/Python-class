class GameCharacter:
    
    def __init__(self, name, character_type):
        self.name = name
        self.character_type = character_type
        self.level = 1
        self.health = 100
        self.coins = 0
    
    def collect_coins(self, amount):
        self.coins += amount
        return f"{self.name} collected {amount} coins! Total: {self.coins}"
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        return f"{self.name} took {damage} damage! Health: {self.health}"
    
    def heal(self):
        if self.coins >= 10:
            self.coins -= 10
            self.health = 100
            return f"{self.name} is fully healed!"
        return f"Not enough coins! Need 10 coins to heal."
    
    def level_up(self):
        self.level += 1
        return f"Congratulations! {self.name} is now level {self.level}!"
    
    def display_stats(self):
        print(f"\nCharacter: {self.name}")
        print(f"Type: {self.character_type}")
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Coins: {self.coins}")

# Create a character
hero = GameCharacter("Thor", "Warrior")

# Play the game
print(hero.collect_coins(15))
print(hero.take_damage(30))
print(hero.heal())
print(hero.level_up())
hero.display_stats()


###################################################################################

# Part 2: Inheritance And Encapsulation
# This session covers fundamental inheritance concepts with practical examples

# For Encapsulation, we use protected and private attributes
class BankAccount:
    def __init__(self):
        self._balance = 0  # Protected attribute
    
    def get_balance(self):
        return f"${self._balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return "Deposit successful"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return "Withdrawal successful"
        return "Insufficient funds"

# Good way to use the account
account = BankAccount()
account.deposit(100)
print(account.get_balance())  # Shows $100
account.withdraw(50)
print(account.get_balance())  # Shows $50
# If we didn't use encapsulation, someone could do this:
# account._balance = -1000000  # This would be bad!



# Example 1: Person-Employee Hierarchy
# Demonstrates basic inheritance with getter/setter methods
class Person:
    def __init__(self, firstName, lastName, country, age, nc):
        self.firstName = firstName
        self.lastName = lastName
        self.country = country
        self.age = age
        self.nc = nc

class Employee(Person):
    def __init__(self, firstName, lastName, country, age, nc, salary, company):
        super().__init__(firstName, lastName, country, age, nc)
        self.salary = salary
        self.company = company

# Test Person-Employee
employee = Employee("Amir", "Amiri", "Iran", 20, 205, 2000, "google")
print(employee.firstName)


#SETTERS AND GETTERS:
#When you need to validate data before setting it
#When working with private or protected attributes
#When you need to perform additional operations during get/set

#This but with Setter and Getter:
class Person:
    def __init__(self, firstName, lastName, country, age, nc):
        self.firstName = firstName
        self.lastName = lastName
        self.country = country
        self.age = age
        self.nc = nc

    def setfirstName(self, firstName):
        if len(firstName) >= 2:
            self.firstName = firstName
            print("Name updated successfully")
        else:
            print("Name must be at least 2 characters")

    def setage(self, age):
        if 0 <= age <= 120:
            self.age = age
            print("Age updated successfully")
        else:
            print("Age must be between 0 and 120")

    def getfirstName(self):
        return self.firstName

    def getage(self):
        return self.age

class Employee(Person):
    def __init__(self, firstName, lastName, country, age, nc, salary, company):
        super().__init__(firstName, lastName, country, age, nc)
        self.salary = salary
        self.company = company

    def setsalary(self, salary):
        if salary >= 1000:
            self.salary = salary
            print("Salary updated successfully")
        else:
            print("Salary must be at least 1000")

    def getsalary(self):
        return self.salary

# Test
employee = Employee("Amir", "Amiri", "Iran", 20, 205, 2000, "google")
employee.setfirstName("A")  # Will show error message
employee.setfirstName("Ali")  # Will work
employee.setage(150)  # Will show error message
employee.setage(25)  # Will work
employee.setsalary(3000)  # Will work
print(employee.getfirstName())  # Shows Ali
print(employee.getage())  # Shows 25
print(employee.getsalary())  # Shows 3000


# Example 2: Food Hierarchy
# Shows inheritance with method overriding
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def show_info(self):
        print(f"{self.name}: ${self.price}")

class Pizza(Food):
    def __init__(self, name, price, toppings):
        super().__init__(name, price)
        self.toppings = toppings
    
    def add_topping(self):
        print(f"Added {self.toppings} to {self.name}")

class Drink(Food):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size
    
    def make_cold(self):
        print(f"Your {self.size} {self.name} is now cold!")

# Test Menu
pizza1 = Pizza("Pepperoni", 12, "extra cheese")
drink1 = Drink("Coca Cola", 3, "large")

pizza1.show_info()
pizza1.add_topping()
drink1.show_info()
drink1.make_cold()

#Protected - one underline in setter getter means protected and can be accessed inside the class and its subclasses
class Food:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    def set_name(self, value):
        self._name = value
    
    def set_price(self, value):
        self._price = value
    
    def show_info(self):
        print(f"{self._name}: ${self._price}")


class Pizza(Food):
    def __init__(self, name, price, toppings):
        super().__init__(name, price)
        self._toppings = toppings
    
    def get_toppings(self):
        return self._toppings
    
    def set_toppings(self, value):
        self._toppings = value
    
    def add_topping(self):
        print(f"Added {self._toppings} to {self._name}")


class Drink(Food):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size
    
    def get_size(self):
        return self._size
    
    def set_size(self, value):
        self._size = value
    
    def make_cold(self):
        print(f"Your {self._size} {self._name} is now cold!")

# Test Menu
pizza1 = Pizza("Pepperoni", 12, "extra cheese")
drink1 = Drink("Coca Cola", 3, "large")

# Using getters and setters
pizza1.show_info()
pizza1.add_topping()
drink1.show_info()
drink1.make_cold()

# Example of using getters and setters
print(pizza1.get_name())
drink1.set_size("medium")
print(drink1.get_size())


