# gold 5
# 암호 만들기

def check():
    v_cnt, c_cnt = 0, 0

    for a in answer:
        if a in "aeiou":
            v_cnt+=1
        else:
            c_cnt+=1
    
    if v_cnt>=1 and c_cnt>=2:
        print("".join(answer))

def dfs(idx, cnt):

    if cnt==L:
        check() # 자음, 모음 개수 체크 후 print()
        return
    
    for i in range(idx, C):
        answer.append(Cs[i])
        dfs(i+1, cnt+1) # 다음 인덱스부터 체크하도록 +1
        answer.pop()

import sys

input = sys.stdin.readline

L, C = map(int, input().split())
Cs = sorted(list(input().split()))
answer = []

dfs(0, 0)