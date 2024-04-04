# gold 3
# 내리막 길

import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):

    if x==N-1 and y==M-1: # 목표지점
        return 1
    elif visited[y][x]!=-1: # 경우의 수 n
        return visited[y][x]
    else: # 방문하지 않은 곳
        visited[y][x] = 0
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or nx>=N or ny<0 or ny>=M or board[ny][nx]>=board[y][x]:
            continue
    
        visited[y][x] += dfs(nx, ny)
    
    return visited[y][x]


M, N = map(int, input().split())
board = []
visited = [[-1]*(N) for _ in range(M)]

for m in range(M):
    board.append(list(map(int, input().split())))

print(dfs(0, 0))