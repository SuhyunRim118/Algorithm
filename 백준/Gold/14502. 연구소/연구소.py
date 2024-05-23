# gold 4
# 연구소

import sys
input = sys.stdin.readline
from collections import deque
import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 벽 만들기
# 백트래킹
def wall(cnt):
    if cnt==3:
        virus()
        return

    for y in range(N):
        for x in range(M):
            if board[y][x]==0:
                board[y][x] = 1
                wall(cnt+1)
                board[y][x] = 0

# 바이러스 퍼뜨리기
def virus():
    global safe
    q = copy.deepcopy(v_q)
    visit = copy.deepcopy(board)

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<M and 0<=ny<N and visit[ny][nx]==0:
                visit[ny][nx] = 2
                q.append([nx, ny])
    
    # 안전영역 확인
    cnt = 0
    for n in range(N):
        cnt += visit[n].count(0)
    
    safe = max(safe, cnt)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
v_q = deque()
safe = 0

for y in range(N):
    for x in range(M):
        if board[y][x]==2:
            v_q.append([x, y])

wall(0)
print(safe)