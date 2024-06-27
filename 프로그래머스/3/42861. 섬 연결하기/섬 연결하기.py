def find(parent, i):
    if parent[i]==i:
        return i
    
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    
    # 합치기 (두 노드의 랭크 비교)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot]+=1

def solution(n, costs):    
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n)] # 각 노드의 부모 노드 저장하는 배열
    rank = [0]*n # 각노드의 트리의 랭크

    min_cost = 0
    edges = 0
    
    for edge in costs:
        if edges == n-1: # n-1개의 간선이 포함되 경우
            break
            
        # 두 노드의 최종 루트 찾기
        x = find(parent, edge[0])
        y = find(parent, edge[1])
        
        if x!=y: # 서로 다른 집합일 때
            union(parent, rank, x, y) # 집합 합치기
            min_cost+= edge[2]
            edges+=1
            
    return min_cost