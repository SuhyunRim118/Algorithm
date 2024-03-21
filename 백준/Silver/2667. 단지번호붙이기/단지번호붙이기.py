# silver 1
# 단지번호붙이기

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    count = 1
    queue = deque()
    queue.append([y, x])
    houses[y][x] = 0

    while queue:
        # print(queue)
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if houses[ny][nx]==1:
                houses[ny][nx] = 0
                queue.append([ny, nx])
                count+=1
    
    return count

n = int(input())
houses = []

for i in range(n):
    house = list(map(int, input().rstrip()))
    houses.append(house)

count = []
for i in range(n):
    for j in range(n):
        if houses[i][j]==1:
            count.append(bfs(i, j))

print(len(count))
print(*sorted(count), sep='\n')