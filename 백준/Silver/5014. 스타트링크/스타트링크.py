# silver 1
# 스타트링크

import sys
from collections import deque

def bfs(floor):
    q = deque([floor])
    visit[floor] = 1

    while q:
        now = q.popleft()

        if now==G:
            break

        for move in [U, D*-1]:
            next = now+move

            if 0<next<=F and visit[next]==0:
                visit[next] = visit[now] + 1
                q.append(next)

F, S, G, U, D = map(int, sys.stdin.readline().split())
visit = [0]*(F+1)

bfs(S)

if visit[G]==0:
    print("use the stairs")
else:
    print(visit[G]-1)