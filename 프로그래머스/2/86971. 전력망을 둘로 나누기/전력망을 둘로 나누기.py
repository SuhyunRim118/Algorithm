from collections import defaultdict, deque

# 송전탑 개수 차이(절대값) 계산
def check_diff(curr_node, next_node, n, connected):
    queue = deque([curr_node])
    connection = {curr_node}
    
    while queue:
        node = queue.pop()
        
        for check_node in connected[node]:
            # 현재 노드를 제외한 모든 연결된 노드 찾기
            if check_node==next_node or check_node in connection:
                continue
            connection.add(check_node)
            queue.append(check_node)
    
    # 차이 계산
    current = len(connection)
    left = n - current
    
    return abs(current-left)

def dfs(node, n, connected, visited):
    global answer
    
    for next_node in connected[node]:
        
        if visited[next_node]==False:
            visited[next_node] = True
            diff = check_diff(node, next_node, n, connected) # 송전탑 개수 차이 계산
            answer = min(answer, diff)
            
            dfs(next_node, n, connected, visited)    

answer = float('inf')
def solution(n, wires):
    connected = defaultdict(list)
    visited = [False]*n
    
    for u, v in wires:
        connected[u-1].append(v-1)
        connected[v-1].append(u-1)
    
    # print(connected)
    visited[0] = True
    dfs(0, n, connected, visited)
    
    return answer