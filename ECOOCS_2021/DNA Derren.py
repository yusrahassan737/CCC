# Name: Yusra Hassan
# Date: May 1, 2021
# Description: 
# Purpose: ECOO actual (level 2 question)

line = input()
newLine = ""
vowels = ["A"]
consonants = ["C", "T", "G"]

for i in range(len(line)):
    prev = ""
    if i != 0:
        prev = line[i - 1]
    cur = line[i]
    
    if (prev in vowels and cur in vowels) or (prev in consonants and cur in consonants):
        newLine += " " + cur
    else:
        newLine += cur

print(newLine)
