def solution(board, aloc, bloc):    
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    
    def is_valid(r, c):
        return 0<=r<len(board) and 0<=c<len(board[0])
    
    def count_step(a_pos, b_pos, visited, step):
        
        # 현재 플레이어의 위치 정보 저장
        r, c = a_pos if step%2==0 else b_pos
        can_move = False
        is_op_win = True
        
        win_step, lose_step = [], []
        
        # 현재 위치에서 이동할 수 있는 모든 방향으로 이동
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            
            # 이동할 수 있는지 확인
            if is_valid(nr, nc) and (nr, nc) not in visited and board[nr][nc]:
                can_move = True
                
                # 같은 위치에서, 현재 플레이어가 먼저 이동하면 win
                if a_pos==b_pos:
                    return True, step+1
                
                # 재귀를 통해 승리여부와 이동 횟수 확인
                if step%2==0:
                    op_win, step_return = count_step([nr, nc], b_pos, visited|{(r, c)}, step+1)
                else:
                    op_win, step_return = count_step(a_pos, [nr, nc], visited|{(r, c)}, step+1)
        
                is_op_win &= op_win
                (win_step if op_win else lose_step).append(step_return)
                
        if not can_move:
            return False, step
        
        # 상대 플레이어가 이겼을 경우, 최선을 다해야 하기 때문에 win_step의 max로 반환
        if is_op_win:
            return False, max(win_step)
        # 상대 플레이어가 졌을 경우, 가장 짧은 이동 횟수로 이겨야 하기 때문에 lose_step의 min 반환
        return True, min(lose_step)
    
    _, steps = count_step(aloc, bloc, set(), 0)
    return steps
        