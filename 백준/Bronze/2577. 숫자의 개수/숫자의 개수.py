numA = int(input())
numB = int(input())
numC = int(input())

dic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

num = 0
num = numA*numB*numC

for i in map(int, str(num)):
    dic[i]+=1

for times in dic:
    print(dic[times])