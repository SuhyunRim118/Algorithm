# gold 5
# A와 B 2

import sys
input = sys.stdin.readline
from collections import deque

def make_T(s, t):
    global answer

    q = deque([s])

    while q:
        s_next = q.popleft()

        if s_next==t:
            answer = 1
            break
        
        if s_next not in t and s_next[::-1] not in t:
            continue

        if len(s_next) >= len(t):
            continue
            
        # A 추가
        q.append(s_next+'A')

        # B 추가 후 뒤집기
        q.append((s_next+'B')[::-1])

S = input().rstrip()
T = input().rstrip()
answer = 0

make_T(S, T)

print(answer)