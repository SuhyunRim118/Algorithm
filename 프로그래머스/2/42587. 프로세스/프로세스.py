from collections import deque

def solution(priorities, location):
    answer = 0
    n = len(priorities)
    p_q = deque(priorities)
    i_q = deque(i for i in range(n))
    cnt = 0
    
    while p_q:
        num = p_q.popleft()
        idx = i_q.popleft()
        
        for p in p_q:
            if num<p:
                p_q.append(num)
                i_q.append(idx)
                break
        else:
            cnt+=1
            if idx==location:
                return cnt
    
    return answer