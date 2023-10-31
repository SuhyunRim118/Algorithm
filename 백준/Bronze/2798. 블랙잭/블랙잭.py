card_num, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = -1

for i in range(card_num-2):
    first = cards[i]
    for j in range(i+1, card_num-1):
        second=cards[j]
        for k in range(j+1, card_num):
            third = cards[k]
            
            top = first+second+third
            
            if top <= M and answer < top:
                answer=top

print(answer)