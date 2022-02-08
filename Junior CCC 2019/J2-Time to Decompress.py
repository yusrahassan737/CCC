# Name: Yusra Hassan
# Date: Nov.10, 2020
# Description: Decode messages from a friend where the first line is the number of lines in the message and the following contain an integer of how many of the letter that proceeds
# Purpose: Junior CCC practice (level 2 question)

# Variables
numLines = int(input()) # first line
message = [] # empty list to hold final message

# Loop to analyze each line after the first
for i in range(numLines):
    # Variables
    line = input() # get input of the line
    times = int(line[:line.find(" ")]) # get the number from the input
    char = line[line.find(" ") + 1:] # get the character(s) from the input
    
    message.append(times * char) # the message = the character(s) repeated (number from line input) times for each line

# Print final message
for i in message:
    print(i)
