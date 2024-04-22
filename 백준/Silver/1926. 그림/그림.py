# silver 1
# 그림

import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    global cnt
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<m and 0<=ny<n and board[ny][nx]==1:
                board[ny][nx] = 0
                q.append((nx, ny))
                cnt+=1

n, m = map(int, input().split())
board = []
answer = [0]

for i in range(n):
    board.append(list(map(int, input().split())))

for y in range(n):
    for x in range(m):
        if board[y][x]==1:
            cnt = 1
            board[y][x] = 0
            bfs(x, y)
            answer.append(cnt)

print(len(answer)-1)
print(max(answer))