# gold 5
# 컨베이어 벨트 위의 로봇

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt_len = 2*N
belt = list(map(int, input().split()))
robot = [0]*belt_len
cnt = 0

while belt.count(0)<K: # (4) 내구도가 0인 칸의 개수가 K개 이상이라면 과정 종료
    cnt+=1

    # (1) 벨트 회전 (로봇과 함께)
    belt = belt[-1:] + belt[:-1]
    robot = robot[-1:] + robot[:-1]

    if robot[N-1]!=0: # 내리는 위치에 로봇이 있을 경우
        robot[N-1]=0

    # (2) 가장 먼저 올라간 로봇부터 한 칸씩 이동
    for idx in range(belt_len-1, -1, -1):
        if robot[idx]==0: # 로봇 없음
            continue

        if robot[idx+1]==0 and belt[idx+1]>0:
            belt[idx+1]-=1 # 내구도 -1

            if idx+1!=N-1: # 내리는 위치가 아니라면
                robot[idx+1] = robot[idx] # 로봇 이동
            robot[idx] = 0 # 현재 위치 로봇 X

    # (3) 올리는 위치
    if belt[0] > 0:
        robot[0]=max(robot)+1 # 로봇올리기
        belt[0]-=1 # 내구도 -1

print(cnt)