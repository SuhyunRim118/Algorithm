# silver 3
# 1로 만들기

import sys
sys.setrecursionlimit(15000)
n = int(sys.stdin.readline())
dp = [0]*(n+1)

# Bottom to Top
# for i in range(2, n+1):
#     dp[i] = dp[i-1]+1

#     if i%2==0:
#         dp[i] = min(dp[i], dp[i//2]+1)
#     if i%3==0:
#         dp[i] = min(dp[i], dp[i//3]+1)

# Top to Bottom
def rec(n):
    if n==1 or dp[n]!=0:
        return dp[n]

    if (n%3==0) and (n%2==0):
        dp[n] = min(rec(n//3)+1, rec(n//2)+1)
    elif n%3==0:
        dp[n] = min(rec(n//3)+1, rec(n-1)+1)
    elif n%2==0:
        dp[n] = min(rec(n//2)+1, rec(n-1)+1)
    else:
        dp[n] = rec(n-1)+1
    
    return dp[n]

rec(n)

print(dp[n])