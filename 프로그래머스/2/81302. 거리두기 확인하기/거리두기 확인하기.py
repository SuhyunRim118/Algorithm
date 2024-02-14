def solution(places):
    answer = []
    
    for place in places:
        keep_distance = True
        
        for y in range(5):
            for x in range(5):
                # 응시자일 경우
                if place[y][x]=='P':
                    # 맨해튼 거리 1일 때
                    neigh_one = [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]
                    for (ny, nx) in neigh_one:
                        if ny<0 or ny>4 or nx<0 or nx>4:
                            continue

                        if place[ny][nx]=='P':
                            keep_distance = False
                            break
                            
                    # 맨해튼 거리 2일 때
                    neigh_two = [(y-1, x-1), (y-2, x), (y-1, x+1), 
                                 (y, x-2), (y, x+2),
                                 (y+1, x-1), (y+2, x), (y+1, x+1)]
                    (ky0, kx0), (ky1, kx1), (ky2, kx2), (ky3, kx3) = neigh_one
                    
                    for idx, (ny, nx) in enumerate(neigh_two):
                        if ny<0 or ny>4 or nx<0 or nx>4:
                            continue

                        if place[ny][nx]=='P':
                            if idx==0:
                                if place[ky0][kx0]!='X' or place[ky1][kx1]!='X':
                                    keep_distance = False
                            elif idx==1:
                                if place[ky0][kx0]!='X':
                                    keep_distance = False
                            elif idx==2:
                                if place[ky0][kx0]!='X' or place[ky2][kx2]!='X':
                                    keep_distance = False
                            elif idx==3:
                                if place[ky1][kx1]!='X':
                                    keep_distance = False
                            elif idx==4:
                                if place[ky2][kx2]!='X':
                                    keep_distance = False
                            elif idx==5:
                                if place[ky1][kx1]!='X' or place[ky3][kx3]!='X':
                                    keep_distance = False
                            elif idx==6:
                                if place[ky3][kx3]!='X':
                                    keep_distance = False
                            elif idx==7:
                                if place[ky2][kx2]!='X' or place[ky3][kx3]!='X':
                                    keep_distance = False
                            
                        if keep_distance==False:
                            break

                    if keep_distance==False:
                        break
                    
            if keep_distance==False:
                break
                
        if keep_distance==False:
            answer.append(0)
        else:
            answer.append(1)
    
    return answer