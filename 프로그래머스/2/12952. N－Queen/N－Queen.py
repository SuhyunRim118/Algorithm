def check(n, row, column, diagonal1, diagonal2):
    answer = 0
    
    if row==n: # Queen N개가 채워졌을 때
        answer+=1
    else:
        for i in range(n): # 행
            if column[i] or diagonal1[i+row] or diagonal2[i-row+n]: # 열, 대각선 확인
                continue
                
            column[i] = diagonal1[i+row] = diagonal2[i-row+n] = True
            answer+=check(n, row+1, column, diagonal1, diagonal2)
            
            column[i] = diagonal1[i+row] = diagonal2[i-row+n] = False # 다음 행 넘어가기 전 초기화
    
    return answer

def solution(n):
    answer = check(n, 0, [False]*n, [False]*(n*2), [False]*(n*2))
    
    return answer