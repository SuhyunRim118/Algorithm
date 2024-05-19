# silver 1
# 동물원

import sys

N = int(sys.stdin.readline())
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 3

for n in range(2, N+1):
    dp[n] = (dp[n-1]*2 + dp[n-2])%9901

print(dp[N])

# 메모리 초과
# dp = [[0]*3 for _ in range(N)]

# for n in range(N):
#     for i in range(3):
#         if n==0:
#             dp[n][i] = 1
#         else:
#             if i==0:
#                 dp[n][i] = dp[n-1][1] + dp[n-1][2]
#             elif i==1:
#                 dp[n][i] = dp[n-1][0] + dp[n-1][2]
#             elif i==2:
#                 dp[n][i] = dp[n-1][0] + dp[n-1][1] + dp[n-1][2]

# print(sum(dp[N-1])%9901)