# silver 3
# 크로스 컨트리

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    
    team = set(data)
    team_pass = [t for t in team if data.count(t)==6]
    
    score = {}
    count = 0
        
    for d in data:
        if d in team_pass:
            count+=1
            if d in score.keys():
                score[d].append(count)
            else:
                score[d]=[count]

    min = -1
    min_team = []
    for k, v in score.items():
        if min==-1 or min > sum(v[:4]):
            min_team = [k]
            min = sum(v[:4])
        elif min == sum(v[:4]):
            min_team.append(k)
            
    min = -1
    for team in min_team:
        if min==-1 or min > score[team][4]:
            min = score[team][4]
            min_team = team

    print(min_team)