# silver 2
# N과 M (9)

def dfs():
    check=0

    if len(answer)==M:
        print(*answer)
        return
    
    for i in range(N):
        if check!=Ns[i] and visit[i]==0:
            answer.append(Ns[i])
            visit[i] = 1
            check = Ns[i]
            dfs()
            answer.pop()
            visit[i] = 0

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Ns = sorted(list(map(int, input().split())))
visit = [0]*N
answer = []

dfs()