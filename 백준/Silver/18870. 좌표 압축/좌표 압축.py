N = int(input())
nums = list(map(int, input().split()))

num_sort = sorted(set(nums))

dic = {num_sort[i]:i for i in range(len(num_sort))}

for n in nums:
    print(dic[n], end=' ')