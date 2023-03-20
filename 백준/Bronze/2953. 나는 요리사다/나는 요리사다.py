p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
p3 = list(map(int, input().split()))
p4 = list(map(int, input().split()))
p5 = list(map(int, input().split()))

score = {1:0, 2:0, 3:0, 4:0, 5:0}
person = 0
maxScore = 0

for i in range(4):
    score[1] += p1[i]
    score[2] += p2[i]
    score[3] += p3[i]
    score[4] += p4[i]
    score[5] += p5[i]

for i in range(5):
    if score[i+1]>maxScore:
        person = i+1
        maxScore = score[i+1]

print(person, maxScore)