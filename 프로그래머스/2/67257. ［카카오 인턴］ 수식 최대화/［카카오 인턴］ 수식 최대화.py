from itertools import permutations
import re

def operate(e,a,b):
    if e=='+':
        return a+b
    elif e=='-':
        return a-b
    elif e=='*':
        return a*b

def solution(expression):
    answer = []
    ops = []
    
    exp = re.split('([^0-9])', expression)
    
    for i in range(1, len(exp), 2):
        ops.append(exp[i])
    used_ops = set(ops)
    
    ops_list = list(permutations(used_ops, len(used_ops)))
    
    for ops in ops_list:
        ex = exp
        
        for op in ops:
            calc = []
            
            for e in ex:
                if calc and calc[-1]==op:
                    operation = calc.pop()
                    calc[-1] = operate(operation, int(calc[-1]), int(e))
                else:
                    calc.append(e)
                    
            ex = calc
            
        answer.append(abs(ex[0]))
        
    return max(answer)