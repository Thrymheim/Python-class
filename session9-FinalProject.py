class Customer:
    def __init__(self, name, password, fatherName, cash, ID):
        self.name = name
        self.password = password
        self.fatherName = fatherName
        self.cash = cash
        self.ID = ID
        self.loan = 0

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_fatherName(self):
        return self.fatherName

    def set_fatherName(self, fatherName):
        self.fatherName = fatherName

    def get_cash(self):
        return self.cash

    def set_cash(self, cash):
        self.cash = cash

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def get_loan(self):
        return self.loan

    def set_loan(self, loan):
        self.loan = loan

    def information(self):
        return f"Name: {self.name.title()}\tFather name: {self.fatherName.title()}\nCash amount: {self.cash}\tID: {self.ID}"

class Employee:
    def __init__(self, name, password, fatherName, ID):
        self.name = name
        self.password = password
        self.fatherName = fatherName
        self.ID = ID

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_fatherName(self):
        return self.fatherName

    def set_fatherName(self, fatherName):
        self.fatherName = fatherName

    def get_ID(self):
        return self.ID

    def set_ID(self, ID):
        self.ID = ID

    def information(self):
        return f"Name: {self.name.title()}\tFather name: {self.fatherName.title()}\nId: {self.ID}"

def isDuplicateID(id):
    for customer in AllCustomers:
        if customer.get_ID() == id:
            return True
    return False

def isDuplicateEmployeeID(id):
    for employee in AllEmployees:
        if employee.get_ID() == id:
            return True
    return False

def newCustomer():
    name = input("\nPlease enter the customer's name: ")
    fatherName = input("Please enter the customer's father's name: ")
    cash = int(input("Please enter the customer's cash amount: "))

    ID = int(input("Please provide the customer's ID number: "))
    while isDuplicateID(ID):
        print("ID already exists. Please provide a unique customer's ID number.")
        ID = int(input("Please provide the customer's ID number: "))

    password = input("Enter a password: ")

    customer = Customer(name, password, fatherName, cash, ID)
    AllCustomers.append(customer)
    print("\nInformation saved successfully!")

def showCustomer():
    for customer in AllCustomers:
        print(f"\nName: {customer.get_name()}")
        print(f"Father's Name: {customer.get_fatherName()}")
        print(f"ID: {customer.get_ID()}")
        print(f"Cash: {customer.get_cash() + customer.get_loan()}")

def findCustomer():
    findID = int(input("\nPlease enter the customer's ID: "))
    foundCustomer = None

    for customer in AllCustomers:
        if customer.get_ID() == findID:
            foundCustomer = customer
            break

    if foundCustomer:
        print(f"\nName: {foundCustomer.get_name()}")
        print(f"Father's Name: {foundCustomer.get_fatherName()}")
        print(f"ID: {foundCustomer.get_ID()}")
        print(f"Cash: {foundCustomer.get_cash() + foundCustomer.get_loan()}")
    else:
        print("\nThis customer doesn't exist")

def renameCustomer():
    findID = int(input("\nPlease enter the customer's ID: "))
    foundCustomer = None

    for customer in AllCustomers:
        if customer.get_ID() == findID:
            foundCustomer = customer
            break

    if foundCustomer:
        new_name = input("\nPlease enter the customer's new name: ")
        foundCustomer.set_name(new_name)
        print("\nInformation saved successfully!")
    else:
        print("\nThis customer doesn't exist")

def deleteCustomer():
    findID = int(input("\nPlease enter the customer's ID: "))
    foundCustomer = None

    for customer in AllCustomers:
        if customer.get_ID() == findID:
            foundCustomer = customer
            break

    if foundCustomer:
        AllCustomers.remove(foundCustomer)
        print("\nInformation saved successfully!")
    else:
        print("\nThis customer doesn't exist")

def loanCustomer():
    findID = int(input("\nPlease enter customer's ID: "))
    foundCustomers = [customer for customer in AllCustomers if customer.get_ID() == findID]

    if foundCustomers:
        for customer in foundCustomers:
            username = input("Please enter username: ")
            password = input("Please enter password: ")

            if customer.get_name() == username and customer.get_password() == password:
                loan = int(input("\nPlease enter the amount: "))

                if loan >= customer.get_cash():
                    customer.set_loan(loan)
                    print("\nInformation saved successfully!")
                else:
                    customer.set_cash(loan + customer.get_cash())
                    print("\nInformation saved successfully!")
            else:
                print("Wrong input!")
                break
    else:
        print("\nThis customer doesn't exist")

def newEmployee():
    name = input("\nPlease enter employee's name: ")
    fatherName = input("Please enter employee's father name: ")
    idNumber = int(input("Please provide employee's ID number: "))

    while isDuplicateEmployeeID(idNumber):
        print("ID already exists. Please provide a unique employee's ID number.")
        idNumber = int(input("Please provide employee's ID number: "))

    password = input("Enter a password: ")
    employee = Employee(name, password, fatherName, idNumber)
    AllEmployees.append(employee)
    print("\nInformation saved successfully!")

def showEmployee():
    for employee in AllEmployees:
        print(f"\nName: {employee.get_name()}")
        print(f"Father's Name: {employee.get_fatherName()}")
        print(f"ID: {employee.get_ID()}")

def findEmployee():
    findID = int(input("\nPlease enter employee's ID: "))

    for employee in AllEmployees:
        if employee.get_ID() == findID and employee.get_password() == input("Please enter password: "):
            print(f"\nName: {employee.get_name()}")
            print(f"Father's Name: {employee.get_fatherName()}")
            print(f"ID: {employee.get_ID()}")
            return

    print("Wrong input or employee not found")

def renameEmployee():
    findId = int(input("\nPlease enter employee's ID: "))

    for employee in AllEmployees:
        if employee.get_ID() == findId and employee.get_password() == input("Please enter password: "):
            new_name = input("\nPlease enter employee's new name: ")
            employee.set_name(new_name)
            print("\nInformation saved successfully!")
            return

    print("Wrong input or employee not found")

def deleteEmployee():
    findID = int(input("\nPlease enter employee's ID: "))

    for employee in AllEmployees:
        if employee.get_ID() == findID and employee.get_password() == input("Please enter password: "):
            AllEmployees.remove(employee)
            print("\nInformation saved successfully!")
            return

    print("Wrong input or employee not found")

AllCustomers = []
AllEmployees = []

while True:
    option = int(input("\nWelcome to our bank, how can we help you today? \n1-Add a customer\n2-Show all customers\n3-Find a customer\n4-Edit a customer\n5-Delete a customer\n6-Loan application\n7-Add an employee\n8-Show all employees\n9-Find an employee\n10-Edit an employee\n11-Delete an employee\n12-Exit\nEnter: "))

    if option == 1:
        newCustomer()
    elif option == 2:
        if AllCustomers:
            showCustomer()
        else:
            print("There are no customers")
    elif option == 3:
        if AllCustomers:
            findCustomer()
        else:
            print("There are no customers")
    elif option == 4:
        if AllCustomers:
            renameCustomer()
        else:
            print("There are no customers")
    elif option == 5:
        if AllCustomers:
            deleteCustomer()
        else:
            print("There are no customers")
    elif option == 6:
        if AllCustomers:
            loanCustomer()
        else:
            print("There are no customers")
    elif option == 7:
        newEmployee()
    elif option == 8:
        if AllEmployees:
            showEmployee()
        else:
            print("There are no employees")
    elif option == 9:
        if AllEmployees:
            findEmployee()
        else:
            print("There are no employees")
    elif option == 10:
        if AllEmployees:
            renameEmployee()
        else:
            print("There are no employees")
    elif option == 11:
        if AllEmployees:
            deleteEmployee()
        else:
            print("There are no employees")
    elif option == 12:
        print("Have a nice day!")
        break
    else:
        print("Wrong input!")
