#معرفی نامه
name='maziyar'
age='kolagar'
city='babol'
print(f'my name is {name.title()} and im {age} years old and im from {city.upper()} and i programming ')

#اعمال ریاضی
x, y =2, 3
print(f'the sum of x and y = {x+y}')
print(f'the subtract of x and y = {x-y}')
print(f'the multiply of x and y = {x*y}')
print(f'the divide x and y = {x/y}')

##################################################################

#indexing
name='maziyar'
print(name[0])

userName="  maziyar      x        "
#remove space from left
print(userName.lstrip())
#remove space from right
print(userName.rstrip())
#remove space from both sides
print(userName.strip())

#or u can write like this with puting it in a variable
x = userName.strip()
print(x)

#Types
name="Maziyar123"
score=20
height=1.90
alive = True

print(type(name))
print(type(score))
print(type(height))
print(type(alive))

#library
import math
print(math.sqrt(16))

#input is for getting data from user
name=input("please enter your name: ")
print(f"you`r name is {name}")

#for gettting number input we use int(input())
number=int(input())
print(f"your number is {number}")

#Example
a,b = int(input()),int(input())
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)
print(b//a)

#list
scores=[20,19,18,17,16,15,14]
#printing whole list
print(scores)
#printing a specific index --> starts from 0
print(scores[3])
#printing the type of scores
print(type(scores))
#printing our list length --> starts from 1
print(len(scores))
#printing our list sorted
print(sorted(scores))
print(sorted(scores, reverse=True))
#using our list in a sentence
print(f'Hello my grade is {scores[3]}')

#Example
y=["python","cpp","c#","java","php"]
print(y)
print(type(y))
print(len(y))
print(sorted(y))
print(sorted(y, reverse=True))
print(f"{y[0]}\n {y[1]}\n{y[2]}\n{y[3]}\n{y[4]}")

#MAX and MIN and SUM
numbers = [3, 7, 2, 11, 5]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#Replace
students = ["amir","ALI","mmd"]
students [1] = "ahmad"
print (students)

#append which comes from the end
students = ["amir","ALI","mmd"]
students.append ("morteza")
print (students)

#append input
students = ["amir","ALI","mmd"]
students.append(input("Plz enter a name : "))
print (students)

#insert --> append always add in the end of the list but with insert u chose where to input 
students = ["amir","ALI","mmd"]
students.insert(int(input("Plz enter a number : ")),input("Plz enter a name : "))
print (students)

#del
students = ["amir","ALI","mmd"]
del students [2]
print (students)

#pop
students = ["amir","ALI","mmd"]
deletedStudents=students.pop(0)
print (deletedStudents)
print (students)

#Remove
students = ["amir","ALI","mmd"]
students.remove ("amir")
print (students) 

#slicing
students = ["amir","ALI","mmd"]
print (students[0:2])

#Copy list
students = ["amir","ALI","mmd"]
studentsA = students[0:2] 
print (studentsA)

#Zip - with zip u can combine 2 lists
students = ["amir","ALI","mmd"]
Grades = [18,19,20]
studentsGrades = zip(students,Grades)
print(list(studentsGrades))

#Example
students = ["amir","ALI","mmd"]
Grades = [18,19,20]
schools = ["1","2","3"]
studentsGrades = zip(students,Grades,schools)
print(list(studentsGrades))

#is and is not
a = [1 , 2, 3]
b = [1 , 2, 4]
c = a
print(a is b)
print(a is c)


#if and elif and else
number = int(input("pls enter a number : "))
if number > 10 :
 print ("pass")
elif number == 10 :
 print ("that was close")
else :
 print ("fail")

#Example
seasson=int(input())
if seasson==1:
  print("bahar")
elif seasson==2:
  print("tabestan")
elif seasson==3:
  print("paiiz")
elif seasson==4:
  print("zemestan")
else:
  print("Error")

#Example
name = input("pls enter a name")
if name == "maziyar" :
 print ("ostad")
else :
 print ("student")

#Example
name=input()
# != means not equeal, == means equal, >= means equal and higher, <= means equal or lower
if name!="maziyar":
  print("student")
else:
  print("ostad")

#and --> works when all of our conditions are True
number = int(input("pls enter a number so i tell u if u can divide it by 6 "))
if number%2==0 and number%3==0 :
 print ("yes u can divide it")
else :
 print ("no u cant")

#or --> works when atleast one of our conditions is True
number = int(input("Enter a number "))
if number>10 or number==10 :
 print ("pass")
else :
 print ("fail")

 
#if u want to check if a word is in a list u can use "in"
fruits = ["apple", "banana", "cherry"]
word = input("Enter a word: ")
if word.lower() in fruits: #not in is basically this but reversed
    print("The word is in the list")
else:
    print("The word is not in the list")

#Example
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
if a>=b and a>=c :
 print (a)
elif b>=c and b>=a :
 print (b)
else:
 print (c) 
    
