# silver 3
# 피보나치 함수

import sys
input = sys.stdin.readline

testcase = []
fib = [0, 1, 1]

T = int(input())
for t in range(T):
    testcase.append(int(input()))

max_num = max(testcase)

if max_num >= 3:
    for i in range(3, max_num+1):
        fib.append(fib[i-1]+fib[i-2])\

for tc in testcase:
    if tc==0:
        print(1, 0)
    else:
        print(fib[tc-1], fib[tc])