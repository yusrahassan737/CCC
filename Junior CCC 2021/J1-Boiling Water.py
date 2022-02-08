# Name: Yusra Hassan
# Date: April 15th, 2021
# Description: Find atmospheric pressure and level based on boiling point
# Purpose: CCC practice (level 1 question)

# Variables
boilingPoint = int(input())
pressure = 5 * boilingPoint - 400

# Output
print(pressure)
if pressure == 100:
    print(0)
elif pressure > 100:
    print(-1)
else:
    print(1)
