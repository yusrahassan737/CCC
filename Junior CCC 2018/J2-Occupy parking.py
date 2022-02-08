# Name: Yusra Hassan
# Date: August 12th, 2021
# Description: Count the number of parking spaces which were occupied both yesterday and today
# Purpose: CCC Practice (level 2)

# Get input
import sys
numSpaces = int(sys.stdin.readline())
yesterday = sys.stdin.readline().strip()
today = sys.stdin.readline().strip()
bothDays = 0

# Count same spaces and print num
for i in range(numSpaces):
    if yesterday[i] == "C" and yesterday[i] == today[i]:
        bothDays += 1
print(bothDays)
