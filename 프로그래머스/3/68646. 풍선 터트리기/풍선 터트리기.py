def solution(a):
    answer = 2
    
    left = [a[0]]
    right = [a[-1]]
    
    for i in range(1, len(a)):
        if a[i]<left[i-1]:
            left.append(a[i])
        else:
            left.append(left[i-1])
        
        if a[len(a)-i-1]<right[i-1]:
            right.append(a[len(a)-i-1])
        else:
            right.append(right[i-1])
            
    right.reverse()

    for i in range(1, len(a)-1):
        if a[i]<left[i-1] or a[i]<right[i+1]:
            answer+=1
        
    return answer