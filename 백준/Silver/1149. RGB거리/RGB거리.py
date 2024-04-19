# silver 1
# RGB거리

import sys
input = sys.stdin.readline

N = int(input())
house = []

for n in range(N):
    house.append(list(map(int, input().split())))

for n in range(1, N):
    house[n][0] += min(house[n-1][1:])
    house[n][1] += min(house[n-1][0], house[n-1][2])
    house[n][2] += min(house[n-1][:2])

print(min(house[N-1]))