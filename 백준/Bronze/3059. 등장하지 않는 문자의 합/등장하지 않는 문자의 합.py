testcase = int(input())
inputL=[]
for i in range(testcase):
    inputL.append(input())

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(testcase):
    sum = 0

    for a in alpha:
        if a not in inputL[i]:
            sum += ord(a)
    print(sum)