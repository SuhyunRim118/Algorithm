savedL = dict()
L=[]
idx=[]
sum = 0

for i in range(8):
    score = int(input())
    L.append(score)
    savedL[score] = i+1

L.sort(reverse = True)

for i in range(5):
    sum += L[i]

print(sum)
for i in range(5):
    idx.append(savedL[L[i]])

idx.sort()

for index in idx:
	print(index, end=' ')