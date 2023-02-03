from itertools import product

lst = [1,2,3]
T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(1,N+1):
        for num in product(lst,repeat=i):
            if sum(num) == N:
                cnt += 1
    print(cnt)