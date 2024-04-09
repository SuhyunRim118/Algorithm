# silver 2
# 1, 2, 3 더하기 5

import sys
input = sys.stdin.readline

T = int(input())
testcase = []

for t in range(T):
    testcase.append(int(input()))

max_num = max(testcase)

dp = [[0]*3 for _ in range(100000)]

dp[0] = [1, 0, 0]
dp[1] = [0, 1, 0]
dp[2] = [1, 1, 1]

for i in range(3, max_num):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2])%1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2])%1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1])%1000000009

for tc in testcase:
    print(sum(dp[tc-1])%1000000009)