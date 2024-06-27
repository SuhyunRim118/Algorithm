from collections import Counter

def solution(nums):
    answer = 0
    
    counter = Counter(nums)
    n = len(nums)//2
    
    if n <= len(counter):
        return n
    else:
        return len(counter)