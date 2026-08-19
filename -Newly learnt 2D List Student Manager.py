# 2D List Student Manager - Muhammed Omer Pirbudak - Applicaa code U-CU2XY

# inner list = [student name, grade]

students = [
    ["Ali", 78],   # each list in 2d list is a row, column 0 = student name and column 1 is grade
    ["Sarah", 92],
    ["John", 65],
    ["Emma", 84],
    ["David", 71]
]

for student in students: # display every student and their grade
    print(f"{student[0]}: {student[1]}") # student represents the individual

# 2 attempts

studentSearch = input("Enter a student to search for: ").capitalize()

found = False # flag variable stays false unless changed (if met conditions)

for i in range(len(students)):
    if students[i][0] == studentSearch: # if (index meaning row) any of the rows' first column (for name) is same as the inputted studentSearch value then found is true
        found = True
        foundIndex = i # and new temp variable is whichever index meets the condition

# 1 attempt

if found:
    print("Student found")
    print(f"{students[foundIndex][0]}'s grade is: {students[foundIndex][1]}") # print the selected index with name because name is in column 0 and it's grade is column 1 as that contains the grades

else:
    print("Student not found")

# 2 attempts

newStudent = input("Enter a new student: ").capitalize()
newGrade = int(input("Enter their grade: "))

students.append([newStudent, newGrade]) # adds a whole new inner array and grade

# 1 attempt

changeStudent = input("Enter a student whose grade you want to change: ").capitalize()

found = False

for i in range(len(students)): # i will be the indexes that represent the sub lists
    if students[i][0] == changeStudent: # identical principle as lines 22 to 25
        found = True
        students[i][1] = int(input("Enter their new grade: "))

# 4 attempts AI assistance on line 49

if found:
    print(f"{changeStudent}'s grade has been updated.") # if true print the student's name and message
else:
    print("Student not found.") # if not then print student not found

# 2 attempts

removeStudent = input("Enter a student to remove: ").capitalize()

found = False

for i in range(len(students)):
    if students[i][0] == removeStudent: # similar principle for the 3rd time if found then remove whole inputted row and break right after (due to no alternative branch (else))
        found = True
        students.pop(i)
        break # ends loop

# 3 attempts learnt what break does

if found:
    print(f"{removeStudent} has been removed.") # if true then inputted item displayed as removed
else:
    print("Student not found.") # otherwise not

print("Updated students:")

for student in students:
    print(f"{student[0]}: {student[1]}") # for every row in the whole 2D array print the index's name (column 0) and grade (column 1)

# 1 attempt

print("All values in the 2D list:")

for row in students: # row being temporary variable for each row in array
    for item in row: # for EACH CELL in the rows so like [x1, y2], [x3, y4] sort of ordering
        print(item) # prints one from column 0 then the one next to it (column 1) then goes down one and repeats this for all remaining items

# 1 attempt
