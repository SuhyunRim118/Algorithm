# gold 4
# 문자열 폭발
# 스택

import sys
input = sys.stdin.readline

string = input().strip()
bomb = list(input().strip())
length = len(bomb)
stack = [] 

for s in string:
    stack.append(s)

    if stack[len(stack)-length:] == bomb:
        for _ in range(length):
            stack.pop()

if stack:
    print(*stack, sep='')
else:
    print('FRULA')