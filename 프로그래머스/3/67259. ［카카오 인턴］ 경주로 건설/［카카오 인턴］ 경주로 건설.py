def solution(board):
    answer = float('inf')
    N = len(board)
    record = [(0, 0, -1, 0)] # y, x, direction, cost
    isVisit = [[[-1 for _ in range(4)] for _ in range(N)] for _ in range(N)]
    
    while record:
        y, x, direction, cost = record.pop(0)
        
        # 이웃 탐색
        neighbors = [(y, x-1), (y, x+1), (y-1, x), (y+1, x)]
        for direct, (ny, nx) in enumerate(neighbors):
            
            # boundary 벗어난 경우거나 벽(1)인 경우
            if ny<0 or ny>=N or nx<0 or nx>=N or board[ny][nx]: 
                continue
            
            #cost 계산: 직진-100, 코너-500
            calcCost = cost + (100 if direction==-1 or direct==direction else 600)
            
            # 도착점에 도달했고, 
            # 도착점의 cost가 -1(처음 온 상태)이거나 이전에 기록된 cost보다 낮을 때
            # (재)기록
            if (y, x)==(N-1, N-1):
                answer = min(answer, cost)
            #처음 시작이거나 이전에 기록된 cost보다 낮은 cost일 경우
            elif isVisit[ny][nx][direct]==-1 or calcCost < isVisit[ny][nx][direct]:
                isVisit[ny][nx][direct] = calcCost # cost 기록
                record.append((ny, nx, direct, calcCost)) # 길 추가
    
    return answer