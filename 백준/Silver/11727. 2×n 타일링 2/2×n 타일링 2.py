# silver 3
# 2xn 타일링 2

import sys

n = int(sys.stdin.readline())
dp = [0]*(n+1)
dp[1] = 1

if n>=2:
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = 2*dp[i-2] + dp[i-1]

print(dp[n]%10007)