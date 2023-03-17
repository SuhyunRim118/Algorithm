n = int(input())
nums = list(map(int, input().split()))

nums = list(set(nums))
nums.sort()

for num in nums:
    print(num, end=' ')