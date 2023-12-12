# silver 5
# 올림픽

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

results = []

for n in range(N):
    num, gold, sil, bro = map(int, input().split())
    medal = {'num':num, 'gold':gold, 'silver':sil, 'bronze':bro}
    results.append(medal)

result_sort = sorted(results, key=lambda x:(-x['gold'],-x['silver'],-x['bronze']))

idx=-1
count=0
for i in range(N-1, -1, -1):
    if idx!=-1:
        if result_sort[i]['gold']==gold and result_sort[i]['silver']==silver and result_sort[i]['bronze']==bronze:
            count+=1
        else:
            break
    if result_sort[i]['num']==K:
        gold = result_sort[i]['gold']
        silver = result_sort[i]['silver']
        bronze = result_sort[i]['bronze']
        idx=i

print(idx+1-count)