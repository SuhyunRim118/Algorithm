def solution(N, stages):
    fail = {}
    user_n = len(stages)
    
    for i in range(N):
        cnt = stages.count(i+1)
        
        if cnt==0:
            fail[i+1] = 0
        else:
            fail[i+1] = cnt/user_n
        
        user_n-=cnt
        
    answer = sorted(fail, key=lambda x:fail[x], reverse=True)
        
    return answer