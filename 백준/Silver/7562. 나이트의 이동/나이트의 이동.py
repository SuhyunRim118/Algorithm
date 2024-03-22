# silver 1
# 나이트의 이동

import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs():
    
    queue = deque()
    queue.append((begin_x, begin_y))

    while queue:
        x, y = queue.popleft()

        if x==dest_x and y==dest_y:
            break

        for i in range(8):
            count = board[y][x]

            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=l or ny<0 or ny>=l or (nx==begin_x and ny==begin_y):
                continue
            if board[ny][nx]==0 or board[ny][nx]>count+1:
                board[ny][nx]=count+1
                queue.append((nx, ny))

testcase = int(input())

for t in range(testcase):
    l = int(input())
    begin_x, begin_y = map(int, input().split())
    dest_x, dest_y = map(int, input().split())

    board = [[0]*l for _ in range(l)]

    bfs()
    print(board[dest_y][dest_x])