t = int(input())
for i in range(t):
    number_lst = list(map(str, input()))
    idx=0
    for number in number_lst:
        if number == '-':
            number_lst.pop(idx)
        idx += 1
    if number_lst[0] in '34569' and len(number_lst) == 16:
        answer = 1
    else:
        answer = 0
    print(f'#{i+1} {answer}')