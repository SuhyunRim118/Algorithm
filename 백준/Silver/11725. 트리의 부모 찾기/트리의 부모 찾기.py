import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())
tree = dict()
for i in range(1,N+1):
    tree[i] = []
visited = [False]*(N+1)
rootN = [0]*(N+1)

for i in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def find_root(root):
    visited[root] = True
    
    for nodes in tree[root]:
        if visited[nodes]==False:
            rootN[nodes]=root
            find_root(nodes)

find_root(1)
print('\n'.join(map(str, rootN[2:])))