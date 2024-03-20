# silver 2
# 알고리즘 수업 - 너비 우선 탐색 1
# BFS

import sys
from collections import deque

def bfs(R):
    global order
    queue = deque([R])
    visited[R] = order

    while queue:
        node = queue.popleft()

        for i in line[node]:
            if visited[i]==0:
                queue.append(i)
                order+=1
                visited[i] = order


N, M, R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
visited = [0]*(N+1)
order = 1

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    line[u].append(v)
    line[v].append(u)

for i in range(1, N+1):
    line[i].sort()

bfs(R)
for i in range(1, N+1):
    print(visited[i])