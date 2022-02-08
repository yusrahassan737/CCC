# Name: Yusra Hassan
# Date: May 1, 2021
# Description: 
# Purpose: ECOO actual (level 3 question)

import sys
N, M, K = sys.stdin.readline().strip().split()
N, M, K = int(N), int(M), int(K)
lst = []
for i in range(K):
    line = sys.stdin.readline().strip().split()
    for j in range(len(line)):
        line[j] = int(line[j])
    lst.append(line)

bestProfs = ""
for i in range(1, N + 1):
    scores = []
    numLst = []
    for j in range(len(lst)):
        if lst[j][1] == i:
            scores.append(lst[j][2])
            numLst.append(lst[j])

    if scores != []:
        scores.sort(reverse = True)
        for j in numLst:
            if scores[0] in j:
                bestProfs += str(j[0]) + " "
                break
    else:
        bestProfs += "-1 "
        
print(bestProfs[:-1])


#numQuestions, numTeachers, numEmails = map(int, input().split())
#maxArr = [-1] * (numQuestions + 1)
#teacher = {}
#teacher[-1] = "-1"
#for _ in range(numEmails):
    #professor, question, score = map(int, input().split())
    #if maxArr[question] < score:
        #maxArr[question] = score   
        #teacher[question] = professor

#s = ""
##print(maxArr)ans = []
#for i in range(1, len(maxArr)):
    #if maxArr[i] == -1:
        #ans.append(str(-1))
    #else:
        #ans.append(str(teacher[i]))

#print(' '.join(ans), flush=True)
