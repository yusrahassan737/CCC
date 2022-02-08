# Name: Yusra Hassan
# Date: August 12th, 2021
# Description: Find and correct Debra's data by rotating her table of sunflowers' heights which is ordered least to most tall and recent
# Purpose: CCC Practice (level 4)

# Get input
import sys
sideLen = int(sys.stdin.readline())
data = []
for i in range(sideLen):
    ln = sys.stdin.readline().split()
    data.append(list(map(int, ln)))

# Function to "rotate" a 3D list 90 degrees
def rotate(grid):
    newGrid = []
    for i in range(sideLen):
        newLn = []
        for j in range(sideLen):
            newLn.append(grid[sideLen- 1 - j][i])
        newGrid.append(newLn)
    return newGrid

# Function to check if conditions have passed
def check(grid):
    status = True
    vGrid = rotate(grid)
    for i in range(sideLen):
        if sorted(grid[i]) != grid[i] or sorted(vGrid[i], reverse = True) != vGrid[i]: # the vertical sideLenwill be backwards after a rotation
            #print(sorted(grid[i]), grid[i], sorted(vGrid[i], reverse = True), vGrid[i])
            status = False
            break
    return status

# Print data if it can follow the requirements when rotated a multiple of 90 degrees
for i in range(4):
    if not check(data):
        data = rotate(data)
    else:
        break
if check(data):
    for i in data:
        print(" ".join(list(map(str, i))))
