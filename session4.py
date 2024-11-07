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
  fact*=i #عدد  جدید را در عدد قبلی ضرب میکند --> fact = fact * i
  i+=1 #i = i + 1
print(fact)

#رقم های یک عدد را باهم جمع میکند
# Ask the user to enter an integer  
n = int(input("Please enter an integer n: "))  # For example, if the user inputs 123    
sum = 0  
# Loop while n is greater than 0  
while n > 0:  
    # Add the last digit of n to sum  
    sum = sum + (n % 10)  # For 123, this adds 3 (123 % 10)  
    # Remove the last digit from n and when n got only one digit left just add the digit to sum
    n //= 10  # Now n becomes 12 (123 // 10)  
# Print the sum of the digits 
print(sum)  # For 123, this will eventually print 6 (3 + 2 + 1)

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
