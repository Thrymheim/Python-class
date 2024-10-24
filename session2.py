print("maziyar",end=" ")
print("kolagar")

name="maziyarkolagar"
name_with_hyphen = name[:4] + '-' + name[4:]
name_split = name[:4] + "\n" + name[4:] 
name_tab = name[:4] + "\t" + name[4:] 
print("Name with hyphen:", name_with_hyphen)
print("Name split into two lines:", name_split)
print("Name with tab:", name_tab)

name="maziyar"
print(f"hello my name is {name.title()} can program by:\n\t1:cpp\n\t2:python\n\t3:c#") 

firstName="maziyar"
lastName="kolagar"
fullName="{}  {}".format(firstName.upper(),lastName.title())
print(fullName)



userName="  maziyar      x        "
print(userName.lstrip())
print(userName.rstrip())
print(userName.strip())
x = userName.strip()
print(x)

name="amir123"
score=20
height=1.90

print(type(name))
print(type(score))
print(type(height))

z=5+3j #j represents the imaginary unit (√-1).
print(z.real)
print(z.imag)


a,b=2,3
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)
print(b//a)

#library
import math
print(math.sqrt(16))

name=input("please enter your name: ")
print(f"you`r name is {name}")
number=int(input())
print(f"your number is {number}")

a,b = int(input()),int(input())
print(a+b)
print(a*b)
print(a-b)
print(a/b)
print(a%b)
print(a**b)
print(b//a)

scores=[20,19,18,17,16,15,14]
print(scores)
print(scores[3])
print(type(scores))
print(len(scores))
print(sorted(scores))
print(sorted(scores, reverse=True))

