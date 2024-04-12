# silver 2
# 촌수계산

import sys
input = sys.stdin.readline
from collections import deque

def bfs(first):
    q = deque([first])
    visit[first] = 0

    while q:
        person = q.popleft()
        
        for r in relation[person]:

            if visit[r]==-1:
                visit[r] = visit[person]+1
                q.append(r)

n = int(input())
first, second = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
visit = [-1]*(n+1)

for i in range(m):
    parent, child = map(int, input().split())

    relation[parent].append(child)
    relation[child].append(parent)

bfs(first)

if visit[second]==-1:
    print(-1)
else:
    print(visit[second])