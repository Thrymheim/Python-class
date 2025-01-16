#While recap
counter = 1
while counter <= 5:
    print(counter)
    counter += 1

#factorial
n=int(input("please enter number:"))
i,fact=1,1
while i<=n:
  fact=fact*i #عدد  جدید را در عدد قبلی ضرب میکند
  #fact*=i
  i+=1
print(fact)

#Original == reverse ?
number = int(input("Enter a number: "))
original_number = number  # ذخیره عدد اصلی
reversed_number = 0

while number > 0:
    digit = number % 10  # گرفتن آخرین رقم
    reversed_number = reversed_number * 10 + digit  # اضافه کردن رقم به عدد برعکس
    number = number // 10  # حذف آخرین رقم

if original_number == reversed_number:
    print(f"The number {original_number} is a palindrome.")
else:
    print(f"The number {original_number} is not a palindrome.")

#Type_casting
# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Type casting to list (keys)
dict_to_list = list(my_dict)
print(dict_to_list)  # Output: ['a', 'b', 'c']

# Type casting to list (values)
dict_values_to_list = list(my_dict.values())
print(dict_values_to_list)  # Output: [1, 2, 3]

# Type casting to list (items)
dict_items_to_list = list(my_dict.items())
print(dict_items_to_list)  # Output: [('a', 1), ('b', 2), ('c', 3)]

# Original list
my_list = [1, 2, 3, 4]

# Type casting to tuple
list_to_tuple = tuple(my_list)
print(list_to_tuple)  # Output: (1, 2, 3, 4)

# Type casting to set
list_to_set = set(my_list)
print(list_to_set)  # Output: {1, 2, 3, 4}

# Original tuple
my_tuple = (1, 2, 3, 4)

# Type casting to list
tuple_to_list = list(my_tuple)
print(tuple_to_list)  # Output: [1, 2, 3, 4]

# Type casting to set
tuple_to_set = set(my_tuple)
print(tuple_to_set)  # Output: {1, 2, 3, 4}

# Original set
my_set = {1, 2, 3, 4}

# Type casting to list
set_to_list = list(my_set)
print(set_to_list)  # Output: [1, 2, 3, 4]

# Type casting to tuple
set_to_tuple = tuple(my_set)
print(set_to_tuple)  # Output: (1, 2, 3, 4)


#Function with Multiple Returns
def analyze_number(n):
    is_even = n % 2 == 0
    is_positive = n > 0
    return is_even, is_positive
number_info = analyze_number(-4)
print(f"Number analysis - Even: {number_info[0]} \n Positive: {number_info[1]}")

#Another example
def three_analyze_number(n):
    is_odd = n % 2 == 1
    is_negetive = n < 0
    is_big = n > 100
    return is_odd, is_negetive, is_big
number_info = three_analyze_number(-4)
print(f"Number analysis - Even: {number_info[0]} \n Positive: {number_info[1]} \n Big: {number_info[2]}")

#Decorators def
def greeting_decorator(func):
    def wrapper():
        print("Hello! The function is about to run.")
        func()  # Call the original function
        print("Goodbye! The function has finished running.")
    return wrapper

# Usage
@greeting_decorator
def say_hello():
    print("I'm saying hello!")
say_hello()

#Decorators def
def programming_decorator(func):
    def wrapper():
        print("Hello! Im Maziar and i am 20 years old and i live in Babol")
        func()  # Call the original function
        print("Its the art of making a computer do what you want it to do")
    return wrapper

# Usage
@programming_decorator
def say():
    print("I wanted to communicate with the computer")
say()

#sum_multiplyer_decorator
def sum_multiplyer_decorator(func):
    def wrapper(a, b):
        print(f"Original result: {func(a, b)}")
        result = func(a, b)
        print(f"Modified result: {result * 2}")
    return wrapper

# Usage
@sum_multiplyer_decorator
def sum_def(a, b):
    return a + b
sum_def(2, 3)

#Encoding
def reverse_encode(text):
    return text[::-1] 
#we put two : to make the reverse and the -1 is to reverse the string 
#if we put one : it will reverse the string but not the letters

# Example usage
text = "Hello"
encoded_text = reverse_encode(text)
print("Encoded:", encoded_text)

# Decoding is the same as encoding (reverse again)
decoded_text = reverse_encode(encoded_text)
print("Decoded:", decoded_text)

#Zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Zip the lists into a list of tuples
zipped = zip(names, ages)

zipped_list = list(zipped)
print(zipped_list)

#if theres a difference in the length of the lists it will stop at the shortest list
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30]

zipped = zip(names, ages)
print(list(zipped))

#class zip name, age, city
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

zipped = zip(names, ages, cities)

zipped_list = list(zipped)
print(zipped_list)


#For in the list
numbers = [x for x in range(1, 11)]
print(numbers)

#Another example
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares)

#Any and All
def check_conditions(numbers):
    #Checks if any number is even and if all numbers are positive
    any_even = any(x % 2 == 0 for x in numbers)
    all_positive = all(x > 0 for x in numbers)
    return any_even, all_positive

# Example usage
numbers = [1, 3, 5, 7, 8]
any_even, all_positive = check_conditions(numbers)
print(f"Any even number? {any_even}")
print(f"All numbers positive? {all_positive}")
