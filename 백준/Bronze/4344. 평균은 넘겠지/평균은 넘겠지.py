testcase = int(input())

for i in range(testcase):
    case = list(map(int, input().split()))

    avg = sum(case[1:])/case[0]

    cnt = 0
    for score in case[1:]:
        if score > avg:
            cnt = cnt + 1
        
    rate = cnt/case[0] * 100
    print(f'{rate:0.3f}%')