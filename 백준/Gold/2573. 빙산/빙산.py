# gold 4
# 빙산

import sys
input = sys.stdin.readline
from collections import deque
import copy

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# 얼음 녹이기
def melt():
    ice_melt = [[0]*M for _ in range(N)]

    for r in range(1, N-1):
        for c in range(1, M-1):
            if ice[r][c] > 0:
                for i in range(4):
                    nr = r+dr[i]
                    nc = c+dc[i]

                    if ice[nr][nc]==0:
                        ice_melt[r][c]+=1
    
    for r in range(1, N-1):
        for c in range(1, M-1):
            if ice[r][c] > 0:
                if ice[r][c] <= ice_melt[r][c]:
                    ice[r][c] = 0
                else:
                    ice[r][c] -= ice_melt[r][c]

# 빙산 덩어리 개수 확인
def bfs(r, c):
    q = deque()
    q.append((r, c))
    visit[r][c] = 1

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]

            if 0<=nr<N and 0<=nc<M:

                if ice[nr][nc]!=0 and visit[nr][nc]==0:
                    q.append((nr, nc))
                    visit[nr][nc] = 1

# input
N, M = map(int, input().split())
ice = []
for n in range(N):
    ice.append(list(map(int, input().split())))

ice_cnt = 0
year = 0

while True:
    ice_cnt = 0
    visit = [[0]*M for _ in range(N)]
    year+=1

    melt()

    for n in range(1, N-1):
        for m in range(1, M-1):
            if ice[n][m]>0 and visit[n][m]==0:
                bfs(n, m)
                ice_cnt+=1

    if ice_cnt > 1: # 빙산 덩어리가 2개 이상일 때
        break
    elif ice_cnt==0: # 빙산이 다 녹았을 때
        year = 0
        break

print(year)