from collections import deque
import math

def solution(progresses, speeds):
    days = deque()
    answer = []
    
    for i in range(len(progresses)):
        days.append(math.ceil((100-progresses[i])/speeds[i]))
    
    while days:
        cnt = 1
        day = days.popleft()
        
        while days:
            if day >= days[0]:
                days.popleft()
                cnt+=1
            else:
                answer.append(cnt)
                break
    answer.append(cnt)
    
    return answer