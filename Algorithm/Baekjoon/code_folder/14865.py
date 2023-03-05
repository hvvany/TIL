import sys
input = sys.stdin.readline

def solution():
    coor = dict()
    idx_heap = []
    check_set = set()
    pair_num = 1
    before_plus = False
    start_x, start_y = 0, 0
    first_regist = True
    regist_x = 0
    plus_start = False

    N = int(input())
    for i in range(N+1):
        if i == N:
            if plus_start:
                idx_heap.append(regist_x)
                coor[regist_x] = pair_num
            x, y = start_x, start_y
        else:
            x, y = map(int,input().split())
        if i == 0:
            start_x = x
            start_y = y
            if y > 0:
                plus_start = True
                before_plus = True
        if y > 0 and not before_plus:
            first_regist = False
            idx_heap.append(x)
            coor[x] = pair_num
            if pair_num in check_set:
                pair_num += 1
            else:
                check_set.add(pair_num)
            before_plus = True
        elif y < 0 and before_plus:
            if first_regist:
                regist_x = x
                first_regist = False
                before_plus = False
                continue
            idx_heap.append(x)
            coor[x] = pair_num
            if pair_num in check_set:
                pair_num += 1
            else:
                check_set.add(pair_num)
            before_plus = False
    idx_heap.sort()
    ans_in, ans_out = 0, 0
    cnt = 0
    visited_set = set()
    before_num = -1
    for x in idx_heap:
        check = coor[x]
        if cnt == 0:
            ans_out += 1
        # 괄호 닫히는 경우
        if check in visited_set:
            cnt -= 1
            if before_num == check:
                ans_in += 1
        # 괄호 열리는 경우
        else:
            cnt += 1
            visited_set.add(check)
        before_num = check
    return (ans_out,ans_in)
print(*solution())