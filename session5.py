#Ebarat sharti
num = int(input('Enter a number : '))  
if num % 2 == 0:  
    print('zog')  
else:  
    print('fard')  

#تعداد ارقام
number = int(input("enter a number: "))
count = 0
while number:
    number //= 10  
    count += 1
print(f" {count}")


#ایا معکوس با عدد فعلی برابر است؟
n=int(input("please enter n: "))
reverse=0
temp=n
while n>0:
  reverse=reverse*10+(n%10)
  n//=10
# print(reverse)
if reverse==temp:
  print("yes")
else:
  print("no")

#ترکیبی قوی و مهم 
numbers=[]
while True:
  number=int(input("please enter number: "))
  numbers.append(number)
  option=input("do you want continue? (yes/no) : ")
  if option.lower()=='no':
    break

print(sum(numbers)/len(numbers))

#######################################################################
#continue with while
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

#loop - for
#First is start, second is end point, third how to go if we write nothing its 1
for i in range(0,20):
  print("hello")

#but wat if we want it to go as x number we enter?
n=int(input())
for i in range (0,n+1) :
 print (i)

#and if for example i want it go like 0 2 4 6
n=int(input())
for i in range (0,n,2) :
 print (i)

#takes number 5 time and and multiplies it by 2 
for i in range(0,5):
  number=int(input())
  print(number*2)

# Example 5: Nested for loops to create a multiplication table  
for i in range(1, 6):  # Outer loop for rows  
    for j in range(1, 6):  # Inner loop for columns  
        print(f"{i} * {j} = {i * j}")  
    print()  # Print a new line after each row

#for in list
students = ["amir","ali","reza"]
for student in students :
 print (f"hello {student.title()}")

#Average
numbers = [20,9,8,7,6,3,16]
avg = 0
for number in numbers :
  avg +=number
  #avg = avg + number
print (avg/len(numbers))

students ["ali","ghadir","goli","mmd","reza"]
programmers = ["ali","ghadir"]
for student in students :
 if student in programmers :
  print (f"hello {student} student and programmer")
 else :
  print (f"hello {student} student")

#Continue
for i in range(0,20):
  if i==6:
    continue
  print(i)

#break
for i in range(0,10):
    if i == 3:
        break
    print(i)

# عدد اول عددی است که تنها بر یک و خود بخش پذیر باشد
n=int(input("please enter number: "))
for i in range(2,n):
  if n%i==0:
    print("No")
    break
else:
  print("Yes")
