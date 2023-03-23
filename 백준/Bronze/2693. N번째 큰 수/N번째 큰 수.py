testcase = int(input())

for i in range(testcase):
    numList = list(map(int, input().split()))
    numList.sort(reverse = True)
    print(numList[2])