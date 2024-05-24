# gold 4
# 인구 이동

import sys
input = sys.stdin.readline
from collections import deque

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def move(x, y):
    q = deque()
    q.append([x, y])
    unite = [[x, y]]
    ppl_n = 0

    while q:
        x, y = q.popleft()
        visit[y][x] = 1

        for i in range(4):
            nx, ny = x+d[i][0], y+d[i][1]

            if 0<=nx<N and 0<=ny<N and visit[ny][nx]==0:
                if L<=abs(land[y][x]-land[ny][nx])<=R:
                    visit[ny][nx] = 1
                    q.append([nx, ny])
                    unite.append([nx, ny])
    
    if len(unite)<=1:
        return 0
    ppl_n = sum(land[y][x] for x, y in unite)//len(unite)

    for x, y in unite:
        land[y][x] = ppl_n

    return 1

N, L, R = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(N)]

day = 0
while True:
    cnt = 0
    visit = [[0]*N for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if visit[y][x]==0:
                cnt += move(x, y)

    if cnt==0:
        break
    else:
        day+=1

print(day)