# Name: Yusra Hassan
# Date: March 21/22, 2021
# Description: Determine if a dog is happy or sad based on the number and sizes of treats he had that day
# Purpose: CCC practice (level 1 question)

# Input
small = int(input())
med = int(input())
large = int(input())

# Variable to calculate treats to find dog's state
happiness = (small + med * 2 + large * 3) >= 10

# Print result
if happiness:
    print("happy")
else:
    print("sad")
