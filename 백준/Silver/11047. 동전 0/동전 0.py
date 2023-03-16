value = list(map(int, input().split()))
coins=[]
count = 0

for i in range(value[0]):
    coin = int(input())
    coins.append(coin)

idx = len(coins)-1
total = int(value[1])

for i in range(idx, -1, -1):
    if total >= coins[i]:
        n = total // coins[i]
        total -= (coins[i]*n)
        count += n

print(count)