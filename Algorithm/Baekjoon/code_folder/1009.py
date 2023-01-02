t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    lst = [str(a)[-1],str(a**2)[-1],str(a**3)[-1],str(a**4)[-1]]
    if lst[b % 4 - 1] == '0':
        print(10)
    else:
        print(lst[b % 4 - 1])
    print(lst)