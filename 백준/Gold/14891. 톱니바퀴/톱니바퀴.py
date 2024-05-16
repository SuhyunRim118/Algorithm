# gold 5
# 톱니바퀴

import sys
import copy
input = sys.stdin.readline
from collections import deque

wheel = []
for i in range(4):
    wheel.append(list(map(int, input().rstrip())))

overlap = [[1], [0, 2], [1, 3], [2]]

K = int(input())
for k in range(K):
    visit = [0]*4
    temp = copy.deepcopy(wheel)
    w_num, dir = map(int, input().split())
    
    w_q = deque([(w_num-1, dir)])
    
    while w_q:
        turn, turn_dir = w_q.popleft()

        # 맞닿은 톱니바퀴 회전
        for over in overlap[turn]:

            if visit[over]==1:
                continue
            if (over < turn and temp[over][2]==temp[turn][6]) or (over>turn and temp[over][6]==temp[turn][2]):
                visit[over]=1
                continue

            if turn_dir==1: # 맞닿은 톱니바퀴는 반시계방향 회전
                wheel[over] = temp[over][1:] + temp[over][:1]
                next_dir = -1
            else: # 맞닿은 톱니바퀴는 시계방향 회전
                wheel[over] = temp[over][-1:] + temp[over][:-1]
                next_dir = 1
            
            visit[over]=1
            if over==1 or over==2:
                w_q.append((over, next_dir))
        
        # 해당되는 톱니바퀴 회전
        if visit[turn]==0:
            visit[turn]=1
            if turn_dir==1:
                wheel[turn] = temp[turn][-1:] + temp[turn][:-1]
            else:
                wheel[turn] = temp[turn][1:] + temp[turn][:1]

print(wheel[0][0] + wheel[1][0]*2 + wheel[2][0]*4 + wheel[3][0]*8)