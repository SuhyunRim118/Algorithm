from collections import Counter

def solution(want, number, discount):
    answer = 0
    total_want = sum(number)
    want_count = {}
    
    days = len(discount)-total_want+1
    
    for i in range(len(want)):
        want_count[want[i]] = number[i]
    
    for day in range(days):
        discount_count = Counter(discount[day:day+total_want])

        if want_count==discount_count:
            answer+=1
            
    return answer