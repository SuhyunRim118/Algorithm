# silver 2
# DFS와 BFS

N, M, V = map(int, input().split())
graph = [[False]*(N+1) for _ in range(N+1)]
dfs_visit = [False]*(N+1)
bfs_visit = [False]*(N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(V):
    dfs_visit[V] = True
    print(V, end=' ')
    for i in range(1, N+1):
        if graph[V][i]==True and dfs_visit[i]==False:
            dfs(i)
        

def bfs(V):
    queue = [V]
    bfs_visit[V] = True
    
    while queue:
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if graph[V][i]==True and bfs_visit[i]==False:
                queue.append(i)
                bfs_visit[i]=True

dfs(V)
print()
bfs(V)