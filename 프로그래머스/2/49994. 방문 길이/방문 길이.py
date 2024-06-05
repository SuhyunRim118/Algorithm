def solution(dirs):
    answer = 0
    visit = []
    dir = {'U':[0, -1], 'D':[0, 1], 'R':[1, 0], 'L':[-1, 0]}
    
    x, y = 0, 0
    
    for d in dirs:
        nx, ny = x+dir[d][0], y+dir[d][1]
        
        if nx<-5 or nx>5 or ny<-5 or ny>5:
            continue
        
        if [x, y, nx, ny] not in visit:
            answer+=1
            visit.append([x, y, nx, ny])
            visit.append([nx, ny, x, y])
        
        x, y = nx, ny
        
    return answer