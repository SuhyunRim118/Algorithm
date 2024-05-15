# gold 5
# 치킨 배달

import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())
city = []
chicken = []
house = []
answer = 9999999

for i in range(N):
    city.append(list(map(int, input().split())))

    for j in range(N):
        if city[i][j]==1:
            house.append([j, i])
        elif city[i][j]==2:
            chicken.append([j, i])

for chosen in combinations(chicken, M):
    total_dis = 0

    for hx, hy in house:
        distance = 9999999
        for cx, cy in chosen:
            distance = min(distance, abs(hx-cx)+abs(hy-cy))

        total_dis += distance
    
    answer = min(answer, total_dis)

print(answer)