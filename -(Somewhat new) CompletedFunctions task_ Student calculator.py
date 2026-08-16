#Function Student Calculator - Muhammed Omer Pirbudak (proof to LAET of work over the holidays) 


# this function returns two inputted parameters as total of each other 
def calculate_total(grade1, grade2):
    total = grade1 + grade2       
    return total                  #returns the sum back to the program 
#1 attempt

# function to calculate average 
def calculate_average(grade1, grade2):
    average = (grade1 + grade2) / 2   # Adds the grades and divide by 2 
    return average                    # returns the modified value of average back to the program
#1 attempt

# extra challenge
# function gets the two grades from user
def get_grade():
    firstGrade = int(input("Enter first grade: "))    
  # Gets first input and converts it to an integer
    secondGrade = int(input("Enter second grade: "))  
  # Gets second input and converts it to an integer

    return firstGrade, secondGrade  # Returns both values to the main program


# Calls get grade and stores its two returned values
firstGrade, secondGrade = get_grade()
#1 attempt

# Sends the two grades into calculate total
# The sum is given 
totalResult = calculate_total(firstGrade, secondGrade)
#3 attempt

# Sends the two arguments to calculate average and returns the final product
# The returned average is stored in averageResult
averageResult = calculate_average(firstGrade, secondGrade)
#2 attempts

# Displays the values returned by the functions
print(f"Total: {totalResult}")
print(f"Average: {averageResult}")
#1 attempt
