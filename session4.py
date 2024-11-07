#Bozorgtarin addad
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
if a>=b and a>=c :
 print (a)
elif b>=c and b>=a :
 print (b)
else:
 print (c) 
    
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

#che addaie
x = int(input("Please enter a number : "))
numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
if x > 9 or x < 0 :
 print ("Out of range")
else :
 print (numbers[x])  

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

#if u want to check if a word is in a list u can use "in"
# Check if a word is in a list
fruits = ["apple", "banana", "cherry"]
word = input("Enter a word: ")
if word.lower() in fruits: #not in is basically this but reversed
    print("The word is in the list")
else:
    print("The word is not in the list")

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

# Example:
# n = 123
# digit = n % 10 → digit = 123 % 10 = 3
# print(digit, end=" ") → Outputs 3 (the last digit).
# counter += 1 → counter becomes 1.
# n = n // 10 → n now becomes 123 // 10 = 12

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
##############################################################################
#Taklif bashe
numbers=[]
while True:
  number=int(input("please enter number: "))
  numbers.append(number)
  option=input("do you want continue?y/n")
  if option.lower()=='n':
    break

print(sum(numbers)/len(numbers))