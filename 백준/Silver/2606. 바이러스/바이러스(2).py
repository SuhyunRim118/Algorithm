# silver 3
# 바이러스
# DFS

import sys

def dfs(start):
    global count

    visited[start] = True
    count+=1

    for i in line[start]:
        if visited[i]==False:
            dfs(i)

input = sys.stdin.readline

n = int(input())
m = int(input())
line = [[] for _ in range(n+1)]
visited = [False]*(n+1)
count = 0

for i in range(m):
    a, b = map(int, input().split())

    line[a].append(b)
    line[b].append(a)

dfs(1)
print(count-1)
