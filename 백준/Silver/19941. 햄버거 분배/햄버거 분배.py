import sys

input = sys.stdin.readline

N, K = map(int, input().split())
location = list(input())
count = 0

for i in range(N):
    if location[i]=='P':
        for j in range(max(0, i-K), min(i+K+1, N)):
            if location[j]=='H':
                location[j] = 1
                count+=1
                break

print(count)