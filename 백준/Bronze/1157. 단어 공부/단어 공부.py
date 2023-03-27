word = input()
word = word.upper()
dic = dict()
max = 0
check = -1

for letter in word:
    if letter in dic.keys():
        dic[letter] += 1
    else:
        dic[letter] = 1

for key in dic.keys():
    if dic[key] > max:
        check = 0
        max = dic[key]
        maxKey = key
    elif dic[key] == max:
        check = 1

if check == 1:
    print("?")
else:
    print(maxKey)