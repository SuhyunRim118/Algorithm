

def solution(n):
    answer = []
    
    def hanoi(start, dest, mid, n):
        if n==1:
            answer.append([start, dest])
        else:
            # 1->2 기둥 (n-1개의 원판 이동)
            hanoi(start, mid, dest, n-1)
            # 1->3 기둥 (n번째 원판 이동)
            answer.append([start, dest])
            # 2->3 기둥 (n-1개의 원판 이동)
            hanoi(mid, dest, start, n-1)

    hanoi(1, 3, 2, n)
    
    return answer