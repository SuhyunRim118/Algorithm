# silver 1
# 겹치는 건 싫어

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

counter = [0]*(max(nums)+1)
start, end = 0, 0
longest = 0

while end<N:  
    if counter[nums[end]] < K:
        counter[nums[end]]+=1
        end+=1
    else:
        counter[nums[start]]-=1
        start+=1

    longest = max(longest, end-start)

print(longest)