case = list(map(int, input().split()))

sum = 0

for num in case:
    sum = sum + num**2

print(sum%10)