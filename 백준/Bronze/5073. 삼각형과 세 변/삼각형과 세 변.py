import sys
input = sys.stdin.readline

while(True):
    tri = list(map(int, input().split()))
    tri.sort()
    if tri.count(0)==3:
        break
    
    if tri[2] >= tri[0]+tri[1]:
        print('Invalid')
    else:
        if tri.count(tri[0])==3:
            print('Equilateral')
        elif tri.count(tri[0])==2 or tri.count(tri[1])==2:
            print('Isosceles')
        else:
            print('Scalene')