# 슬라이싱과 set의 콜라보
input_lst = []
char_lst = []

n, m = map(int,input().split())
for _ in range(n):
    input_lst.append(input())
for i in range(m):
    word = ''
    for alphbet in input_lst:
        word += alphbet[i]
    char_lst.append(word)

start = 0
end = n - 1
answer = n - 1
while start <= end:
    check_set = set()
    cnt = (start + end) // 2
    for sentence in char_lst:
        if sentence[-cnt-1:] in check_set:
            if n-cnt-2 < answer:
                answer = n-cnt-2
            start = cnt + 1
            break
        else:
            check_set.add(sentence[-cnt-1:])
    else:
        end = cnt - 1
print(answer)