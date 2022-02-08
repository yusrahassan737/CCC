# Name: Yusra Hassan
# Date: April 26th, 2021
# Description: Finds lowest possible number of swaps to get Valntina's books in order from L to S
# Purpose: CCC practice (level 4 question)

# Variables
series = input()
switchCount = 0

# Creating a list of values where L = 3, M = 2 and S = 1 for easier sorting
values = series.replace("L", "3")
values = values.replace("M", "2")
values = values.replace("S", "1")
values = list(values)

# Bubble sort algorithm to sort through vvalues and count steps
for ref in range(len(values) - 1):
        for comparison in range(ref + 1, len(values)):
            if values[ref] < values[comparison]:
                values[ref], values[comparison] = values[comparison], values[ref]
                switchCount += 1

print(switchCount)
