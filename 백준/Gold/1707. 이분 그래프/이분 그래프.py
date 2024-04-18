# gold 4
# 이분 그래프

import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque([v])
    visit[v] = 1
    
    while q:
        v = q.popleft()

        for neighbor in graph[v]:
            if visit[neighbor]==0:
                visit[neighbor] = visit[v]*-1
                q.append(neighbor)
            elif visit[neighbor]==visit[v]:
                return -1
    
    return 1


T = int(input())

for t in range(T):
    V, E = map(int, input().split())

    graph = {}
    visit = [0]*(V+1)

    for e in range(E):
        v1, v2 = map(int, input().split())

        if v1 in graph.keys():
            graph[v1].append(v2)
        else:
            graph[v1] = [v2]
        
        if v2 in graph.keys():
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]
    
    for v in graph.keys():
        if visit[v]==0:
            if bfs(v)==-1:
                print('NO')
                break
    else:
        print('YES')