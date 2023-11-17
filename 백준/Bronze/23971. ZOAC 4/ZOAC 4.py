import sys
import math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())
count = 0
        
print(math.ceil(H/(N+1)) * math.ceil(W/(M+1)))