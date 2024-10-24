print("amir",end=" ")
print("hajitabar")

name="amirhajitabar"
name_with_hyphen = name[:4] + '-' + name[4:]
name_split = name[:4] + "\n" + name[4:] #class to do
name_tab = name[:4] + "\t" + name[4:] #class to do
print("Name with hyphen:", name_with_hyphen)
print("Name split into two lines:", name_split)
print("Name with tab:", name_tab)

name="amir"
print(f"hello my name is {name.title()} can program by:\n\t1:cpp\n\t2:python\n\t3:c#") #class to do an example

firstName="amir"
lastName="hajitabar"
fullName="{} hossein {}".format(firstName.upper(),lastName.title())
print(fullName) #class to do with they name and language they about to learn


#Tell them the diffrence between these two, one just print it and one actually do it
userName="  amir"
print(userName.lstrip())
userName=userName.lstrip()
print(userName)

password="amir123  "
password=password.rstrip()
print(f"{password}correct")

city="   babol  "
city=city.strip()
print(city)

name="amir123"
score=20
height=1.90

# type for showing data type of variable
print(type(name))
print(type(score))
print(type(height))

z=5+3j #j represents the imaginary unit (√-1).
print(z.real)
print(z.imag)

#tell about int and string numbers
a,b=2,3
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)
print(b//a)

money=16
DOLLAR=50000
print(money*50000)

#library
import math
print(math.sqrt(16))

name=input("please enter your name: ")
print(f"you`r name is {name}")
number=int(input())
print(type(number))
print(f"your answare is {number/5}")

c=complex(input())
print(c.real)
print(c.imag)

a,b,c,x=int(input()),int(input()),int(input()),int(input())

print(f"result--> {(a*x**2)+(b*x)+c}")

name="amirhossein"
print(len(name))

scores=[20,19,18,17,16,15,14]
print(scores)
print(scores[3])
print(type(scores))
print(len(scores))
print(sorted(scores))
print(sorted(scores, reverse=True))

