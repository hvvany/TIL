n, k = map(int,input().split())
lst = list(range(1,n+1))
num = 0  # 남아 있는 숫자의 번수
cnt = 0  # 정답 개수
counter = 1  # 점프 개수
answer = []
idx = 0
while cnt != n:
    idx = num % n
    m = lst[idx]
    if m != 'x':
        if counter == k:
            counter = 0
            answer.append(m)
            cnt += 1
            lst[idx] = 'x'
        counter += 1
    num += 1
print("<",end='')
print(*answer, sep=', ', end='')
print(">")