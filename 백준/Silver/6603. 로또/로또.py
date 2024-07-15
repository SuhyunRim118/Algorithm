# silver 2
# 로또

import sys
input = sys.stdin.readline
from itertools import combinations

testcase = list(map(int, input().split()))

while testcase[0] != 0:
    k = testcase[0]
    S = testcase[1:]

    comb = list(combinations(S, 6))
    
    for c in comb:
        print(*c)
    print()
    testcase = list(map(int, input().split()))