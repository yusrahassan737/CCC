# Name: Yusra Hassan
# Date: Nov.10, 2020
# Description: Takes in types of scores and numbers from two basketball teams and determines the winner
# Purpose: Junior CCC practice (level 1 question)

# Take in score types with number of each from both teams
aShots = int(input())
aFieldGoals = int(input())
aFreeThrows = int(input())
bShots = int(input())
bFieldGoals = int(input())
bFreeThrows = int(input())

# Calculate scores of both teams
aScore = (aShots * 3) + (aFieldGoals * 2) + aFreeThrows
bScore = (bShots * 3) + (bFieldGoals * 2) + bFreeThrows

# Print the winning team or tie
if aScore > bScore:
    print("A")
elif aScore < bScore:
    print("B")
else:
    print("T")
