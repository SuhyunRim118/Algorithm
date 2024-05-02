# gold 4
# 불!

import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs_fire():

    while q_f:
        r, c = q_f.popleft()

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if 0<=nr<R and 0<=nc<C and miro[nr][nc]!='#':
                if visit_f[nr][nc]==-1:
                    visit_f[nr][nc] = visit_f[r][c] + 1
                    q_f.append((nr, nc))

def bfs_jihun():

    while q_j:
        r, c = q_j.popleft()

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]

            if 0<=nr<R and 0<=nc<C:
                if miro[nr][nc]!='#' and visit_j[nr][nc]==-1:
                    if visit_f[nr][nc]==-1 or visit_j[r][c]+1 < visit_f[nr][nc]:
                        visit_j[nr][nc] = visit_j[r][c] + 1
                        q_j.append((nr, nc))
            else:
                return visit_j[r][c]+1

    return "IMPOSSIBLE"

R, C = map(int, input().split())
miro = []
visit_f = [[-1]*C for _ in range(R)]
visit_j = [[-1]*C for _ in range(R)]
q_f = deque()
q_j = deque()

for r in range(R):
    miro.append(input().rstrip())

    for c in range(C):
        if miro[r][c]=='J':
            q_j.append((r, c))
            visit_j[r][c] = 0
        if miro[r][c]=='F':
            q_f.append((r, c))
            visit_f[r][c] = 0

bfs_fire()
print(bfs_jihun())