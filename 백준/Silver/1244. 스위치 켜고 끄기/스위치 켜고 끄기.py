# silver 4
# 스위치 켜고 끄기

import sys

input = sys.stdin.readline

switch_N = int(input())
switches = list(map(int, input().split()))
stu_N = int(input())

change = {0:1, 1:0}

for i in range(stu_N):
    gender, num = list(map(int, input().split()))
    
    if gender==1:
        for j in range(num, switch_N+1, num):
            switches[j-1] = change[switches[j-1]]
    else:
        switches[num-1] = change[switches[num-1]]
        
        move = min(num-1, switch_N-num)
        for j in range(1, move+1):
            if switches[num-1-j]==switches[num-1+j]:
                switches[num-1-j] = change[switches[num-1-j]]
                switches[num-1+j] = change[switches[num-1+j]]
            else:
                break
    
for i in range(1, switch_N+1):
    print(switches[i-1], end=' ')
    
    if i%20==0:
        print()