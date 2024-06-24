from itertools import combinations

def solution(orders, course):
    answer = []
    comb = {}
    
    for order in orders:
        for n in course:
            ncr = list(combinations(order, n)) # 메뉴 조합 찾기
            for c in ncr:
                c_l = list(c)
                c_l.sort()
                menu = ''.join(c_l)
                if menu not in comb:
                    comb[menu] = 0
                comb[menu]+=1
    
    # 가장 많이 함께 주문한 단품메뉴 찾기
    for c in course:
        check = {k: v for k, v in comb.items() if v >= 2 and len(k)==c}
        left = [k for k, v in check.items() if v>=max(check.values())]
        answer.extend(left)
        
    answer.sort()
    
    return answer