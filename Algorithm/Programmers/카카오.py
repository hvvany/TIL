def solution(board, moves):
    result = []
    cnt = 0

    for idx_w in moves:
        for h in board:
            if h[idx_w-1] != 0:
                result.append(h[idx_w-1])
                h[idx_w-1] = 0
                break
    init_len = len(result)

    i=0
    while i+1 < len(result):
        if result[i] == result[i+1]:
            result.pop(i)
            result.pop(i)
            i=0
        else:
            i += 1
    answer = init_len - len(result)  
    return answer

mov = [1,5,3,5,1,2,1,4]
bod = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
print(solution(bod,mov))