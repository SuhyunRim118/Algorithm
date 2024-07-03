from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(maps):
    w, h = len(maps[0]), len(maps)
    q = deque([])
    q.append([0, 0])
    visit = [[0]*w for _ in range(h)]
    visit[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0<=nx<w and 0<=ny<h:
                if maps[ny][nx]==1 and visit[ny][nx]==0:
                    visit[ny][nx] = visit[y][x]+1
                    q.append([nx, ny])
                    
    return visit[-1][-1] if visit[-1][-1]!=0 else -1