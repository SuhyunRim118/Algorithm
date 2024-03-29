# silver 3
# 계단 오르기

import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]*(N)
dp = [0]*(N)

for n in range(N):
    s = int(input())
    stairs[n] = s

dp[0] = stairs[0]

for i in range(1, N):
    if i==1:
        dp[i] = stairs[0]+stairs[1]
    elif i==2:
        dp[i] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    else:
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

print(dp[N-1])