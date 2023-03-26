ran = list(map(int, input().split()))

sum = 0
count = 0
for i in range(1, 1000, 1):
    for j in range(i):
        count+=1
        
        if count > ran[1]:
            break
        if count >= ran[0] and count <= ran[1]:
            sum += i

print(sum)