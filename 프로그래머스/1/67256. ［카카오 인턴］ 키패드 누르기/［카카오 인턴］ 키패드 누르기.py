def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7, -1]
    right = [3, 6, 9, -1]
    middle = [2, 5, 8, 0]
    left_thumb, right_thumb = -1, -1
    check_left = True
    
    for num in numbers:
        if num in left:
            check_left = True
        elif num in right:
            check_left = False
        else:
            idx = middle.index(num)
            
            if left_thumb in left:
                left_idx = left.index(left_thumb)
            else:
                left_idx = middle.index(left_thumb)
                
            if right_thumb in right:
                right_idx = right.index(right_thumb)
            else:
                right_idx = middle.index(right_thumb)

            left_distance = abs(left_idx-idx)
            right_distance = abs(right_idx-idx)
            
            if left_thumb in left:
                left_distance+=1
            if right_thumb in right:
                right_distance+=1
                        
            if left_distance < right_distance:
                check_left = True
            elif left_distance > right_distance:
                check_left = False
            else:
                if hand=='left':
                    check_left = True
                else:
                    check_left = False
                    
        if check_left==True:
            answer+='L'
            left_thumb = num
        else:
            answer+='R'
            right_thumb = num
    
    return answer