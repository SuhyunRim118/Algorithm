from itertools import permutations

N, M = map(int, input().split())

numbers = [i for i in range(1, N+1)]

comb = list(permutations(numbers, M))

for c in comb:
    nums = ' '.join(map(str, c))
    print(nums)