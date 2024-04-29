# silver 2
# 상자넣기

import sys
input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if boxes[i]>boxes[j]:
            if dp[i]!=1:
                dp[i] = max(dp[i], dp[j]+1)
            else:
                dp[i] = dp[j]+1

print(max(dp))