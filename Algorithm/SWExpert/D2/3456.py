t = int(input())
for i in range(t):
    num_lst = list(map(int,input().split()))
    num_dic = dict()
    for number in num_lst:
        if number in num_dic:
            num_dic[number] += 1
        else:
            num_dic[number] = 1
    for key in num_dic:
        if num_dic[key] == 1 or num_dic[key] == 3:
            print(f'#{i+1} {key}')