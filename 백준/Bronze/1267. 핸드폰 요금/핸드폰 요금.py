num = int(input())
calls = list(map(int, input().split()))

y = 0
m = 0

for i in range(num):
    y += calls[i]//30*10
    m += calls[i]//60*15

    if calls[i]%30 > -1:
        y += 10
    if calls[i]%60 > -1:
        m += 15

if y<m:
    print("Y", y)
elif y>m:
    print("M", m)
else:
    print("Y M", y)