def solution(gems):
    N = len(gems)
    answer = [1, N]
    types_len = len(set(gems))
    gem_found = {gems[0]:1}
    l, r = 0, 0
    
    while l<N or r<N:
        if len(gem_found) < types_len: # 모든 종류의 보석을 다 찾지 못했을 때
            r+=1
            if r==N:
                break
            gem_found[gems[r]] = gem_found.get(gems[r], 0) + 1
        
        else: # 모든 종류의 보석을 찾았을 때
            if r-l < answer[1]-answer[0]:
                answer = [l+1, r+1]
            if gem_found[gems[l]]==1:
                del gem_found[gems[l]]
            else:
                gem_found[gems[l]]-=1
            l+=1
    
    return answer