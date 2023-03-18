price = int(input())

count = 0
change = 0
rest = 1000 - price

while True:        
    if rest >= 500:
        change = 500
    elif rest >= 100:
        change = 100
    elif rest >= 50:
        change = 50
    elif rest >= 10:
        change = 10
    elif rest >= 5:
        change = 5
    elif rest >= 1:
        change = 1
    else: # rest == 0
        break
    
    rest -= change
    count += 1

print(count)