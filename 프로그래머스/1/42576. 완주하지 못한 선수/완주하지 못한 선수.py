from collections import Counter

def solution(participant, completion):
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    # p_set = set(participant)
    # c_set = set(completion)

    if len(p_counter.keys())!=len(c_counter.keys()):
        p_set = set(p_counter.keys())
        c_set = set(c_counter.keys())
        return list(p_set-c_set)[0]
    
    for p in p_counter.keys():
        if p_counter[p]!=c_counter[p]:
            return p
