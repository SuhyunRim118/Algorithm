num = int(input())

check = 2
while check <= num:
    if num % check == 0:
        print(check)
        num /= check
    else:
        check += 1