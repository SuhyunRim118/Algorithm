def solution(cards1, cards2, goal):
    answer = True
    idx1 = 0
    idx2 = 0
    idx = 0
    
    while True:
        if idx1<len(cards1) and cards1[idx1]==goal[idx]:
            idx1+=1
            idx+=1
        elif idx2<len(cards2) and cards2[idx2]==goal[idx]:
            idx2+=1
            idx+=1
        else:
            answer=False
            break
        
        if idx==len(goal):
            break
        
    return "Yes" if answer==True else "No"