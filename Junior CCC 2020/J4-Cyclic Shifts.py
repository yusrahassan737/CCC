# Name: Yusra Hassan
# Date: April 4th, 2021
# Description: found if a given input contains a cyclic shift of a sequence
# Purpose: CCC Practice (level 4)

# input
T = input()
S = input()
   
# other variables
shifts = []
found = "no"

# create a list of cyclic shifts of S
for i in S:
    S = S[1:] + S[0]
    shifts.append(S)

# check if an item of the list of cyclic shifts is in T and change state if so, then print state
for i in shifts:
    if i in T:
        found = "yes"
        break
print(found)
