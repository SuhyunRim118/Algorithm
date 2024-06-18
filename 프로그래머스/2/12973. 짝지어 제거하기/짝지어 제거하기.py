def solution(s):
    answer = 0
    stack = []
    
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1]==s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    
    if not stack:
        answer = 1

    return answer