# gold 3
# 말이 되고픈 원숭이

import sys
from collections import deque
input = sys.stdin.readline

# next move
monkey = [[0, -1], [0, 1], [-1, 0], [1, 0]]
horse = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

def bfs():
    q = deque()
    q.append([0, 0, 0])
    visit[0][0][0] = 1

    while q:
        x, y, z = q.popleft()

        if x==W-1 and y==H-1:
            return visit[z][y][x]-1

        # 원숭이
        for mx, my in monkey:
            nx, ny = x+mx, y+my

            if 0<=nx<W and 0<=ny<H and road[ny][nx]==0:
                if visit[z][ny][nx]==0:
                    visit[z][ny][nx] = visit[z][y][x] + 1
                    q.append([nx, ny, z])

        # 말
        if z < K:
            for hx, hy in horse:
                nx, ny = x+hx, y+hy

                if 0<=nx<W and 0<=ny<H and road[ny][nx]==0:
                    if visit[z+1][ny][nx]==0:
                        visit[z+1][ny][nx] = visit[z][y][x] + 1
                        q.append([nx, ny, z+1])

    return -1

K = int(input())
W, H = map(int, input().split())
road = []
visit = [[[0]*(W) for _ in range(H)] for _ in range(K+1)]
for h in range(H):
    road.append(list(map(int, input().split())))

print(bfs())