import math

def solution(n, words):
    answer = [0, 0]
    word_set = {words[0]}
    prev = words[0]

    for i in range(1, len(words)):
        word = words[i]
        if word in word_set or prev[-1]!=word[0]:
            answer[0] = (i+1)%n if (i+1)%n!=0 else n
            answer[1] = math.ceil((i+1)/n)
            
            return answer
        
        word_set.add(words[i])
        prev = word

    return answer