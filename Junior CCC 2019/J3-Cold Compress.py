# Name: Yusra Hassan
# Date: Feb.18, 2020
# Description: Run-length encoding for a given input of characters - none being a space
# Purpose: Junior CCC practice (level 3 question)

# Variables
numLines = int(input())
message = []

# Loop iterating through each following line
for i in range(numLines):
    # Variables
    outputLine = ""
    currentLine = input()
    
    # Loop iterating through each character
    for j in range(len(currentLine)):
        
        # Check if it is the first iteration and set char and its times if so
        if j == 0:
            char = currentLine[j]
            charTimes = 0
            
        # Check if the latest character is differerent from the last
        elif currentLine[j] != char:
            outputLine += str(charTimes) + " " + char + " " # record last character with num
            char = currentLine[j]
            charTimes = 0
        charTimes += 1
        
        # If the character is the last one from the line, record it and its quantity immeditely
        if j == len(currentLine) - 1:
            outputLine += str(charTimes) + " " + char + " "
        
    # Add line to message after removing extra space
    outputLine = outputLine.strip()
    message.append(outputLine)

# Print out message
print()
for i in message:
    print(i)
    
