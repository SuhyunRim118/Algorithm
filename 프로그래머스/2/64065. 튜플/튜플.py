def solution(s):
    answer = []
    s = s.replace("{", "").replace("}", "")
    s_list = list(s.split(','))
    s_set = set(s_list)
    
    s_dict = {}
    for each in s_set:
        s_dict[each] = s_list.count(each)
        
    sorted_dict = dict(sorted(s_dict.items(), key= lambda item:item[1], reverse=True))

    answer = [int(k) for k, v in sorted_dict.items()]
    
    return answer