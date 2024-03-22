# gold 5
# 토마토

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(queue):

    while(queue):
        y, x = queue.popleft()

        for i in range(4):
            count = boxes[y][x]

            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if boxes[ny][nx]==0:
                boxes[ny][nx]=count+1
                queue.append((ny, nx))
        


m, n = map(int, input().split())
boxes = []
queue = deque()

for i in range(n):
    box = list(map(int, input().split()))
    boxes.append(box)

for i in range(n):
    for j in range(m):
        if boxes[i][j]==1:
            queue.append((i, j))

bfs(queue)

days = 0
for i in range(n):
    for j in range(m):
        if boxes[i][j]==0:
            print(-1)
            exit()

    days = max(days, max(boxes[i]))

print(days-1)