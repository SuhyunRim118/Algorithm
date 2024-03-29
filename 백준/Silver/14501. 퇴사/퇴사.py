# silver 3
# 퇴사

import sys
input = sys.stdin.readline

N = int(input())
T = [0]*(N+1)
P = [0]*(N+1)
dp = [0]*(N+1)

for n in range(N):
    t, p = map(int, input().split())
    T[n] = t
    P[n] = p

for i in range(N, 0, -1):
    if i+T[i-1] > N+1:
        dp[i-1] = dp[i]
    else:
        dp[i-1] = max(dp[i], P[i-1]+dp[i-1+T[i-1]])

print(dp[0])