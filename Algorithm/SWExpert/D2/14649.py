t = int(input())
for i in range(t):
    num_lst = list(map(int,input().split()))
    num_sum = sum(num_lst[1::2]) + sum(num_lst[0::2])*2
    first_num = num_sum%10
    if first_num == 0:
        first_num = 10
    print(f'#{i+1} {10-first_num}')