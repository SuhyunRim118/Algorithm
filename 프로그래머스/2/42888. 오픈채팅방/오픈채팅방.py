def solution(record):
    answer = []
    order = []
    action_id = {'Enter':[], 'Leave':[]}
    id_name = {}
    
    for sentence in record:
        r = sentence.split()
        
        if r[0]!='Change':
            order.append(r[0])
            action_id[r[0]].append(r[1])
        
        if r[0]=='Enter':
            id_name[r[1]] = r[2]
        elif r[0]=='Change':
            id_name[r[1]] = r[2]

    for action in order:
        if action=='Enter':
            answer.append(id_name[action_id[action][0]] + '님이 들어왔습니다.')
        elif action=='Leave':
            answer.append(id_name[action_id[action][0]] + '님이 나갔습니다.')
        
        action_id[action].pop(0)
    
    return answer