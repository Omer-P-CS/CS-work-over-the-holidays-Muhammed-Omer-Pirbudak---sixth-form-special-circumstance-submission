#Student dictionary manager Muhammed Omer Pirbudak - Applicaa code U-CU2XY
#Major topic I didn't learn or learnt too litte
students = {
    "Ali": 78,
    "Sarah": 92,
    "John": 65,
    "Emma": 84,
    "David": 71
}

for student in students:
    print(f"{student}: {students[student]}") # student becomes each individual key and the keys behave like the individual indexes in the array then first print the keys then use the keys to print their assigned values

#2 attempts

studentSearch = input("Enter a student to search for: ").capitalize()

if studentSearch in students:
    print("Student found")
    print(f"{studentSearch}'s grade is: {students[studentSearch]}")
else:
    print("Student not found")

#2 attempt I accidentally made a for loop and AI corrected me to get rid of it otherwise the rest is my work 

giveStudent = input("Enter a new student: ")
giveGrade = int(input("Enter their grade: "))

students[giveStudent] = giveGrade #if student exists, change their value if not add a new key with value pair that is giveGrade

print(f"{giveStudent}'s grade is: {students[giveStudent]}")

#2 attempt

alterListStudent = input("Enter a student whose grade you want to change: ").capitalize()

if alterListStudent in students:
    newGrade = int(input("Enter their new grade: ")) #if inputted name is in the array then request user to input new grade 
    students[alterListStudent] = newGrade #new grade is the modified value for inputted (correct) key
    print(f"{alterListStudent}'s grade has been changed to {students[alterListStudent]}")
else:
    print("Student does not exist")
#3 attempts had to get assistance with chatGPT for line 39 only

removeStudent = input("Enter a student to remove: ").capitalize()

if removeStudent in students:
    students.pop(removeStudent) #if inputted user exists then .pop() will remove the inputted key and its value pair along with it
    print(f"{removeStudent} has been removed.")
else:
    print("Student does not exist")
#1 attempt 



print("Updated students:")

for student, grade in students.items():
    print(f"{student}: {grade}")
#lines 58 and 59 are the ones that confused me apparently you can represent key and value with two local variables in a for loop only for dictonaries in this situation long as you use the .items() dictionary code 
#attempts 5
# Part 7 — Count the students

print(f"Number of students: {len(students)}")
#1 attempt
