# gold 5
# 숨바꼭질 3

import sys
input = sys.stdin.readline
from collections import deque

dx = [2, -1, 1]

def bfs(x):
    q = deque([x])
    visit[x] = 1

    while q:
        x = q.popleft()

        if x==K:
            break

        for i in range(3):
            if x==0 and i==0:
                continue
            
            if i==0:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            
            if 0<=nx<100001 and visit[nx]==0:
                # print(i, dx[i], x, nx)
                if i==0:
                    visit[nx] = visit[x]
                    q.append(nx)
                else:
                    visit[nx] = visit[x]+1
                    q.append(nx)
                # print(q)

N, K = map(int, input().split())
visit = [0]*(100001)

bfs(N)
print(visit[K]-1)