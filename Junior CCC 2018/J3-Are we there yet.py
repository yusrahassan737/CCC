# Name: Yusra Hassan
# Date: August 12th, 2021
# Description: Count the distances between 5 different cities and display in a table (0 values indicate that it is the city of that number)
# Purpose: CCC Practice (level 3)

# Variables and input
import sys
numCities = 5
allLines = []
distances = sys.stdin.readline().split()
distances = list(map(int, distances)) # cast input to int

# Determine distances for each cell in the table
for i in range(numCities):
    line = []
    for j in range(numCities):
        if i > j:
            line.append(sum(distances[j:i]))
        elif i < j:
            line.append(sum(distances[i:j]))
        else:
            line.append(0)
    allLines.append(line)

# Print as strings
for i in allLines:
    print(" ".join(list(map(str, i))))
