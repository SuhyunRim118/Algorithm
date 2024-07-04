# 다익스트라
import heapq

def solution(N, road, K):
    answer = 0
    village = [[]for _ in range(N+1)] # 도로 정보
    time = [float('inf')]*(N+1) # 배달 시간 정보
    time[1] = 0
    queue = []
    heapq.heappush(queue, (0, 1))

    for a, b, t in road:
        village[a].append((b, t))
        village[b].append((a, t))
    
    while queue:
        curr_time, vil_n = heapq.heappop(queue)
        
        for vil_next, weight in village[vil_n]:
            t = curr_time + weight
            if t < time[vil_next]: # 최소 배달 시간
                time[vil_next] = t
                heapq.heappush(queue, (t, vil_next))
                    
    answer = sum(1 for t in time if t<=K)

    return answer