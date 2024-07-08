# silver 2
# 결혼식

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
friends = [[] for _ in range(N)]
invitation = {0}

for m in range(M):
    a, b = map(int, input().split())

    friends[a-1].append(b-1)
    friends[b-1].append(a-1)

for friend1 in friends[0]:
    invitation.add(friend1)
    
    for friend2 in friends[friend1]:
        if friend2 not in invitation:
            invitation.add(friend2)

print(len(invitation)-1)