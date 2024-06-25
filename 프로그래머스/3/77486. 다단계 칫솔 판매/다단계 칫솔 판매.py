def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = {name:0 for name in enroll}
    grp = dict(zip(enroll, referral))
    
    for i in range(len(seller)):
        person = seller[i]
        price = amount[i]*100
        
        while price>0 and person!='-':
            div = price//10
            
            answer[person]+=(price-div) # 이익
            
            person = grp[person]
            price = div
                            
    return [answer[name] for name in enroll]