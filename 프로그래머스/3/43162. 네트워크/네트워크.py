from collections import deque

def bfs(start, computers, visit, n):
    q = deque([start])
    
    while q:
        x, y = q.popleft()
        
        for i in range(n): # 연결되어 있는 컴퓨터
            if computers[x][i]==1 and i not in visit:
                visit.add(i)
                q.append([i, x])
    
def solution(n, computers):
    answer = 0
    visit = set()
    cnt = 0
    
    for y in range(n):
        for x in range(n):
            if x==y:
                continue
            if computers[y][x]==1 and x not in visit: # 다른 컴퓨터와 연결되어 있는
                visit.add(x)
                cnt+=1
                bfs([x, y], computers, visit, n)
    
    # # 연결되어 있지 않은 컴퓨터
    left = n-len(visit)

    return cnt+left