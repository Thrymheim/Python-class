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

#File
#Write in file
file=open('name.txt','w')
file.write("Maziyar")

#Read file
file=open('name.txt','r')
print(file.read())

#Append to existing file
file=open('name.txt','a')
file.write(" kolagar")

#Create new file and then write your name and age in it and then read it
file=open('Me.txt','w')
file.write("Maziyar\n20")
file=open('Me.txt','r')
print(file.read())

# 1. Basic Function Definition
def sayHello():
    print("hello")
sayHello()

#Class write a function thar print name then last name and then print your age
def printall():
    print("maziyar")
    print("kolagar")
    print("20")
printall()

# 2. Functions with Input
def multiplyFive():
    n = int(input("Please enter number for multiplication: "))
    print(n * 5)
multiplyFive()

#class write a function that takes two numbers and return the sum of them
def sumTwoNumbers():
    n1 = int(input("Please enter number 1: "))
    n2 = int(input("Please enter number 2: "))
    print(n1 + n2)
sumTwoNumbers()

# 3. Functions with Parameters
def multiplyFive(n):
    print(f"{n} multiplied by 5 = {n * 5}")
#we give it a number
multiplyFive(10) 

#user gives it a number
number = int(input("Please enter number to multiply: "))
multiplyFive(number)
print()

# 4. Functions with Default Parameters
def Greet(name="amir", age=23):
    print(f"name is {name} and {age} year's old")

Greet()
Greet(name="ali", age=20)
print()

# 5. Functions with Return Values - they do the job but wont print anything until we print it
def multiplyFive(n):
    return n * 5
multiplyFive(5) # --> this will not print anything
print(f"Direct print: {multiplyFive(5)}")

#Class
#user gives it a number
result = int(input("Please enter number for multiplication: "))
print(f"Result stored in variable: {multiplyFive(result)}")

#Class
# 6. Factorial Function
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print(f"Factorial of 5 is: {factorial(5)}")

#Class power function
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result
print(f"2^3 = {power(2, 3)}")

#CLASS
#fact recurssive
def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

# Test with some values
for i in range(6):
    print(f"Factorial of {i} is {factorial(i)}")

#power recurive
def power(base, exponent):
    # Base case: any number raised to the power of 0 equals 1
    if exponent == 0:
        return 1
    
    # مثل فاکتوریل همینطوری از کم باید شروع کنه
    return base * power(base, exponent - 1)

# Get user input for base and exponent
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (a non-negative integer): "))

# Validate that exponent is non-negative
if exponent < 0:
    print("Please enter a non-negative exponent for this recursive function.")
else:
    # Calculate and display the result
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")


# 7. Multiple Parameters
def greet(name, lastName, age):
    return f"my name is {name} {lastName} and i am {age} year's old"

print(greet("Maziyar", "kolagar", 20))

#Class do it with user input
name,lastname,age = input("Please enter your name, lastname and age: ").split() #split() splits the input by space
print(greet(name,lastname,age))

#Class
# 8. Calculator
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
