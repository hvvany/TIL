
# from pprint import pprint

n = int(input())
gam_matrix = [list(map(int,input().split())) for _ in range(n)]

m = int(input())
order_matrix = [list(map(int,input().split())) for _ in range(m)]

# 명령어 처리 식
for order in order_matrix:
    col = order[0]

    direc = order[1]
    rotat = order[2]
    val_idx_lst = []
    for _ in range(rotat):
        if direc == 0:
            gam_matrix[col-1].append(gam_matrix[col-1].pop(0))
        else:
            gam_matrix[col-1].insert(0,gam_matrix[col-1].pop())
# pprint(gam_matrix)
# 모래시계...? 아하 홀수!
idx1, idx2 = 0, n-1
gam_sum = 0
for row in range(n):
    if idx1 <= idx2:
        gam_sum += sum(gam_matrix[row][idx1:idx2+1])
    else:
        gam_sum += sum(gam_matrix[row][idx2:idx1+1])
    idx1 += 1
    idx2 -= 1

print(gam_sum)