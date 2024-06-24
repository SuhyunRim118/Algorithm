def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report_id = {}
    report_cnt = {}
    
    for i in id_list: # 초기화
        report_id[i] = []
        report_cnt[i] = 0
    
    for r in report:
        frm, to = r.split()
        
        if frm not in report_id[to]:
            report_id[to].append(frm) # 신고한 사람들 기록
            report_cnt[to]+=1 # 신고 받은 사람 cnt+=1
    
    for frm, cnt in report_cnt.items():
        if cnt>=k:
            for to in report_id[frm]:
                answer[id_list.index(to)]+=1

    return answer