#Aim : To be able to use append(), remove(), for loops, range(), len(), and make and use flag variables (Only True/False examples)
#Muhammed Omer Pirbudak (proof to LAET about work over the holidays) 

students = ["Ali", "Sarah", "John", "Emma", "David"]

print("Original students:")
print(students)

# So this here requests input from user and that value is stored within a variable. Said variable is used in xxx.append(thevariable)
newStudent = input("Enter a new student: ")
students.append(newStudent)

print("Updated students:")
print(students)

# Remove a student from the array 'students'
removeStudent = input("Enter a student to remove(do capitalise the first letter): ")

found = False  #this is a flag variable --- this is what gets checked to see if a conditon (in the further local scope) is met then action is taken accoridng to that

for student in students:  #student is temporary variable
    if student == removeStudent: #checks here if the removed student 
        found = True

if found == True: #this is a continuation of the previous code block
    students.remove(removeStudent) #if condition 
    print("Student removed.")
else:
    print("Student doesn't exist.")
# Display final list modified
print("Final students:")
print(students)
#Note: The remaining code was assisted by chatGPT while the previous ones were made by me HOWEVER the starter such as the variable and the mind map was given by me

# Display students with their indexes
print("Students with indexes:")

for i in range(len(students)): #'i' is temporary and length of array is the value stored into i e.g. 4 would mean indexes 0 to 3
    print(i, ":", students[i]) #prints each index value of i with its according item like i = 0 is first item and i = 1 is second item

#Summary:
#Task: Given by chatGPT
#Mindmap:given by chatGPT only after halfway mark where I was stuck
#Work: I have done about 75-80% of this by myself through trial and error can be questions on this. The rest is provided by chatGPT
