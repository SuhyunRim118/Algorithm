def solution(arr1, arr2):
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    
    for h in range(len(arr2[0])):
        a = []
        for i in range(len(arr1)): # 행
            sum = 0
            for j in range(len(arr1[0])): # 열
                sum += arr1[i][j]*arr2[j][h]

            answer[i][h] = sum         
    
    return answer