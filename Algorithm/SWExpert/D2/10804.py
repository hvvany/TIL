t = int(input())

before_lst = [ 'b' , 'q', 'p', 'd' ]
after_lst = [ 'd', 'p', 'q', 'b' ]
for i in range(t):
    test_lst = list(map(str,input()))
    answer = ''
    for text in test_lst:
        idx = before_lst.index(text)
        answer += after_lst[idx]
    print(f'#{i+1} {answer[::-1]}')