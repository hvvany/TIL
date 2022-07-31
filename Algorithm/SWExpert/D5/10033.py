import sys
sys.stdin = open('10033.txt')



test_case = int(input())

for i in range(test_case):
    card_lst = list(map(str,input()))
    print(card_lst)
    cnt = 0
    last = 0
    while last < len(card_lst)-1:
        last = 0
        for idx in range(len(card_lst)-1):
            if card_lst[idx] == 'B'and card_lst[idx+1] == 'W':
                cnt += 1
                card_lst[idx] = 'W'
                card_lst[idx+1] = 'B'
                print(card_lst)
                break
            else:
                last += 1
    print(f'#{i+1} {cnt}')