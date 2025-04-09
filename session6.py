# #مدرسه تاپلی
# student1 = ('Alice', (85, 90, 78))
# student2 = ('Bob', (88, 92, 95))
# student3 = ('Charlie', (80, 85, 88))
# # List of students
# students = [student1, student2, student3]
# # Input from user for student name
# student_name = input("Enter student name (Alice/Bob/Charlie): ")
# # Search for the student and calculate average score
# for student in students:
#     if student_name.lower() == student[0].lower():
#         name = student[0]
#         scores = student[1]
#         average_score = sum(scores) / len(scores)
#         print(f"{name}'s average score: {average_score}")
#         break
# else:
#     print("Student not found")


# #سینما پارادایس
# movies = {
#     "morning": "12 Angry Men",
#     "evening": "Django Unchained",
#     "night": "A clockwork orange"
# }

# # Viewers for each show stored in sets
# morning_viewers = {"Mina", "Ali", "Sara", "Reza"}
# evening_viewers = {"Ali", "Nima", "Sara", "Tina"}
# night_viewers = {"Sara", "Saman"}

# # Check who's watching multiple shows
# all_day_viewers = morning_viewers.intersection(evening_viewers)
# print("Loyal viewers watching multiple shows:", all_day_viewers)

# # Total unique viewers today
# total_viewers = morning_viewers.union(evening_viewers).union(night_viewers)
# print(f"Total unique viewers today: {len(total_viewers)}")

# # Count how many shows each loyal viewer watched
# for viewer in all_day_viewers:
#     show_count = 0
#     if viewer in morning_viewers:
#         show_count += 1
#     if viewer in evening_viewers:
#         show_count += 1
#     if viewer in night_viewers:
#         show_count += 1
#     print(f"{viewer} watched {show_count} shows today")


# # Show which movies each viewer watched
# for viewer in total_viewers:
#     viewer_movies = []
#     if viewer in morning_viewers:
#         viewer_movies.append(movies["morning"])
#     if viewer in evening_viewers:
#         viewer_movies.append(movies["evening"])
#     if viewer in night_viewers:
#         viewer_movies.append(movies["night"])
#     print(f"{viewer} watched: {viewer_movies}")
####################################################

#Set
#Set is unpedictable and u cant edit it and it cant have repedetive items
shiriniha = {"tar","Khmeie","napoleini"}
print(shiriniha)
for shirini in shiriniha :
    print(shirini)

#if we have duplicate like two 3 in set, set will delete one of them so we cant have duplicate in set
shiriniha = {"tar","Khmeie","napoleini", "tar"}
print(shiriniha)

#Add
shiriniha = {"tar","Khmeie","napoleini"}
shiriniha.add("khoshk")
print(shiriniha)

#Remove --> if item not in set we get error
shiriniha = {"tar","Khmeie","napoleini"}
shiriniha.remove("tar")
shiriniha.remove("khoshk") #not in the set and gives error
print(shiriniha)

#Discard --> if item not on set we wont get error
shiriniha = {"tar","Khmeie","napoleini"}
shiriniha.discard("tar")
shiriniha.remove("khoshk") #not in the set and wont give error
print(shiriniha)

#Union - ejtema in another varaible
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho"}
cars=car1.union(car2)
print (cars)

#Or u can use Update
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho"}
car1.update(car2)
print (car1)
print (car2)

#Intersection - Eshterak in another variable
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
eshtrakcars=car1.intersection(car2)
print(eshtrakcars)

#Or u can use update
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
car1.intersection_update(car2)
print(car1)

#Symmetric difference (egtema bedon eshtrak)
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
sc=car1.symmetric_difference(car2)
print(sc)

#Or u can use update
car1={"bmw","benz","prado","ferrari"}
car2={"pride","peikan","pezho","bmw"}
car1.symmetric_difference_update(car2)
print(car1)

#File
#Write in file
file=open('name.txt','w')
file.write("Maziyar")

#Read file
file=open('name.txt','r')
print(file.read())

#Append to existing file
file=open('name.txt','a')
file.write(" kolagar")

#Create new file and then write your name and age in it and then read it
file=open('Me.txt','w')
file.write("Maziyar\n20")
file=open('Me.txt','r')
print(file.read())


# Define the students dictionary first
students = {
    "Alice": {"active": True, "age": 20, "grades": [85, 90, 78]},
    "Bob": {"active": True, "age": 22, "grades": [88, 92, 95]},
    "Charlie": {"active": False, "age": 21, "grades": [80, 85, 88]}
}

# Class
# Create a new file and write student records to it name, active, age, average, and grade status A B C D
file = open('student_data.txt', 'w')
file.write("STUDENT RECORDS\n")

# Process each student
for student_name, student_data in students.items():
    print(f"\nStudent: {student_name}")
    
    # Check status
    if student_data["active"]:
        status = "Currently Enrolled"
    else:
        status = "Not Enrolled"
        
    # Calculate average directly
    average = sum(student_data["grades"]) / len(student_data["grades"])
    
    # Grade evaluation
    if average >= 90:
        grade_status = "A"
    elif average >= 80:
        grade_status = "B"
    elif average >= 70:
        grade_status = "C"
    else:
        grade_status = "D"
    
    # Write to file - use append mode
    file.write(f"\n{student_name}\n")
    file.write(f"Status: {status}\n")
    file.write(f"Age: {student_data['age']}\n")
    file.write(f"Average: {average}\n")
    file.write(f"Grade: {grade_status}\n")
    
    # Display on screen
    print(f"Status: {status}")
    print(f"Age: {student_data['age']}")
    print(f"Average: {average}")
    print(f"Grade: {grade_status}")

# Close the file when done
file.close()
