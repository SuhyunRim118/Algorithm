# bronze 1
# 부녀회장이 될테야

import sys
input = sys.stdin.readline

T = int(input())
kn = []
max_k = 0
max_n = 0

for t in range(T):
    k = int(input())
    n = int(input())
    kn.append([k, n])
    
    if max_k < k:
        max_k = k
    if max_n < n:
        max_n = n

house = [[0]*(max_n+1) for _ in range(max_k+1)]

for i in range(max_k+1):
    for j in range(max_n+1):
        if i==0:
            house[i][j] = j
        else:
            house[i][j] = sum(house[i-1][:j+1])

for k, n in kn:
    print(house[k][n])