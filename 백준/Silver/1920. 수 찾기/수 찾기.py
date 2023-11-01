N = int(input())
A_List = set(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

answers = [1 if n in A_List else 0 for n in num]

print(*answers, sep='\n')