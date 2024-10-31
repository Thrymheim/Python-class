#For better reading of numbers we can use _
x=1_000_000
print(x)

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

#insert --> append always add in the end of the list but with insert u chose where to input *
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

number = int(input("pls enter a number : "))
if number > 10 :
 print ("pass")
elif number == 10 :
 print ("that was close")
else :
 print ("fail")

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

name = input("pls enter a name")
if name == "maziyar" :
 print ("ostad")
else :
 print ("student")

name=input()
if name!="maziyar":
  print("student")
else:
  print("ostad")

#and
number = int(input("pls enter a number so i tell u if u can divide it by 6 "))
if number%2==0 and number%3==0 :
 print ("yes u can divide it")
else :
 print ("no u cant")

#or
number = int(input("Enter a number "))
if number>10 or number==10 :
 print ("pass")
else :
 print ("fail")