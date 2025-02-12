#when you want to show something to user you use print, whatever you write in between quotations, that will be print
print("Hello world")

#if you want to print variables, you should write the varaible name without quotations
message = "Hello world"
print(message)

print(2+2)

a = 2
b = 3
print(a+b)

#You can comment using CTRL + ?

#Lower_case
first_name="Maziyar"
#camelCase
firstName="Maziyar"

#Whe can use indexing for printing a single character in a word, or a list and...
firstName="Maziyar kolagar"
print(firstName)
print(firstName[3])
print(firstName[4])
#when you write negetive, it means start from the end and go to first
print(firstName[-12])

name="Maziyar kolagar"
print(name.upper())

ostad="MAZIYAR"
print(ostad.lower())

address="babol karegar sardaran10"
print(address.title())

name="Maziyar"
print(f"hello {name}")

#For better reading of numbers we can use _
x=1_000_000
print(x)

#\n works as Enter key
print("Maziyar\nkolagar")
#\t works as 8 space
print("Maziyar\tkolagar")

#end is basically reverse of \n
print("maziyar",end=" ")
print("kolagar")

#by using fstring u can both write your sentense and also print your variables 
name="maziyar"
print(f"hello my name is {name.title()} can program by:\n\t1:cpp\n\t2:python\n\t3:c#") 

#format is the same but its just useless honestly
firstName="maziyar"
lastName="kolagar"
fullName="{}  {}".format(firstName.upper(),lastName.title())
print(fullName)
