# gold 4
# 뱀

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
turn = {}
visit = [[0]*(N+1) for _ in range(N+1)]

K = int(input())
for k in range(K): # 사과 위치
    ay, ax = map(int, input().split())
    visit[ay][ax] = 2

L = int(input())
for l in range(L): # 회전 시간, 방향
    X, C = map(str, input().split())
    turn[int(X)] = C

direction = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 오른, 아래, 왼, 위
turn_D = {0:1, 1:2, 2:3, 3:0}
turn_L = {0:3, 3:2, 2:1, 1:0}
head = 0 # 오른쪽

snake_q = deque()
snake_q.append([1, 1]) # 뱀 위치
sec = 0 # 시간

while True:
    x, y = snake_q[0]
    visit[y][x] = 1
    dx, dy = direction[head]
    nx, ny = x+dx, y+dy

    if 0<nx<=N and 0<ny<=N and visit[ny][nx]!=1:
        if visit[ny][nx]==0: # 사과가 없으면 꼬리 줄이기
            rx, ry = snake_q.pop()
            visit[ry][rx] = 0

        # 새로운 뱀의 머리 위치
        visit[ny][nx] = 1
        snake_q.appendleft([nx, ny])
    else:
        sec += 1
        break
    
    sec += 1

    # 방향 회전
    if sec in turn.keys():
        if turn[sec]=='D': # 시계 방향 90도
            head = turn_D[head]
        elif turn[sec]=='L': # 반시계 방향 90도
            head = turn_L[head]


    # if sec==10000:
    #     break
    
print(sec)