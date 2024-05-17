# gold 4
# 주사위 굴리기

import sys
input = sys.stdin.readline

dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]

def move_dice(x, y, direction):
    global dice

    if direction==1: # 동
        dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]
    elif direction==2: # 서
        dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]
    elif direction==3: # 북
        dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]
    elif direction==4: # 남
        dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]
    
    if board[y][x]==0:
        board[y][x] = dice[6]
    else:
        dice[6] = board[y][x]
        board[y][x] = 0

N, M, y, x, K = map(int, input().split())
board = []
dice = [0]*7

for n in range(N):
    board.append(list(map(int, input().split())))

move = list(map(int, input().split()))

for direction in move:
    nx = x + dir[direction-1][0]
    ny = y + dir[direction-1][1]

    if 0<=nx<M and 0<=ny<N:
        move_dice(nx, ny, direction)
        print(dice[1])
        x, y = nx, ny