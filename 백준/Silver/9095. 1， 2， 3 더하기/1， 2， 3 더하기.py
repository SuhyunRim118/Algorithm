# silver 3
# 1, 2, 3 더하기

import sys
input = sys.stdin.readline

def rec(n):
    if n==1:
        dp[n] = 1

    elif n==2:
        dp[n] = 2
    elif n==3:
        dp[n] = 4
    else:
        dp[n] = rec(n-1)+rec(n-2)+rec(n-3)
        
    return dp[n]

T = int(input())

for t in range(T):
    n = int(input())
    dp = [0]*(n+1)

    rec(n)

    print(dp[n])