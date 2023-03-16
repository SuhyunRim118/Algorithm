word = input()
count = 0

for letter in word:
    print(letter, end = '')

    count += 1
    if count%10 == 0:
        print("")