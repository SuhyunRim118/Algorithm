# silver 1
# 미로 탐색

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    step[y][x] = 1

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            count = step[y][x]
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if board[ny][nx]==1:
                
                if step[ny][nx]==0 or step[ny][nx]>count+1:
                    count+=1
                    step[ny][nx] = count
                    queue.append((ny, nx))


n, m = map(int, input().split())
board = []
step = [[0]*m for _ in range(n)]
for i in range(n):
    each = list(map(int, input().rstrip()))
    board.append(each)

bfs(0, 0)
print(step[n-1][m-1])