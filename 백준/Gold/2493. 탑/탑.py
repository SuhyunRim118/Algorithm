# gold 5
# 탑
# 스택

import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int, input().split()))
visit = ['0']*n
stack = []

# 오른쪽 탑부터 탐색
for i in reversed(range(n)):
    while stack and tower[i] >= stack[-1][1]: # 스택에 남아있는 탑 중에 현재 탑보다 낮은 탑
        visit[stack.pop()[0]] = str(i+1) # 수신
    stack.append([i, tower[i]])

print(' '.join(visit))