from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1
    
    weak_l = len(weak)
    for i in range(weak_l):
        weak.append(weak[i]+n)
    
    for i in range(weak_l):
        for friends in permutations(dist, len(dist)): # 친구들 순서 배치
            cnt = 1
            position = weak[i] + friends[cnt-1] # 시작지점에서부터 이동 후 지점
            
            for j in range(i, i+weak_l):
                if position < weak[j]: # 다음 weak 지점
                    cnt+=1
                    # 친구 수 초과인 경우
                    if cnt > len(dist):
                        break
                        
                    position = weak[j] + friends[cnt-1]
                    
            answer = min(answer, cnt)
    
    return answer if answer <= len(dist) else -1