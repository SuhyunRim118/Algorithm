testcase = int(input())

for i in range(testcase):
    equ = list(map(str, input().split()))
    num = float(equ[0])

    for j in range(1, len(equ), 1): # @는 3을 곱하고, %는 5를 더하며, #는 7을 빼는 연산자
        if equ[j]=='@':
            num *= 3
        elif equ[j]=='%':
            num += 5
        elif equ[j]=='#':
            num -=7
        
    print(f'{num:0.2f}')