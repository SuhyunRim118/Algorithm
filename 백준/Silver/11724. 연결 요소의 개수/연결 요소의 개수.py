# silver 2
# 연결 요소의 개수

import sys
input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque([n])
    visit[n] = 1

    while q:
        n = q.popleft()

        for nn in graph[n]:
            if visit[nn]==0:
                q.append(nn)
                visit[nn] = 1

N, M = map(int, input().split())
graph = {}
visit = [0]*(N+1)
cnt = 0

for n in range(1, N+1):
    graph[n] = []

for m in range(M):
    u, v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)

for n in range(1, N+1):
    if visit[n]==0:
        bfs(n)
        cnt+=1

print(cnt)