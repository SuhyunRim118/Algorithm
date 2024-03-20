# silver 2
# 알고리즘 수업 - 깊이 우선 탐색 1
# DFS

import sys
sys.setrecursionlimit(150000)

def dfs(R):
    global order
    visited[R] = order

    line[R].sort()
    for i in line[R]:
        if visited[i]==False:
            order+=1
            dfs(i)


N, M, R = map(int, sys.stdin.readline().split())
line = [[]for _ in range(N+1)]
visited = [0]*(N+1)
order=1
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    line[u].append(v)
    line[v].append(u)

dfs(R)
for i in range(1, N+1):
    print(visited[i])