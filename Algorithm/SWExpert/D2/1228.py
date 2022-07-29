# import sys
# sys.stdin = open('1228.txt')



for number in range(10):
    l = int(input())
    raw_code_lst = list(input().split())
    fix_cnt = int(input())
    fix_code_lst = list(input().split())

    def Fix_Code(i):  # I 의 인덱스 입력
        idx = int(fix_code_lst[i+1])
        long = int(fix_code_lst[i+2])
        for cod_lst in fix_code_lst[i+3:i+3+long]:
            raw_code_lst.insert(idx,cod_lst)
            idx += 1
        return

    i = 0
    for case in fix_code_lst:
        if case == 'I':
            Fix_Code(i)
        i += 1

    print(f'#{number+1} ',end='')
    for code in raw_code_lst[0:10]:
        print(code,end=' ')
    print('')
