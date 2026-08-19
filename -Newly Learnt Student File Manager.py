#Student File Manager - Muhammed Omer Pirbudak - Applicaa code U-CU2XY

with open("students.txt", "w") as file: #learnt that as "file" makes "file" be the variable that represents the file
    file.write("Ali\n")  # \n prepares a new line (after the name here) for other student names
    file.write("Sarah\n")
    file.write("John\n")
    file.write("Emma\n")
    file.write("David\n")
#2 attempt

with open("students.txt", "r") as file: #read mode only views and stores similar to ROM but not exactly
    studentList = file.read()
#1 attempt

print("Students currently stored:")
print(studentList) #gives current list
#1 attempt

newStudent = input("Enter a new student: ").capitalize()
#1 attempt

with open("students.txt", "a") as file: #append mode allows to add the inputted value in newStudent to be added to the file
    file.write(newStudent + "\n") #adds the newStudent value via "write" and \n puts it to a new line 

#2 attempts
with open("students.txt", "r") as file: #open in read mode nothing to be altered for now
    studentList2 = file.read()  #newer updated list is read and the value is kept at this point in the program
#1 attempt

print("Updated students:")
print(studentList2) #prints updated list 
#1 attempt

with open("students.txt", "r") as file: # read the students.txt file
    studentLineView = file.readlines() #readlines contains the lines from the text file as individual CSV (comma separated values) example: "Ali\n" and so on


print(studentLineView) #studenLineView is now an array with separate strings prints for example: "X\n", "Y\n", "Z\n"


for i in range(len(studentLineView)): #i is a variable in the local scope equals to the length of the array so value of 5 is 5 indexes so from 0 to 4
    studentPrint = studentLineView[i].replace("\n", "") #this prints studentLineView without the excess "\n"
    print(f"{i + 1}: {studentPrint}") #prints the index with its belonging element and i + 1 makes sure they're listed in numerical order instead of say 0: Ali and 1: Sarah it is 1: Ali and 2: Sarah
