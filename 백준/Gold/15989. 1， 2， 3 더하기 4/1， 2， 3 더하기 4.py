# gold 5
# 1, 2, 3 더하기 4

import sys
input = sys.stdin.readline

T = int(input())
testcases = [int(input()) for _ in range(T)]
largest = max(testcases)
dp = [[0]*3 for _ in range(largest)]
dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[2][2] = 1

for i in range(3, largest):
    dp[i][0] = dp[i-1][0]
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]

for t in testcases:
    print(sum(dp[t-1]))