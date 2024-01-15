import sys

input = sys.stdin.readline
games = {'Y':1, 'F':2, 'O':3}

N, type = map(str, input().split())
N = int(N)
ppl = set()

for i in range(N):
    name = input().strip()
    ppl.add(name)
    
print(int(len(ppl)/games[type]))