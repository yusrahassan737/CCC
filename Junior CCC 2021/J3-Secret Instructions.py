# Name: Yusra Hassan
# Date: April 15th, 2021
# Description: Decode a set of instructions based on the sum of the first two digits of each line (except the last)
# Purpose: CCC practice (level 3 question)

# Get instructions
instructions = []
while True:
    line = input()
    if line == "99999": # stop taking input after this line
        break
    instructions.append(line)

# find direction and steps from each line and print
for i in instructions:
    sumOfTwo = int(i[0]) + int(i[1])
    if sumOfTwo == 0:
        pass
    elif sumOfTwo % 2 == 0:
        direction = "right"
    else:
        direction = "left"
    print(direction, i[2:])
