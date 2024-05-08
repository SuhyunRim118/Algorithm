def solution(s):
    answer = [0, 0]
        
    while True:
        answer[0] += 1
        answer[1] += s.count('0')
        s = s.replace('0', '')

        s = bin(len(s))[2:]
        
        if len(s)==1:
            break
        
    return answer