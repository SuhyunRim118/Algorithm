nums = []
mod = []

for i in range(10):
    num = int(input())
    nums.append(num)
    mod.append(num%42)

result = list(set(mod))

print(len(result))