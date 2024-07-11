from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, max_comb = 0, {}
    
    # 라이언, 어피치 점수 구하기
    def calculate_s(comb):
        r_s, ap_s = 0, 0

        for i in range(1, 11):
            if comb.count(i) > info[10-i]:
                r_s+=i
            elif info[10-i] > 0:
                ap_s+=i
        
        return r_s, ap_s
    
    # 점수 차이, max_s 비교
    def calculate_diff(diff, counter):
        nonlocal max_diff, max_comb
        
        if diff > max_diff:
            max_comb = counter
            max_diff = diff
        
    # 조합의 모든 경우의 수 찾기    
    for comb in combinations_with_replacement(range(11), n):
        counter = Counter(comb)

        r_s, ap_s = calculate_s(comb)
        
        if r_s > ap_s:
            diff = r_s-ap_s
            calculate_diff(diff, counter)
        
    if max_diff > 0: # 라이언이 우승할 수 있는 경우
        answer = [0]*11
        
        for n in max_comb:
            answer[10-n]= max_comb[n]
    else:
        answer = [-1]
    
    return answer