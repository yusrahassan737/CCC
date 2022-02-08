# Name: Yusra Hassan
# Date: August 12th, 20217
# Description: Determine if a choose your own adventure book's pages are all reachable and find the shortest path to the end
# Purpose: CCC Practice (level 5)

#N = int(input())
#removed = []

#for i in range(N):
    #line = input()
    #indx = int(line[:line.find(" ")])
    #word = line[line.find(" ") + 1:]
    #removed.append(word[:indx - 1] + word[indx:])
    
#for i,j in enumerate(removed):
    #print(i + 1, j)

# problem
inp = input()
start = int(inp[:inp.find(" ")])
ttl = int(inp[inp.find(" ") + 1:])
lst = []
grid = []

# Filling calender with values
for i in range(start):
    lst.append("0")
for i in range(1, ttl + 1):
    lst.append(str(i))

# 
print("Sun Mon Tue Wed Thr Fri Sat")
for i in range(0, len(lst), 7):
    grid.append(lst[i - 7: i + 1])
for i in grid:
    print("   ".join(i))

