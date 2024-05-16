# gold 4
# 불

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def fire_bfs():

    while fire_q:
        x, y = fire_q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<W and 0<=ny<H and building[ny][nx]!='#' and fire_visit[ny][nx]==-1:
                fire_visit[ny][nx] = fire_visit[y][x] + 1
                fire_q.append([nx, ny])
    
def sang_bfs():
    
    while sang_q:
        x, y = sang_q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<W and 0<=ny<H:
                if building[ny][nx]=='.' and sang_visit[ny][nx]==-1:
                    if fire_visit[ny][nx]==-1 or sang_visit[y][x] + 1 < fire_visit[ny][nx]:
                        sang_visit[ny][nx] = sang_visit[y][x] + 1
                        sang_q.append([nx, ny])
            else:
                return sang_visit[y][x]+1
            
    return "IMPOSSIBLE"

T = int(input())
for t in range(T):
    W, H = map(int, input().split())
    building = []
    fire_visit = [[-1]*W for _ in range(H)]
    sang_visit = [[-1]*W for _ in range(H)]
    fire_q = deque()
    sang_q = deque()

    for h in range(H):
        building.append(input().rstrip())

        for w in range(W):
            if '@' == building[h][w]:
                sang_q.append([w, h])
                sang_visit[h][w] = 0
        
            if '*' == building[h][w]:
                fire_q.append([w, h])
                fire_visit[h][w] = 0

    fire_bfs()
    print(sang_bfs())