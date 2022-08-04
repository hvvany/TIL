t = int(input())
for _ in range(t):
    lst = list(map(int,input().split()))
    lst.sort(reverse=True)
    print(lst[2])