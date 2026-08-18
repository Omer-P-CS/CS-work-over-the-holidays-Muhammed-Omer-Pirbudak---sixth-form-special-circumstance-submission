#Search through list of requested students, get used to flag variables
#Muhammed Omer Pirbudak (proof to LAET about work over the holidays) Applicaa code U-CU2XY

students = ["Ali", "Sarah", "John", "Emma", "David"]
grades = [78, 92, 65, 84, 71]
#Display students and their according grades 

for i in range(len(students)):
    print(f"{students[i]}: {grades[i]}")

nameSearchStore = input("Enter a student to view their grade: ").capitalize()

found = False 

for i in range(len(students)):          #--
    if nameSearchStore == students[i]:  #--Similar to
        found = True                    #--task 2
        foundIndex = i                  #--

if found:
    print("Student found")
    print(f"{students[foundIndex]}'s grade is: {grades[foundIndex]}")
else:
    print("Student does not exist")

#Everything except for lines 15 and 19 were done by me and I've understood the material 
