# gold 4
# 테트로미노

import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# ㅜ, ㅗ, ㅏ, ㅓ
ux = [[0, 1, 2, 1], [0, 1, 2, 1], [0, 0, 0, 1], [0, 1, 1, 1]]
uy = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 1, 2, 1], [0, -1, 0, 1]]

def check_shape(x, y, sum, cnt):
    global result
    
    if cnt==4:
        result = max(result, sum)
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<M and 0<=ny<N and visit[ny][nx]==0:
            visit[ny][nx] = 1
            check_shape(nx, ny, sum+paper[ny][nx], cnt+1)
            visit[ny][nx] = 0

def check_ushape(x, y):
    global result

    for i in range(4):
        add = 0
        cnt = 0
        for j in range(4):
            nx, ny = x+ux[i][j], y+uy[i][j]

            if 0>nx or nx>=M or 0>ny or ny>=N:
                break
            
            cnt+=1
            add+=paper[ny][nx]
        
        if cnt==4:
            result = max(result, add)

input = sys.stdin.readline
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
result = 0

for y in range(N):
    for x in range(M):
        visit[y][x] = 1
        check_shape(x, y, paper[y][x], 1)
        visit[y][x] = 0

        check_ushape(x, y)

print(result)