# 이분탐색기법
def solution(stones, k):
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left+right)//2
        cnt = 0
        
        for s in stones:
            if s-mid<=0: # 건널 수 없음
                cnt+=1
            else:
                cnt=0
                
            if cnt==k: #최대 
                break
            
        if cnt==k: #최대
            right = mid-1
        else:
            left = mid+1

    return right
