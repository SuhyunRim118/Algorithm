# silver 3
# DFS와 BFS

import sys
from collections import deque
input = sys.stdin.readline

def dfs(start):
    visited_dfs[start] = 1
    print(start, end=' ')

    for i in line[start]:
        if visited_dfs[i]==0:
            dfs(i)

def bfs(start):
    queue = deque([start])

    visited_bfs[start] = 1
    print(start, end=' ')

    while queue:
        node = queue.popleft()

        for i in line[node]:
            if visited_bfs[i]==0:
                queue.append(i)
                visited_bfs[i] = 1
                print(i, end=' ')

n, m, v = map(int, input().split())
line = [[] for _ in range(n+1)]
visited_dfs = [0]*(n+1)
visited_bfs = [0]*(n+1)

for i in range(m):
    a, b = map(int, input().split())

    line[a].append(b)
    line[b].append(a)

for i in range(1, n+1):
    line[i].sort()

dfs(v)
print()
bfs(v)