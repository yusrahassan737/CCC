# Name: Yusra Hassan
# Date: May 1, 2021
# Description: 
# Purpose: ECOO actual (level 1 question)

import sys

start = int(sys.stdin.readline().strip())
interval = int(sys.stdin.readline().strip())
sent = int(sys.stdin.readline().strip())
message = "Who knows..."
times = []
for i in range(100):
    time = start + (interval * i)
    if time > 100:
        break
    times.append(time)

for i in times[1:]:
    if i >= sent:
        message = i
        break
print(message)
