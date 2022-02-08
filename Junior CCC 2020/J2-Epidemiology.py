# Name: Yusra Hassan
# Date: March 22nd, 2021
# Description: Finds first day where infected people is greater than people entered using rNaught and day 0 infections
# Purpose: CCC practice (level 2 question)

# Input
p = int(input())
n = int(input())
r = int(input())

# Variables
totInfections = n
day = 0

# Loop to calculate infections and find number of days
while totInfections <= p:
    n *= r # the number of new infections is multiplied (by the r naught) with each day
    totInfections += n # add new infections to the number of total infections
    day += 1
print(day)
    
