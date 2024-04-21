# silver 1
# 영역 구하기

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
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and paper[ny][nx]==0:
                cnt+=1
                paper[ny][nx] = 1
                q.append((nx, ny))

M, N, K = map(int, input().split())
paper = [[0]*N for _ in range(M)]
answer = []

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 1

for y in range(M):
    for x in range(N):
        if paper[y][x]==0:
            cnt = 1
            paper[y][x] = 1
            bfs(x, y)
            answer.append(cnt)

answer.sort()
print(len(answer))
print(*answer)