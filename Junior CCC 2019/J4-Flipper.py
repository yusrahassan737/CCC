# Name: Yusra Hassan
# Date: February 19th, 2021
# Description: Displays the orientation of a square of consecutive numbers based on a number of horizontal and vertical flips entered
# Purpose: Junior CCC practice (level 4 question)

# Variables
square = [1, 2, 3, 4]
flips = input()
   
# Keep track of the number of each type of flip
hFlips = flips.count("H")
vFlips = flips.count("V")

# Check flips
if hFlips % 2 != 0:
    square = [square[2], square[3], square[0], square[1]]
if vFlips % 2 != 0:
    square = [square[1], square[0], square[3], square[2]]

# Display new square orientation
for i in range(2):
    print(square[i * 2], square[(i * 2) + 1])
