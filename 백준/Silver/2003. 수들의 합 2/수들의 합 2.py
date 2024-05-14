# silver 4
# 수들의 합2

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
cnt = 0
# sum = 0

while start<N and end<N:
    add = sum(nums[start:end+1])
    
    if add == M:
        cnt += 1

    if add >= M:
        start+=1
        end=start
    elif add < M:
        end += 1

print(cnt)