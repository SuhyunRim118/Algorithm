import sys

input = sys.stdin.readline

N = int(input())
cookie = []
head = False
heart_x = 0
heart_y = 0
body_len = [0]*5

for n in range(N):
    row = input().strip()
    cookie.append(row)
    
    if head==False and '*' in row:
        head = True
        heart_x = len(cookie)+1
        heart_y = row.index('*')+1
    elif head==True and len(cookie)==heart_x:
        body_len[0] = row[:heart_y-1].count('*') #왼쪽 팔
        body_len[1] = row[heart_y:].count('*') #오른쪽 팔
    elif head==True:
        if row[heart_y-1]=='*':
            body_len[2]+=1
        else:
            if row[heart_y-2]=='*':
                body_len[3]+=1
            if row[heart_y]=='*':
                body_len[4]+=1
    
print(heart_x, heart_y)
print(*body_len)