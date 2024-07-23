# silver 2
# N과 M (10)

def dfs():
    check = 0

    if len(answer)==M:
        print(*answer)
        return

    for i in range(N):
        if Ns[i]!=check and visit[i]==0:
            check = Ns[i]

            if len(answer)>0 and answer[-1]>Ns[i]:
                continue

            visit[i] = 1
            answer.append(Ns[i])
            dfs()
            visit[i] = 0
            answer.pop()

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Ns = sorted(list(map(int, input().split())))
visit = [0]*N
answer = []

dfs()