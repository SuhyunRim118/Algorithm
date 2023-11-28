import sys

N = int(sys.stdin.readline())
# heights = [i for i in range(1, N+1)]
A = list(map(int, sys.stdin.readline().split()))
A_cpy = A

order = [] # height가 들어감

for i in range(N-1, -1, -1):
    height = i+1
    count = 0
    if len(order)==0:
        order.append(height)
    else:
        for o in order:
            if o > height:
                count += 1
            if count==A_cpy[i]:
                if order.index(o)==len(order)-1:
                    order.append(height)
                else:
                    order.insert(order.index(o)+1, height)
                break
            elif count>A_cpy[i]:
                order.insert(order.index(o), height)
                break 
    A[i] = -1

print(' '.join(map(str, order)))