from collections import deque

def solution(queue1, queue2):
    
    answer = 0
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    limit = len(q1)*3
    
    while sum1!=sum2:
        if sum1 > sum2:
            n = q1.popleft()
            q2.append(n)
            sum1-=n
            sum2+=n
        else:
            n = q2.popleft()
            q1.append(n)
            sum1+=n
            sum2-=n
        answer+=1
        
        if answer==limit:
            return -1
    
    return answer