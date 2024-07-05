from collections import deque

def dfs(node, visit, computers):
    visit[node] = True
    
    for i, connect in enumerate(computers[node]):
        if connect and not visit[i]:
            dfs(i, visit, computers)
    
def solution(n, computers):
    answer = 0
    visit = [False]*n
    
    for i in range(n):
        
        if not visit[i]:
            dfs(i, visit, computers)
            answer+=1

    return answer