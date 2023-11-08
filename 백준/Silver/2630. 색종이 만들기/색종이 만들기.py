# silver 2
# 색종이 만들기

N = int(input())

white = 0
blue = 0

square = []
for i in range(N):
    row = list(map(int, input().split()))
    square.append(row)

# function
def divide_paper(x, y, length):
    global white
    global blue
    
    white_check = 0
    blue_check = 0

    for i in range(y, y+length):
        row = square[i]
        newRow = row[x:x+length]
    
        if 0 in newRow and 1 not in newRow:
            white_check+=1
        elif 0 not in newRow and 1 in newRow:
            blue_check+=1
    
    if white_check==length:
        white+=1
    elif blue_check==length:
        blue+=1
    else:
        newN = int(length/2)
        divide_paper(x, y, newN)
        divide_paper(x, y+newN, newN)
        divide_paper(x+newN, y, newN)
        divide_paper(x+newN, y+newN, newN)

# call
divide_paper(0, 0, N)
print(white)
print(blue)