# gold 5
# 빗물
# 74% 틀림

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))
answer = 0

for w in range(1, W-1):
    left_max = max(block[:w])
    right_max = max(block[w+1:]
)
    compare = min(left_max, right_max)

    if block[w] < compare:
        answer += (compare - block[w])

print(answer)