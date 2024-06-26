from collections import deque

def solution(info, edges):
    
    p_c = [[] for _ in range(len(info))]
    q = deque([])
    max_sheep = 0
    
    for edge in edges:
        p_c[edge[0]].append(edge[1])
    
    q.append((0, 1, 0, set()))
        
    while q:
        node, s_cnt, w_cnt, visit = q.popleft()
        max_sheep = max(max_sheep, s_cnt)
        visit.update(p_c[node])
        
        for n_node in visit:
            if info[n_node]==1: # 늑대
                if s_cnt!=w_cnt+1:
                    q.append((n_node, s_cnt, w_cnt+1, visit-{n_node}))
                    
            else: # 양
                q.append((n_node, s_cnt+1, w_cnt, visit-{n_node}))

    return max_sheep