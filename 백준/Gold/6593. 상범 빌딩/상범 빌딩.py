# gold 5
# 상범 빌딩

import sys
input = sys.stdin.readline
from collections import deque

dl = [0, 0, 0, 0, -1, 1]
dr = [0, 0, -1, 1, 0, 0]
dc = [-1, 1, 0, 0, 0, 0]

def bfs(s_l, s_r, s_c):
    q = deque()
    q.append([s_l, s_r, s_c])

    visit[s_l][s_r][s_c] = 1

    while q:
        l, r, c = q.popleft()

        if l==e_l and r==e_r and c==e_c:
            break

        for i in range(6):
            nl, nr, nc = l+dl[i], r+dr[i], c+dc[i]

            if 0<=nl<L and 0<=nr<R and 0<=nc<C and visit[nl][nr][nc]==0:
                if building[nl][nr][nc]=='.' or building[nl][nr][nc]=='E':
                    visit[nl][nr][nc] = visit[l][r][c] + 1
                    q.append([nl, nr, nc])

L, R, C = map(int, input().split()) # 층(z), 행(y), 열(x)

while L!=0 and R!=0 and C!=0:
    building = []
    visit = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for l in range(L):
        floor = []

        for r in range(R):
            floor.append(input().rstrip())

            if 'S' in floor[r]:
                s_l, s_r = l, r
                s_c = floor[r].find('S')
            elif 'E' in floor[r]:
                e_l, e_r = l, r
                e_c = floor[r].find('E')
        
        building.append(floor)
        input()

    bfs(s_l, s_r, s_c)

    if visit[e_l][e_r][e_c] != 0:
        print('Escaped in', visit[e_l][e_r][e_c]-1, 'minute(s).')
    else:
        print('Trapped!')

    L, R, C = map(int, input().split())