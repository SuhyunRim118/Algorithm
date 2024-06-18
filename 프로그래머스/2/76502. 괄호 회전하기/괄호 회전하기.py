def solution(s):
    answer = 0
    pair = {']':'[', ')':'(', '}':'{'}
    
    for i in range(len(s)):
        stack = []
        str = s[i:] + s[:i]
        
        for j in range(len(s)):
            if str[j] in pair.values():
                stack.append(str[j])
            else:
                if not stack:
                    break
                if stack[-1]==pair[str[j]]:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer+=1
        
    return answer