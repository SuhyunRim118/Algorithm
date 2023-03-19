testcase = int(input())
numL = []

for i in range(testcase):
    num = int(input())
    numL.append(num)

for num in numL:
    num = str(num)
    reverse = ''
    for i in range(len(num)):
        reverse = reverse + num[len(num)-i-1]
        
    sum = int(num) + int(reverse)
    sum = str(sum)
    
    for i in range(len(sum)):
        if sum[i] != sum[len(sum)-i-1]:
            print("NO")
            break
    else:
        print("YES")