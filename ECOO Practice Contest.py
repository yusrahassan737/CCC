# Name: Yusra Hassan
# Date: April 17th, 2021
# Description: 
# Purpose: ECOO 2021 practice contest (question )

N = int(input())
options = []
for i in range(N-1):
    A, B = input().split()
    options.append((int(A), int(B)))
hers = input().split()
hers[0], hers[1] = int(hers[0]), int(hers[1])
hers = tuple(hers)
place = options.index(hers)

def doIt(curMove):
    global options
    moves = []
    moreMoves = False
    
    for i in options:
        if curMove != i and (curMove[0] in i or curMove[1] in i):
            moves.append(i)
    
    if moves == []:
        return curMove
    print(moves)
    
    for i in moves:
        if doIt(i) == curMove:
            return curMove

print(doIt(hers))
