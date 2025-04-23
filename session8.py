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
##########################################################################################3
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


# Part 2: Inheritance And Encapsulation
# Basic inheritance 
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
