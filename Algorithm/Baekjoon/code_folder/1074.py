n, r, c = map(int,input().split())
answer = 0
while True:
    if n == 0:
        print(answer)
        break
    if r >= 2**(n-1):
        answer += 2**(2*n - 1)
        r -= 2**(n-1)
    if c >= 2**(n-1):
        answer += 2**(2*n - 2)
        c -= 2**(n-1)
    n -= 1