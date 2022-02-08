# Name: Yusra Hassan
# Date: August 12th, 2021
# Description: Given the digits, find out if a phone number belongs to a telemarketer based off the patterns of its last 4 digits
# Purpose: CCC Practice (level 1)

# Get input
import sys
lines = []
for i in range(4):
    lines.append(int(sys.stdin.readline()))

# Print ignore if it follows the pattern and answer otherwise
if lines[0] > 7 and lines[3] > 7 and lines[1] == lines[2]: # can also do (_ == 8 or _ == 9) if input isn't strictly integers from 0-9
    print("ignore")
else:
    print("answer")
