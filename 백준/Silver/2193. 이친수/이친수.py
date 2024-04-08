# silver 3
# 이친수

import sys

N = int(sys.stdin.readline())

pinary = [0, 1, 1, 2, 3]

if N <= 4:
    print(pinary[N])
else:
    for i in range(5, N+1):
        ans = pinary[i-1] + pinary[i-2]
        
        pinary.append(ans)

    print(pinary[N])