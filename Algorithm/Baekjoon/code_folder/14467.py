direc_lst = ['?']*11
cnt_lst = [0]*11
n = int(input())
for _ in range(n):
    cow, di = map(int,input().split())
    if direc_lst[cow] == '?':
        direc_lst[cow] = di
    elif direc_lst[cow] != di:
        direc_lst[cow] = di
        cnt_lst[cow] += 1

print(sum(cnt_lst))