nums = list(map(int, input().split()))
numD = dict()
numberD = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

for i in range(nums[0], nums[1]+1,1):
    num = ''
    for n in str(i):
        check = numberD[int(n)]
        num = num + check + ' '
    
    numD[num] = i

sortD = dict(sorted(numD.items()))
count=0

for t in sortD.values():
    count+=1
    print(t, end=' ')

    if count%10 == 0:
        print('')