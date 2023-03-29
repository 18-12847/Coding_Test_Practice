def solution(board, moves):
    tmp = [[] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[len(board)-1-j][i] != 0:
                tmp[i].append(board[len(board)-1-j][i])
    stack, cnt = [0], 0
    for i in moves:
        if tmp[i-1] == []:
            continue
        if tmp[i-1][-1] == stack[-1]:
            stack.pop()
            tmp[i-1].pop()
            cnt += 2
        else:
            stack.append(tmp[i-1].pop())
    return cnt