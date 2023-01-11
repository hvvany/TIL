def fac(target):
    result = 1
    for i in range(target,0,-1):
        result *= i
    return result

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    answer = int(fac(m)/(fac(n)*fac(m-n)))
    print(answer)