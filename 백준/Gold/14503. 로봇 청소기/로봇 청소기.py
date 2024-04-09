# gold 5
# 로봇 청소기

import sys
input = sys.stdin.readline

# d 기준 반시계 90도 회전 시 방향 
turn_d = {0:3, 3:2, 2:1, 1:0}

back_d = {0:2, 1:3, 2:0, 3:1}

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c, d):
    global clean_cnt

    if room[r][c]==0: # 청소 되지 않은 현재 칸 청소
        room[r][c] = -1
        clean_cnt+=1
    
    for i in range(4):
        # 반시계 방향 90도 회전
        if i==0:
            nd = turn_d[d]
        else:
            nd = turn_d[nd]
        nr = r+dr[nd]
        nc = c+dc[nd]

        if 0<=nr<N and 0<=nc<M and room[nr][nc]==0: # 바라보는 방향 기준 앞쪽 칸이 청소 되지 않은 상태일 때
            dfs(nr, nc, nd) # 전진
            break
    else: # 주변 4칸 중 청소되지 않은 빈 칸이 없을 때
        nd = back_d[d]
        nr = r+dr[nd]
        nc = c+dc[nd]

        if 0<=nr<N and 0<=nc<M and room[nr][nc]!=1: # 바라보는 방향 기준 뒤쪽 칸으로 후진 가능하다면 후진
            dfs(nr, nc, d)
    
    return clean_cnt

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = []
clean_cnt = 0

for n in range(N):
    room.append(list(map(int, input().split())))

print(dfs(r, c, d))