def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0]*3
    
    for i in range(len(answers)):
        a = answers[i]
        if one[i%5]==a:
            score[0]+=1
        if two[i%8]==a:
            score[1]+=1
        if three[i%10]==a:
            score[2]+=1
    
    for i in range(3):
        max_s = max(score)
        if score[i]==max_s:
            answer.append(i+1)
    
    return answer