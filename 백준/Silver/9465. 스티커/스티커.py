# silver 1
# 스티커

import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    n = int(input())
    sticker = []
    dp = [[0]*(n+1) for _ in range(2)]

    for i in range(2):
        sticker.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(2):
            if i==0:
                dp[j][i+1] = sticker[j][i]
            else:
                # 대각선
                diag = abs(j-1)
                dp[j][i+1] = max(dp[diag][i], dp[diag][i-1])+sticker[j][i]
    
    print(max(dp[0][n], dp[1][n]))