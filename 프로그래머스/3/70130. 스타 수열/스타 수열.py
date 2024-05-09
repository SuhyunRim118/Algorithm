from collections import Counter

def solution(a):
    answer = -1
    
    a_cnt = Counter(a)
    
    for num in a_cnt.keys():
        
        if a_cnt[num] <= answer:
            continue
        
        cnt = 0
        idx = 0
        
        while idx < len(a)-1:
            
            if (a[idx]!=num and a[idx+1]!=num) or (a[idx]==a[idx+1]):
                idx+=1
                continue
            
            idx+=2
            cnt+=1
        
        answer = max(answer, cnt)
    
    return 0 if answer==-1 else answer*2