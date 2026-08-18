#Task: develop a manual linear-search algorithm with student list, search through list one at a time and compare with user's input then display the student's name and index
#Muhammed Omer Pirbudak (proof to LAET about work over the holidays) Applicaa code U-CU2XY
students = ["Ali", "Sarah", "John", "Emma", "David", "Hassan", "Zara"]

for i in range(len(students)):
    print(f"{i + 1}: Student: {students[i]}") #here and before done by me

nameSearchStore = input("Enter a student to search: ").capitalize()

found = False

for i in range(len(students)):
    if nameSearchStore == students[i]: #checks if inputted value aligns with an item in the array
        found = True #here and before done by me
        foundIndex = i #aided by chat gpt --- one mistake here (1)
if found:
    print("Student found")
    print(f"{students[foundIndex]} is at index {foundIndex}.") #originally wrote {i} instead of foundIndex another mistake here (2)
else: 
    print("Student doesn't exist")
