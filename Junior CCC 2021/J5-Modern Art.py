# Name: Yusra Hassan
# Date: April 26th/27th, 2021 Edited Jan.26, 2022 for more efficiency
# Description: Find the number of gold cells in a painting where each stroke changes the cell's colour from gold to black or vice versa
# Purpose: CCC practice (level 5 question)

# Get rows, columns and number of choices
rows = int(input())
columns = int(input())
numChoices = int(input())

# Record choices
cWF = {}
for i in range(numChoices):
  ln = input()
  if ln in cWF:
    cWF[ln] += 1
  else:
    cWF[ln] = 1

# The canvas should start with all black (false) cells
canvas = []
goldCount = 0
for i in range(rows):
  line = []
  for j in range(columns):
    line.append(False)
  canvas.append(line)

# Switch the cells based on the choices
for i in cWF:
  current = int(i[i.find(" ") + 1:]) - 1
  if cWF[i] % 2 != 0:
    if i[0] == "R":
      for j in range(columns):
        cell = canvas[current][j]
        if not cell:
          canvas[current][j] = True
        else:
          canvas[current][j] = False
    else:
      for j in range(rows):
        cell = canvas[j][current]
        if not cell:
          canvas[j][current] = True
        else:
          canvas[j][current] = False

# Count how many gold cells there are and print the amount
for i in canvas:
  goldCount += sum(i)
print(goldCount)
