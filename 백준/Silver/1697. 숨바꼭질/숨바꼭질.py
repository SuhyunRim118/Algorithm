# silver 1
# 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

move = [-1, 1]

def bfs(x):
    queue = deque([x])

    while queue:
        # print(queue)
        # print(step[:k+2])
        x = queue.popleft()

        if x==k:
            break
        
        for nx in [x-1, x+1, x*2]:
            if nx<0 or nx>=max or nx==n:
                continue
            if step[nx]==0 or step[nx]>step[x]+1:
                step[nx] = step[x]+1
                queue.append(nx)    

n, k = map(int, input().split())

max = 100001
step = [0]*(max)

bfs(n)
print(step[k])