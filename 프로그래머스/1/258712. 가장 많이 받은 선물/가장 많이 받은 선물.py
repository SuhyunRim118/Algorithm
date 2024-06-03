def solution(friends, gifts):
    answer = 0
    
    record = [[0]*len(friends) for _ in range(len(friends))]
    jisu = [0]*len(friends)
    
    for gift in gifts:
        g_from, g_to = gift.split()
        idx_f = friends.index(g_from)
        idx_t = friends.index(g_to)
        
        record[idx_f][idx_t] += 1
        jisu[idx_f]+=1
        jisu[idx_t]-=1
        
    for i in range(len(friends)):
        cnt = 0
        for j in range(len(friends)):
            if i==j:
                continue
            
            if record[i][j]>record[j][i]:
                cnt+=1
            elif record[i][j]==record[j][i]:
                if jisu[i]>jisu[j]:
                    cnt+=1
                    
        answer = max(answer, cnt)
                
    return answer