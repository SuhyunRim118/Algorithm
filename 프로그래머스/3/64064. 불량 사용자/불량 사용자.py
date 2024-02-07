from itertools import permutations

def check(case, banned_id):
    for i in range(len(case)):
        if len(case[i])!=len(banned_id[i]):
            return False
        for j in range(len(case[i])):
            if banned_id[i][j]!='*' and case[i][j]!=banned_id[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    check_list = []
    
    for case in permutations(user_id, len(banned_id)):
        if check(case, banned_id):
            if set(case) not in check_list:
                check_list.append(set(case))
        
    return len(check_list)