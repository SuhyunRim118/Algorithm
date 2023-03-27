num = int(input())
lastName = dict()
select = []

for i in range(num):
    name = input()
    letter = name[0]
    if letter in lastName.keys():
        lastName[letter] += 1
    else:
        lastName[letter] = 1

for letter in lastName:
    if lastName[letter] >= 5:
        select.append(letter)
    
if len(select) == 0:
    print("PREDAJA")
else:
    select.sort()
    for letter in select:
        print(letter, end='')