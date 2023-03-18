testcase = int(input())

for i in range(testcase):
    sum = 0
    score = 0

    test = input()

    for each in test:
        if each == 'O':
            score += 1
            sum += score
        elif each == 'X':
            score = 0
        
    print(sum)