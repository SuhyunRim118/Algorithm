import sys

input = sys.stdin.readline

N, new_s, P = map(int, input().split())

if N==0:
    rank = 1
elif N>0:
    scoreList = list(map(int, input().split()))
    
    if N==P and scoreList[N-1]>=new_s:
        rank=-1
    else: 
        rank=N+1
        for i in range(N):
            if scoreList[i] <= new_s:
                rank = i+1
                break
            
print(rank)