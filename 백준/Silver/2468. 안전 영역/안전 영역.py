# silver 1
# 안전 영역

import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, rain):
    q = deque()
    q.append((x, y))

    visit[y][x] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N and area[ny][nx]>rain and visit[ny][nx]==0:
                visit[ny][nx] = 1
                q.append((nx, ny))


N = int(input())
area = []

for n in range(N):
    area.append(list(map(int, input().split())))

max_num = max(map(max, area))
answer = 0

for i in range(max_num):
    visit = [[0]*(N) for _ in range(N)]
    cnt = 0

    for y in range(N):
        for x in range(N):
            if area[y][x]>i and visit[y][x]==0:
                bfs(x, y, i)
                cnt+=1
    
    if answer < cnt:
        answer = cnt

print(answer)