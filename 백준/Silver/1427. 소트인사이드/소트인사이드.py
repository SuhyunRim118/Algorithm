number = input()

numSplit = []

for num in number:
	numSplit.append(int(num))

numSplit.sort(reverse = True)

for i in range(len(numSplit)):
    numSplit[i] = str(numSplit[i])

numJoin = ''.join(numSplit)
print(numJoin)