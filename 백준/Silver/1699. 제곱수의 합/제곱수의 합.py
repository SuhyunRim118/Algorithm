# silver 2
# 제곱수의 합

import sys
N = int(sys.stdin.readline())
dp = [i for i in range(N+1)]
dp[1] = 1

for i in range(2, N+1):
    for j in range(1, i):
        if i < j**2:
            break
        # 제곱수를 기준으로 모든 경우의 수 체크
        if dp[i] > dp[i-j**2]+1:
            dp[i] = dp[i-j**2]+1

print(dp[N])