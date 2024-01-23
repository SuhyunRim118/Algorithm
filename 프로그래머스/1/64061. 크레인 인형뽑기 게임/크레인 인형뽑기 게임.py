def solution(board, moves):
    answer = 0
    
    basket = []
    
    for move in moves:
        for b in board:
            if b[move-1]!=0:
                basket.append(b[move-1])
                b[move-1] = 0
                break
        if len(basket)>=2 and basket[-1]==basket[-2]:
            basket.pop()
            basket.pop()
            answer+=2
                
    return answer