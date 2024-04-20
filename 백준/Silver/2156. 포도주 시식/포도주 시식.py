# silver 1
# 포도주 시식

import sys
input = sys.stdin.readline

n = int(input())
drink = [int(input()) for _ in range(n)]
drink.insert(0, 0)
dp = [0]*(n+1)

dp[1] = drink[1]

for i in range(2, n+1):
    if i==2:
        dp[2] = drink[1] + drink[2]
    else:
        dp[i] = max(dp[i-1], max(dp[i-3] + drink[i-1] + drink[i], dp[i-2] + drink[i]))
    
print(max(dp))