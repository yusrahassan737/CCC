# Name: Yusra Hassan
# Date: March 22, 2021
# Description: Find the diagonal coordinates of a frame to best fit a splatter painting based on splatter coordinates
# Purpose: CCC practice (level 3 question)

# Input for number of splatter drops
n = int(input())

# Input for splatter coordinates
splatterX = []
splatterY = []

for i in range(n):
    point = input()
    splatterX.append(int(point[:point.find(",")]))
    splatterY.append(int(point[point.find(",") + 1:]))

# Sorting and indexing to find and print the lowest-left and highest-right positions
splatterX.sort()
splatterY.sort()

print(str(splatterX[0] - 1) + "," + str(splatterY[0] - 1))
print(str(splatterX[len(splatterX) - 1] + 1) + "," + str(splatterY[len(splatterY) - 1] + 1))
