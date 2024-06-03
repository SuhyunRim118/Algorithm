def solution(edges):
    answer = [0, 0, 0, 0] # 생성한 정점 번호, 도넛 모양, 막대 모양, 8자 모양
    edge = {}
    
    for e_f, e_t in edges:
        if e_f not in edge.keys():
            edge[e_f] = [0, 0]
        if e_t not in edge.keys():
            edge[e_t] = [0, 0]
        
        edge[e_f][0]+=1 # 나간
        edge[e_t][1]+=1 # 들어온
        
    for node, exchange in edge.items():
        if exchange[0]>=2 and exchange[1]==0: # 생성한 정점 번호
            answer[0] = node
        elif exchange[0]==0 and exchange[1]>=1: # 막대모양
            answer[2]+=1
        elif exchange[0]>=2 and exchange[1]>=2: # 8자 모양
            answer[3]+=1
    
    answer[1] = edge[answer[0]][0] - answer[2] - answer[3] # 도넛모양
    
    return answer