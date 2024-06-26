from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(maps):
    answer = 0
    w, h = len(maps[0]), len(maps)
    q = deque()
    visit = [[[False for _ in range(2)] for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if maps[i][j]=='S': # 시작 지점
                s_x, s_y = j, i
                visit[i][j][0] = True
                q.append((s_x, s_y, 0, 0))
            elif maps[i][j]=='E': # 출구
                e_x, e_y = j, i
                
    while q:
        x, y, k, time = q.popleft()
        
        if k==1 and x==e_x and y==e_y:
            return time
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            
            if 0<=nx<w and 0<=ny<h and maps[ny][nx]!='X':
                if visit[ny][nx][k]==False:
                    visit[ny][nx][k]=True

                    if maps[ny][nx]=='L':
                        q.append((nx,ny, 1, time+1))
                    else:
                        q.append((nx,ny, k, time+1))
    
    return -1