num = int(input())

fibo = [0,1]

for i in range(2,num+1,1):
    plus = fibo[i-1] + fibo[i-2]
    fibo.append(plus)
    
print(fibo[num])