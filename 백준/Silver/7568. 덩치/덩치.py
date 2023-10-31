num = int(input())
students=[]

for i in range(num):
    w, h = map(int, input().split())
    students.append([w, h])

for stu1 in students:
    rank=1
    for stu2 in students:
        if stu1[0]<stu2[0] and stu1[1]<stu2[1]:
            rank+=1
    
    print(rank, end=' ')