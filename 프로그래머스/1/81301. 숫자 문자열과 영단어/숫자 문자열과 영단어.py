def solution(s):
    answer = ''
    
    num_english = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    string = False
    
    for i in range(len(s)):
        if s[i].isdigit():
            if string==True:
                answer+=str(num_english[s[start_idx:i]])
                string=False
            answer+=s[i]
        else:
            if string==True:
                if s[start_idx:i] in num_english.keys():
                    answer+=str(num_english[s[start_idx:i]])
                    string=False                    
                    
            if string==False:
                string=True
                start_idx = i
                
    if string==True:
        answer+=str(num_english[s[start_idx:i+1]])
    
    return int(answer)