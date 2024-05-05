# silver 1
# 정수 삼각형

import sys

input = sys.stdin.readline

N = int(input())
triangle = []

for n in range(N):
    triangle.append(list(map(int, input().split())))

sum = triangle[0][0]

for n in range(1, N):

    row_n = len(triangle[n])

    for i in range(row_n):
        if i==0:
            triangle[n][i] += triangle[n-1][i]
        elif i==row_n-1:
            triangle[n][i] += triangle[n-1][i-1]
        else:
            triangle[n][i] += max(triangle[n-1][i-1], triangle[n-1][i])

print(max(triangle[N-1]))