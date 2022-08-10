t = int(input())
for _ in range(t):
    s = 0
    car = int(input())
    s += car
    n = int(input())
    for _ in range(n):
        q, p = map(int,input().split())
        s += q*p
    print(s)