T, W = map(int,input().split())
zadu_lst_1 = []
zadu_lst_2 = []
zadu_sum_lst_1 = 

before_num = '1'
cnt = 0
for _ in range(T):
    if input() == '1':
        if before_num == '2':
            zadu_lst_2.append(cnt)
            cnt = 1
        else:
            cnt += 1
        before_num = '1'
    else:
        if before_num == '1':
            zadu_lst_1.append(cnt)
            cnt = 1
        else:
            cnt += 1
        before_num = '2'
if before_num == '1':
    zadu_lst_1.append(cnt)
else:
    zadu_lst_2.append(cnt)
print(zadu_lst_1)
print(zadu_lst_2)