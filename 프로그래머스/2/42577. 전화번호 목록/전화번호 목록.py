def solution(phone_book):
    answer = True
    
    phone_book.sort() # 인접한 번호들끼리 비교할 수 있도록
    
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
        
    return answer