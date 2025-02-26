#mashgh bagher
a = int(input("Enter first angle : "))
b = int(input("Enter second angle : "))
c = int(input("Enter third angle : "))
if a + b + c == 180 :
 print ("Yes")
else :
 print ("No") 

#kodam mah sale
x=int(input("Please enter a number : "))
months = ["farvardib","ordibehesht","khordad","tir","mordad","shahrivar","mehr","aban","azar","day","bahman","esfand"]
if x > 12 or x < 1 :
 print ("Wrong number")
else :
 print (months[x-1])  

#fisaghores
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a > 150 or a < 1 or b > 150 or b < 1 or c > 150 or c < 1 :
    print("Wrong number")

else :
    if (a**2) + (b**2) == (c**2) or (a**2) + (c**2) == (b**2) or (b**2) + (c**2) == (a**2) :
        print("Yes")

    else :
        print("No")

#behdasht va salamat
x = int(input("Please enter a number : "))
finalScore = 0 
Days = int(input("Please say how much day he was on travel : "))

if x > 20 or x < 0:
    print("Error")

else :
    if Days == 7 :
        finalScore = x
    elif Days == 0 :
        x=20
        finalScore = x   
    else :
        finalScore = x - Days
    if finalScore < 0 :
        x = 0
        finalScore = x

    print(f"Noroz score is {finalScore}")

#############################################################################################

# loop - for
# First is start, second is end point, third how to go if we write nothing its 1
for i in range(0,20):
  print("hello")

#Class
#but wat if we want it to go as x number we enter?
n=int(input())
for i in range (0,n+1) :
 print (i)

#and if for example i want it go like 0 2 4 6
n=int(input())
for i in range (0,n,5) :
 print (i)

#takes number 5 time and and multiplies it by 2 
for i in range(0,5):
  number=int(input())
  print(number*2)

# Example 5: Nested for loops to create a multiplication table  
for i in range(1, 6):  # Outer loop for rows  
    for j in range(1, 6):  # Inner loop for columns  
        print(f"{i} * {j} = {i * j}")  

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

#Example
students = ["ali","ghadir","goli","mmd","reza"]
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


# loops-While
i=0
while i<5:
  print("hello")
  i+=1

n=int(input("please enter number: "))
i=0
while i<=n:
  print(i)
  i+=1

#factorial
n=int(input("please enter number:"))
i,fact=1,1
while i<=n:
  fact=fact*i #عدد  جدید را در عدد قبلی ضرب میکند
  #fact*=i
  i+=1
print(fact)

#u can use both break and continue in while
#continue with while
i = 0
while i < 10:
    i += 1
    if i == 6:
        continue
    print(i)

#ارقام را میشکند و سراخر تعداد را میشمارد
n = int(input("Please enter n: "))  
original_n = n  # Keep the original value for later use  
counter = 0  
# First, let's find the total number of digits  
while n > 0:  
    digit = n % 10        # Get the last digit  
    print(digit, end=" ") # Print the digit  
    counter += 1          # Increment the counter  
    n = n // 10           # Remove the last digit  
print("\nTotal number of digits:", counter)

#رقم های یک عدد را باهم جمع میکند
n=int(input("please enter n: "))
sum=0
while n>0:
  sum=sum+(n%10) #sum=sum+n%10
  n//=10
print(sum)

#عدد را برعکس میکند
n = int(input("Please enter n: "))  
reverse = 0  
while n > 0:  
    digit = n % 10  
    reverse = reverse * 10 + digit  # Build the reversed number  
    n //= 10                        # Remove the last digit  
print("Reversed number:", reverse) 

#While True
while True:
  option=int(input("1-sayHello\n2-sayBye\n3-saypython\n4-exit\nenter option: "))
  if option==1:
    print("hello")
  elif option==2:
    print("bye")
  elif option==3:
    print("python")
  elif option==4:
    break
  else:
    print("you`r input invalid option,try agin please!")
