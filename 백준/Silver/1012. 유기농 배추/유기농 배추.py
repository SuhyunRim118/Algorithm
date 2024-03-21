# silver 2
# 유기농 배추

import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(farm, y, x):
    queue = deque()
    queue.append((y, x))
    farm[y][x] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if farm[ny][nx]==1:
                farm[ny][nx]=0
                queue.append((ny, nx))

    return True


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    farm = [[0]*m for _ in range(n)]
    count = 0

    for j in range(k):
        x, y = map(int, input().split())

        farm[y][x] = 1
    
    for y in range(n):
        for x in range(m):
            if farm[y][x]==1:
                if bfs(farm, y, x):
                    count+=1

    print(count)