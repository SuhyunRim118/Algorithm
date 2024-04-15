# silver 4
# 설탕 배달

import sys

N = int(sys.stdin.readline())
dp = [-1]*(N+1)

for i in range(3, N+1):
    if i==4:
        continue

    if i%5==0:
        dp[i] = i//5
    elif dp[i-5]!=-1:
        dp[i] = 1 + dp[i-5]
    elif i%3==0:
        dp[i] = i//3
    else:
        dp[i] = -1
    
print(dp[N])