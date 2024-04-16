# silver 5
# 다리 놓기

import sys
input = sys.stdin.readline

T = int(input())
testcase = []

for t in range(T):
    testcase.append(list(map(int, input().split())))

N = [t[0] for t in testcase]
M = [t[1] for t in testcase]

max_n = max(N)
max_m = max(M)

dp = [[0]*(max_m+1) for _ in range(max_n+1)]

for n in range(max_n+1):
    for m in range(max_m+1):
        if n==m:
            dp[n][m] = 1
        elif n==1:
            dp[n][m] = m
        elif n<m:
            dp[n][m] = dp[n][m-1] + dp[n-1][m-1]

for t in range(T):
    print(dp[testcase[t][0]][testcase[t][1]])