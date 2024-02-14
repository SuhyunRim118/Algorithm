# Test Case 25 failed

def solution(board):
    N = len(board)
    record = [(0, 0, -1, 0)] # y, x, direction, cost
    isVisit = [[-1 for _ in range(N)] for _ in range(N)]
    
    answer = -1
    
    while record:
        y, x, direction, cost = record.pop(0)
        
        # 도착점에 도달했고, 
        # 도착점의 cost가 -1(처음 온 상태)이거나 이전에 기록된 cost보다 낮을 때
        # (재)기록
        if (y, x)==(N-1, N-1) and (answer==-1 or answer>cost):
            answer = cost
        
        # 이웃 탐색
        neighbors = [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]
        for dir, (ny, nx) in enumerate(neighbors):
            
            # boundary 벗어난 경우거나 벽인 경우
            if ny<0 or ny>=N or nx<0 or nx>=N or board[ny][nx]: 
                continue
            
            #cost 계산: 직진-100, 코너-500
            calcCost = cost + (100 if direction==-1 or dir==direction else 600)
            
            #처음 시작이거나 이전에 기록된 cost보다 낮은 cost일 경우
            if isVisit[ny][nx]==-1 or calcCost <= isVisit[ny][nx]:
                isVisit[ny][nx] = calcCost # cost 기록
                record.append((ny, nx, dir, calcCost)) # 길 추가
            
    return answer
