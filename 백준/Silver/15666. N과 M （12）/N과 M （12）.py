# silver 2
# N과 M (12)

def dfs():
    check = 0

    if len(answer)==M:
        print(*answer)
        return
    
    for i in range(N):
        if check!=Ns[i]:
            check = Ns[i]

            if len(answer)>0 and answer[-1]>Ns[i]:
                continue

            answer.append(Ns[i])
            dfs()
            answer.pop()


import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Ns = sorted(list(map(int, input().split())))
answer = []

dfs()