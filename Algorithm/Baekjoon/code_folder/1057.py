n, s, e = map(int,input().split())
cnt = 1
while True:
    if s == e:
        print(cnt - 1)
        break
    else:
        cnt += 1
        s = (s + 1) // 2
        e = (e + 1) // 2