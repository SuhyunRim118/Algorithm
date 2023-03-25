testcase = int(input())
count = 0

for i in range(testcase):
    word = input()
    dic = dict()
    check = True

    for letter in word:
        if letter not in dic.keys():
            dic[letter] = 1
            
        else:
            if letter != now:
                check = False
                break

        now = letter
        
    if check == True or len(word)==1:
        count += 1

print(count)