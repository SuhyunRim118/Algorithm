import math

room = input()
dic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
max = 0

for i in map(int, str(room)):
    dic[i]+=1

dic[6] = math.ceil((dic[6] + dic[9])/2)

for i in range(9):
    if dic[i]>max:
        max = dic[i]

print(max)