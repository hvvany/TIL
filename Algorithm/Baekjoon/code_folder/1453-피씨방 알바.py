people = int(input())
lst = [0]*100
want_lst = list(map(int,input().split()))
cnt = 0
for want in want_lst:
    if lst[want-1] == 1:
        cnt += 1
    else:
        lst[want-1] = 1
print(cnt)