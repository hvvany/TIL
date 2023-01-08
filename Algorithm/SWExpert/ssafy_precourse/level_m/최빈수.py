import sys
sys.stdin = open("최빈수.txt", "r")
t = int(input())
for _ in range(t):
    test_number = int(input())
    num_dic = dict()
    num_lst = list(map(int,input().split()))
    for num in num_lst:
        if num in num_dic:
            num_dic[num] += 1
        else:
            num_dic[num] = 1
    sort_lst = sorted(num_dic.items(),key=lambda x: (x[1],x[0]),reverse=True)
    print(f'#{test_number} {sort_lst[0][0]}')