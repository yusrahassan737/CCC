# Name: Yusra Hassan
# Date: April 15th, 2021
# Description: Find the winner of a silent auction based on an ordered list of participants with their bids
# Purpose: CCC practice (level 2 question)

# Variables
info = []
allBids = []
numBids = int(input())

# Go through the bids and names, append to lists and sort the only-bids one from (greatest to least)
for i in range(numBids):
    name = input()
    bid = int(input())
    info.append((name, bid))
    allBids.append(bid)
allBids.sort(reverse = True)

# Print the name of the person who placed the highest bid (break right after so others who bidded the same are ignored)
for i in info:
    if allBids[0] in i:
        print(i[0])
        break
