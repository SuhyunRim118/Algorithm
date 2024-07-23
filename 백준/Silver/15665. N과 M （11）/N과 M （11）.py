# silver 2
# N과 M (11)

def dfs():
    check = 0

    if len(answer)==M:
        print(*answer)
        return
    
    for i in range(N):
        if check!=Ns[i]:
            check = Ns[i]
            answer.append(Ns[i])
            dfs()
            answer.pop()


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Ns = sorted(list(map(int, input().split())))
answer = []

dfs()