#String analyser.py - Muhammed Omer Pirbudak (proof to LAET about work over the holidays) 
#Underneath each part / block of code I will list attempts and if any were helped from chat GPT (or things I remembered on last attempt that weren't GPT assisted)
printSample = input("Enter a sentence: ")

print(printSample.upper()) #user input in capitals

print(printSample.lower()) #user input in all lowercase

print(f"Number of characters: {len(printSample)}") #takes the length of user given input and give its length 
#1 attempt here

searchWordSentence = input("Enter a word to search for: ")

pos = printSample.find(searchWordSentence) #looks for (second) inputted string and searches to see if it's in the initial (first) input

if pos != -1:   #the fact find returns -1 on fail was given by chatgpt which  I have implemented  
    print(f"{searchWordSentence} starts at index {pos}.")
else:
    print(f"{searchWordSentence} was not found.")

#3 attempts here no chatGPT correction but I remembered what it said about find returning -1 on fail 

#I now understand that find returns the lowest index (first letter entered) of the substring inputted and returns -1 if nothing found we can use that in the if statement to set a specific condition

#part2:
words = printSample.split()

print(f"Words: {words}")                 #lines 22-25 new variable to store the input and split with spaces, print the stored value with differentiating the whitespace like word = "Hello world" would give ["Hello", "world"]
print(f"Number of words: {len(words)}")  # "Hello world" would return "Number of words: 2"

sentenceStarterCheck = input("What should the sentence start with? ")
#1 attempt

if printSample.startswith(sentenceStarterCheck):   #what does the sentence start with? if it does like printSample is "Hello world" and sSCheck value is He or Hello it will output line 30
    print("The sentence starts with that sequence.")   
    #3 attempts 33-34
else:                                                 #otherwise if sSCheck is for example Hola then it won't work
    print("The sentence does not start with that sequence.")


sentenceEndCheck = input("What should the sentence end with? ")
#1 attempt
if printSample.endswith(sentenceEndCheck):           #similar in principle to startswith but this time it is last index to front of new input compared with the last index back to front of the original reference (that being printSample)
    print("The sentence ends with that sequence.")
else:
    print("The sentence does not end with that sequence.")
#over 3 attempts chatGPT assisted with doing tihs whole segment

replaceOld = input("Enter text to replace: ")  
replaceNew = input("Enter replacement text: ")

modifiedSentence = printSample.replace(replaceOld, replaceNew)

print(f"Modified sentence: {modifiedSentence}")
#lines 49-54 took long over 3 attempts majorly assisted by chatGPT
