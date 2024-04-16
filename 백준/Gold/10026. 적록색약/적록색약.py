# gold 5
# 적록색약

import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(y, x):
    q = deque()
    q.append((x, y))
    visit_rgb[y][x] = rgb

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and visit_rgb[ny][nx]==0 and pic[y][x]==pic[ny][nx]:
                visit_rgb[ny][nx] = visit_rgb[y][x]
                q.append((nx, ny))


def bfs_blind(y, x):
    q = deque()
    q.append((x, y))
    visit_rb[y][x] = rb

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and visit_rb[ny][nx]==0:
                if pic[y][x]==pic[ny][nx] or (pic[y][x]!='B' and pic[ny][nx]!='B'):
                    visit_rb[ny][nx] = visit_rb[y][x]
                    q.append((nx, ny))

N = int(input())
pic = []
visit_rgb = [[0]*(N) for _ in range(N)]
visit_rb = [[0]*(N) for _ in range(N)]
rgb = 0
rb = 0

for n in range(N):
    pic.append(list(input().rstrip()))

for i in range(N):
    for j in range(N):
        if visit_rgb[i][j]==0:
            rgb+=1
            bfs(i, j)

for i in range(N):
    for j in range(N):
        if visit_rb[i][j]==0:
            rb+=1
            bfs_blind(i, j)

print(rgb, rb)