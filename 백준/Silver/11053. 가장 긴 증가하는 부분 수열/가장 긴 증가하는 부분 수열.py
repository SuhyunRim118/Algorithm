N = int(input())
A = list(map(int, input().split()))

answer = [1]*N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            answer[i] = max(answer[i], answer[j]+1)

print(max(answer))