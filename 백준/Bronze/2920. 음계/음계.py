numList = list(map(int, input().split()))
ascCheck=1
descCheck=8
asc=False
desc=False

if numList[0]==1:
    asc = True
if numList[0]==8:
    desc = True

for num in numList:
    if asc == True:
        if num == ascCheck:
            ascCheck = ascCheck+1
        else:
            asc = False
            break
    if desc == True:
        if num == descCheck:
            descCheck = descCheck-1
        else:
            desc = False
            break

if asc == True:
    print("ascending")
elif desc == True:
    print("descending")
else:
    print("mixed")