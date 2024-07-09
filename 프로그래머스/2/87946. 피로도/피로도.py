from itertools import permutations
def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    dun = [i for i in range(n)]
    
    def check(order, tiredness):
        max_dun = 0
        
        for i in order:
            if tiredness < dungeons[i][0]:
                return max_dun
            else:
                max_dun+=1
                tiredness-=dungeons[i][1]
        
        return max_dun
    
    perm = list(permutations(dun, n))
    
    for p in perm:
        cnt = check(list(p), k)
        answer = max(answer, cnt)
        
    return answer