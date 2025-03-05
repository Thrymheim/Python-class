#تعداد ارقام
number = int(input("enter a number: "))
count = 0
while number:
    number //= 10  
    count += 1
print(f" {count}")

#ترکیبی قوی و مهم 
numbers=[]
while True:
  number=int(input("please enter number: "))
  numbers.append(number)
  option=input("do you want continue? (yes/no) : ")
  if option.lower()=='no':
    break
print(sum(numbers)/len(numbers))

#مثلث خیام
n = int(input("Enter number of rows: "))
for i in range(0, n):
    for j in range(i):
        print(1, end=" ")
    print()

# تخفیف
for i in range(0, 5):
    price = int(input(f"Enter price {i+1}: "))
    
    if price > 100:
        discount = price * 0.1
        new_price = price - discount
        print(f"Price after 10% discount: {new_price}")
    else:
        print(f"Price: {price} (no discount)")
      
######################################################################

#Dictionary
user={
  'username':'Maziyar',
  'password':'a123',
  'email':'Maziyar@gmail.com',
  'age':23,
  'isTeacher':True
}
print(user)
print(type(user))
print(user['email'])

student={
  'name':'adabi',
  'nc':'7788',
  'schoolName':'alghadir',
  'age':23
}
#modify/edit
student['schoolName']='tizhoshan'
print(student)

#add key,value
student['number']=9111
print(student)

#delete
del student['nc']
print(student)

#Pop
deletedValue=student.pop('nc')
print(deletedValue)
print(student)

#deletes last item
deletedValue=student.popitem()
print(deletedValue)
print(student)

#get in dictionary
#if i type print(student['shirtColors']) i get error so i use get
message1=student.get('shirtColor','we dont have this key')
message2=student.get('schoolName','we dont have this key')
print(message1)
print(message2)

#show all
print(student.items())
for key,value in student.items():
  print(f"{key}--->{value}")

#Show key - show value
print(student.keys())
print(student.values())

#Excersie
favoriteLanguages={
  'amir':'cpp',
  'ali':'python',
  'mmd':'csharp'
}
print(favoriteLanguages.items()) #key + value
print(favoriteLanguages.keys())
print(favoriteLanguages.values())

#Excersie
user1={
  'username':'Maziyar',
  'password':'a123'
}
user2={
  'username':'amir',
  'password':'zzz111'
}
username,password=input("please enter username: "),input("please enter password: ")
if username==user1['username'] and password==user1['password']:
  print("login")
elif username==user2['username'] and password==user2['password']:
  print('login')
else:
  print("cant login")

#This method gets the keys and values together
for name,language in favoriteLanguages.items():
  print(f"{name.upper()} favorite language is {language.title()}")
#This method gets only the keys first, then uses dictionary for values
for name in favoriteLanguages.keys():
  print(f"{name.upper()} favorite language is {favoriteLanguages[name].title()}")

#Dictionary can be in list
users=[{'username':'amir','password':'a123'},{'username':'agha reza','password':'r123'},{'username':'babak','password':'b123'}]
username,password=input("please enter username: "),input("please enter password: ")
for user in users:
  if user['username']==username and password==user['password']:
    print("login")
    break
else:
  print("you need sign up at first")

#List can be in dictionary
programmers={
  'amir':['cpp','python','web'],
  'ali':['python'],
  'maziyar':['cpp','python','c#','django']
}
for name,skills in programmers.items():
  print(f"{name} skills: ")
  for skill in skills:
    print(f"\t{skill}")

#Dictionary can be in another dictionary
students={
  'amir':{'age':23,'skill':'python'},
  'ali':{'age':25,'skill':'cpp'},
  'zolfaghari':{'age':22,'skill':'csharp'}
}
for name,info in students.items():
  print(f"{name} info: {info}")

#Excersie
books = {
    'book1': {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    'book2': {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    'book3': {'title': 'Iliad', 'author': 'Homer', 'year': '8th century BC'}
}
for book_id, details in books.items():
    print(f"{book_id} details: {details}")
