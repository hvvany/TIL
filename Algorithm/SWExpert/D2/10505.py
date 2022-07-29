# 소득 불균형


t = int(input())
for i in range(t):
    n = int(input())
    money_lst = list(map(int,input().split()))
    avg = sum(money_lst)/n
    cnt = 0
    for money in money_lst:
        if money <= avg:
            cnt += 1
    print(f'#{i+1} {cnt}')