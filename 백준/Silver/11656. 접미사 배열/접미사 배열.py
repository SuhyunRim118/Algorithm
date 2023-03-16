word = input()
wordL=[]

for i in range(len(word)):
    wordL.append(word[i:])

wordL.sort()
for words in wordL:
    print(words)