# 후하후하후하후하 12시 전까지 풀어야 한다.

k = int(input())

num_lst = []
for _ in range(k):
    n = int(input())
    if n == 0:
        if len(num_lst) > 0:
            num_lst.pop()
    else:
        num_lst.append(n)
print(sum(num_lst))