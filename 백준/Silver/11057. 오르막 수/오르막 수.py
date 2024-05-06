# silver 1
# 오르막 수

import sys

N = int(sys.stdin.readline())
dp = [[0]*(10) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(10):
        if i==1:
            dp[i][j] = 1
        else:
            dp[i][j] = sum(dp[i-1][j:])

print(sum(dp[N])%10007)