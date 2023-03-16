num = int(input())
price = list(map(int, input().split()))

price.sort()
sum = 0

for i in range(num-1):
    sum += price[i]

print(sum)