# gold 5
# 뱀과 사다리 게임

import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global count
    q = deque([1])

    while q:
        location = q.popleft()

        if location==100:
            break

        for i in range(1, 7):
            count = game[location]
            next = location+i

            if next>100:
                continue
            
            if next in magic.keys():
                next = magic[next]
            
            if game[next]==0 or game[next]>count+1:
                game[next] = count+1
                q.append(next)

N, M = map(int, input().split())
magic = {}
game = [0]*101
count = 0

for n in range(N):
    x, y= map(int, input().split())
    magic[x] = y
for m in range(M):
    u, v = map(int, input().split())
    magic[u] = v

bfs()
# print(game)
print(game[100])