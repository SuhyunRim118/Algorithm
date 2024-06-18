def solution(n, k, cmd):
    answer = ['O']*n
    delete = []
    up = [i-1 for i in range(n+2)]
    down = [i+1 for i in range(n+2)]
    k+=1
    
    for c in cmd:
        if c[0]=='C': # 삭제
            delete.append(k)
            
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            
            k = up[k] if n<down[k] else down[k]
                
        elif c[0]=='Z': # 복구
            d = delete.pop()
            
            up[down[d]] = d
            down[up[d]] = d
            
        else:
            action, num = c.split()
            
            if action=='U':
                for _ in range(int(num)):
                    k = up[k]
            else:
                for _ in range(int(num)):
                    k = down[k]
    
    for d in delete:
        answer[d-1] = 'X'
        
    return ''.join(answer)